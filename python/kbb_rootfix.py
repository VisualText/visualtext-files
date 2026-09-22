# DESC: Correct wrong root= lemmas in en-feat-full.dict, and rebuild en-full.kbb from it.
#
# WHAT IT DOES
#   en-feat-full.dict gives every inflected reading its root, and some of those
#   roots are a different word that happens to share the surface form:
#
#       states     pos=noun root=stat        should be state
#       oranges    pos=noun root=orang       should be orange
#       developed  pos=verb root=develope    should be develop
#
#   The suspects are found mechanically: some OTHER base word of the same part
#   of speech regularly inflects to the same form (-s/-es/-ies, -d/-ed/-ied,
#   -ing, a doubled final consonant).  WordNet then decides each one:
#
#     keep    WordNet lists form -> root as an irregular
#             (leaves -> leaf, crises -> crisis, axes -> ax)
#     keep    the alternative's own paradigm already has a different form of
#             this kind ("bar" has "barred", so "bared" is not bar's)
#     switch  the root cannot produce the form by regular spelling (orang+es)
#             and exactly one alternative is a WordNet lemma
#     switch  the root is not a WordNet lemma and exactly one alternative is
#             (develope -> develop, calory -> calorie)
#     switch  both are plausible and WordNet's usage counts favour the
#             alternative (cooky -> cookie, us -> use) -- except the NOFREQ
#             forms, reviewed by hand, where the commoner word is the wrong one
#             (putted is putt's, not put's)
#     keep    everything else: two plausible variants (aunty / auntie)
#
#   The plan is written as a TSV, one row per suspect reading with the reason,
#   so it can be read before it is applied.  en-lemmas.kbb and en-roots.kbb are
#   generated from en-full.kbb and must be regenerated afterwards.
#
# REQUIRES
#   nltk with the WordNet corpus:
#     pip install nltk
#     python -m nltk.downloader wordnet
#
# USAGE
#   python kbb_rootfix.py plan  en-feat-full.dict plan.tsv
#   python kbb_rootfix.py apply en-feat-full.dict plan.tsv      rewrites the dict in place
#   python kbb_rootfix.py kbb   en-feat-full.dict en-full.kbb   rebuilds the knowledge base
#   python kbb_lemmas.py en-full.kbb en-lemmas.kbb
#   python kbb_roots.py  en-full.kbb en-roots.kbb
#
#   Repeat plan and apply until plan proposes nothing.  One fix can release
#   another: while "internees" is still wrongly filed under interne, interne's
#   paradigm looks taken and "internes" cannot move to it.  The first run over
#   the shipped dictionary fixes 589 forms and the second 3 more; a third
#   proposes nothing.
#
#   "kbb" reproduces the shipped en-full.kbb byte for byte from an unmodified
#   en-feat-full.dict, so a diff of the rebuilt file shows only the fixes.

import sys, collections
from nltk.corpus import wordnet as wn

V = 'aeiou'; SIB = ('s', 'x', 'z', 'ch', 'sh')
def plural(b):
    out = set()
    if b.endswith(SIB) or b.endswith('o'): out.add(b + 'es')
    if b.endswith('y') and len(b) > 1 and b[-2] not in V: out.add(b[:-1] + 'ies')
    elif not b.endswith(SIB): out.add(b + 's')
    return out
def dbl(b): return len(b) >= 3 and b[-1] not in V + 'wxy' and b[-2] in V and b[-3] not in V
def past(b):
    if b.endswith('e'): return {b + 'd'}
    if b.endswith('y') and len(b) > 1 and b[-2] not in V: return {b[:-1] + 'ied'}
    return {b + 'ed'} | ({b + b[-1] + 'ed'} if dbl(b) else set())
def ger(b):
    if b.endswith('ie'): return {b[:-2] + 'ying'}
    if b.endswith('e') and not b.endswith(('ee', 'ye', 'oe')): return {b[:-1] + 'ing'}
    return {b + 'ing'} | ({b + b[-1] + 'ing'} if dbl(b) else set())
GEN = {('noun', 'plural'): plural, ('verb', 'pres3sg'): plural, ('verb', 'past'): past,
       ('verb', 'pastpart'): past, ('verb', 'ger'): ger}
WNPOS = {'noun': wn.NOUN, 'verb': wn.VERB}
NOFREQ = {'putted', 'routed', 'routing'}
def cnt(w, pos): return sum(l.count() for l in wn.lemmas(w, pos=WNPOS[pos]))

def read_dict(path):
    raw = open(path, 'rb').read().decode('utf-8')
    nl = '\r\n' if '\r\n' in raw else '\n'
    lines = raw.split(nl)
    recs = []                        # (lineno, word, [(k, v)])
    for i, line in enumerate(lines):
        if not line.strip() or line.lstrip().startswith('#'): continue
        toks = line.split()
        j = 0
        while j < len(toks) and '=' not in toks[j]: j += 1
        recs.append((i, ' '.join(toks[:j]), [tuple(t.split('=', 1)) for t in toks[j:]]))
    return lines, nl, recs

