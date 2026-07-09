# DESC: Convert a JSON input file into a KBB knowledge base in kb/user/
#
# NLP++ python pass. The engine invokes a python pass as:
#     python "<appdir>/spec/json2kbb.py" "<appdir>" "<inputfile>" <pre|post>
# Place it BEFORE the tokenizer so the KBB is built before later passes load it.
#
# It reads <inputfile> as JSON and writes <appdir>/kb/user/<inputstem>.kbb.
# This is the inverse of the KBFuncs.nlp JsonKB (KB -> JSON) serializer:
#   - a JSON object            -> a concept
#   - "key": <primitive>       -> an attribute on the concept:  key=value
#   - "key": { object }        -> a child concept:  key:
#   - "key": [ array ]         -> counted child concepts:  key1:, key2:, ...
#                                 (each element's members become its attrs/children;
#                                  a primitive element becomes  keyN: value=<primitive>)
# KBB text format (see the engine's parseKBBLine): 2 spaces per indent level,
# "name:" optionally followed by comma-separated "attr=value" pairs; children are
# indented +2. Values are bare when they are simple tokens, else double-quoted.
#
# Any failure (missing/!JSON input) is non-fatal: a warning is printed to stderr
# and the analyzer pipeline continues.

import sys
import os
import io
import json

INDENT = "  "  # 2 spaces per level; the engine reads indent/2 as the depth


def is_primitive(v):
    return not isinstance(v, (dict, list))


def is_simple_token(s):
    # bare (unquoted) when it is a simple identifier-ish token; else quote it
    return len(s) > 0 and all(c.isalnum() or c in "_-." for c in s)


def format_value(v):
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    s = str(v)
    if is_simple_token(s):
        return s
    s = s.replace("\\", "\\\\").replace('"', '\\"')
    return '"' + s + '"'


def split_members(obj):
    # attributes = primitive members; children = object/array members
    attrs, children = [], []
    for key, val in obj.items():
        if val is None:
            continue
        if isinstance(val, (dict, list)):
            children.append((key, val))
        else:
            attrs.append((key, val))
    return attrs, children


def write_concept_line(out, level, name, attrs):
    line = INDENT * level + str(name) + ":"
    if attrs:
        line += " " + ", ".join(k + "=" + format_value(v) for k, v in attrs)
    out.write(line + "\n")


def write_object(out, level, name, obj):
    attrs, children = split_members(obj)
    write_concept_line(out, level, name, attrs)
    write_children(out, level + 1, children)


def write_children(out, level, children):
    for key, val in children:
        if isinstance(val, dict):
            write_object(out, level, key, val)
        elif isinstance(val, list):
            for i, element in enumerate(val, start=1):
                cname = str(key) + str(i)
                if isinstance(element, dict):
                    write_object(out, level, cname, element)
                elif isinstance(element, list):
                    write_concept_line(out, level, cname, [])
                    write_children(out, level + 1, [("item", element)])
                else:
                    write_concept_line(out, level, cname, [("value", element)])


def json_to_kbb(data, root_name):
    out = io.StringIO()
    if isinstance(data, dict) and len(data) == 1 and isinstance(next(iter(data.values())), dict):
        # single object root: use the top-level key as the root concept
        (key, value), = data.items()
        write_object(out, 0, key, value)
    elif isinstance(data, dict):
        write_object(out, 0, root_name, data)
    else:
        # top-level array or primitive: wrap under a root concept named for the file
        if is_primitive(data):
            write_concept_line(out, 0, root_name, [("value", data)])
        else:
            write_concept_line(out, 0, root_name, [])
            write_children(out, 1, [("item", data)])
    return out.getvalue()


def main():
    if len(sys.argv) < 3:
        sys.stderr.write("[json2kbb: usage: json2kbb.py <appdir> <inputfile> [pre|post]]\n")
        return
    appdir = sys.argv[1]
    inputfile = sys.argv[2]

    try:
        with open(inputfile, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        sys.stderr.write("[json2kbb: could not read JSON from " + inputfile + ": " + str(e) + "]\n")
        return

    stem = os.path.splitext(os.path.basename(inputfile))[0]
    kbb = json_to_kbb(data, stem)

    kbdir = os.path.join(appdir, "kb", "user")
    os.makedirs(kbdir, exist_ok=True)
    outpath = os.path.join(kbdir, stem + ".kbb")
    try:
        with open(outpath, "w", encoding="utf-8") as f:
            f.write(kbb)
        sys.stderr.write("[json2kbb: wrote " + outpath + "]\n")
    except Exception as e:
        sys.stderr.write("[json2kbb: could not write " + outpath + ": " + str(e) + "]\n")


if __name__ == "__main__":
    main()