def kind_of(a):
    pos = a.get('pos')
    return pos, ('plural' if pos == 'noun' else a.get('vform'))

def plan(path, out):
    lines, nl, recs = read_dict(path)
    readings = collections.defaultdict(list)
    for _, w, kv in recs: readings[w].append(dict(kv))
    index = collections.defaultdict(set)      # (form,pos,kind) -> bases
    rootforms = collections.defaultdict(set)  # (root,pos,kind) -> forms attributed to it
    for w, rs in readings.items():
        for a in rs:
            pos, kind = kind_of(a)
            if 'root' in a:
                rootforms[(a['root'], pos, kind)].add(w)
            elif pos in ('noun', 'verb'):
                for (p, k), f in GEN.items():
                    if p == pos:
                        for form in f(w): index[(form, pos, k)].add(w)
    isl = lambda w, pos: bool(wn.lemmas(w, pos=WNPOS[pos]))
    rows, seen, stats = [], set(), collections.Counter()
    for w, rs in readings.items():
        for a in rs:
            pos, kind = kind_of(a); root = a.get('root')
            if (pos, kind) not in GEN or not root: continue
            key = (w, pos, root)
            if key in seen: continue
            listed = {x.get('root') for x in rs if x.get('pos') == pos}
            alts = index[(w, pos, kind)] - listed
            if not alts: continue
            seen.add(key)
            cls = 'valid' if w in GEN[(pos, kind)](root) else 'invalid'
            # an alternative whose own paradigm already lists a DIFFERENT form of
            # this kind does not inflect to this one ("bar" has "barred", not "bared")
            cands = sorted(b for b in alts if not (rootforms[(b, pos, kind)] - {w}))
            exc = root in wn._exception_map[WNPOS[pos]].get(w, [])
            wnc = [b for b in cands if isl(b, pos)]
            new, why = None, ''
            if exc:
                why = 'keep: WordNet lists it as irregular'
            elif not cands:
                why = 'keep: alternatives inflect differently'
            elif cls == 'invalid' and len(wnc) == 1:
                new, why = wnc[0], 'root cannot inflect to form; WordNet has the new base'
            elif cls == 'invalid' and not wnc and len(cands) == 1 and not isl(root, pos):
                new, why = cands[0], 'root cannot inflect to form; neither in WordNet'
            elif cls == 'valid' and len(wnc) == 1 and not isl(root, pos):
                new, why = wnc[0], 'variant root not in WordNet; new base is'
            else:
                # both plausible: WordNet's usage counts decide, when they favour
                # the alternative at all
                rc = cnt(root, pos)
                best = max(wnc, key=lambda b: cnt(b, pos)) if wnc else None
                if best and cnt(best, pos) > rc and w not in NOFREQ:
                    new, why = best, 'ambiguous; WordNet usage favours the new base'
                else:
                    why = 'keep: ambiguous'
            stats[(cls, 'fix' if new else why)] += 1
            rows.append((w, pos, root, new or '', cls, ','.join(cands), why))
    with open(out, 'w', encoding='utf-8', newline='\n') as f:
        for r in rows: f.write('\t'.join(r) + '\n')
    for k, v in sorted(stats.items()): print(v, k)
    print(sum(1 for r in rows if r[3]), 'forms to fix ->', out)

def apply(path, planpath):
    fixes = {}
    for line in open(planpath, encoding='utf-8'):
        w, pos, old, new = line.rstrip('\n').split('\t')[:4]
        if new: fixes[(w, pos, old)] = new
    lines, nl, recs = read_dict(path)
    n = 0
    for i, w, kv in recs:
        a = dict(kv)
        new = fixes.get((w, a.get('pos'), a.get('root')))
        if new:
            lines[i] = ' '.join([w] + [k + '=' + (new if k == 'root' else v) for k, v in kv])
            n += 1
    open(path, 'wb').write(nl.join(lines).encode('utf-8'))
    print('rewrote', n, 'readings for', len(fixes), 'forms')

def kbb(path, out):
    lines, nl, recs = read_dict(path)
    words = collections.OrderedDict()
    for _, w, kv in recs: words.setdefault(w, []).append(kv)
    buf = ['# Full English Dictionary knowledge base', 'dictionary']
    for w, rs in words.items():
        buf.append('  ' + w + ':')
        for i, kv in enumerate(rs, 1):
            buf.append('    m%02d: ' % i + ' '.join(k + '=' + v for k, v in kv))
    open(out, 'wb').write('\r\n'.join(buf).encode('utf-8'))   # the shipped file has no final newline

if __name__ == '__main__':
    modes = {'plan': plan, 'apply': apply, 'kbb': kbb}
    if len(sys.argv) != 4 or sys.argv[1] not in modes:
        sys.stderr.write('usage: kbb_rootfix.py plan|apply|kbb <en-feat-full.dict> <file>\n')
        sys.exit(1)
    modes[sys.argv[1]](sys.argv[2], sys.argv[3])
