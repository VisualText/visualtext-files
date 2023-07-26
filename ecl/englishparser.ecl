// Calling the full English Parer
import nlp from lib_nlp;
import Visualizer;

text01 := 'The quick brown fox jumped over the lazy boy.';
parsedtext01 := nlp.AnalyzeText('parse-en-us',text01);
parsedtext01;

p := DATASET([parsedtext01] ,{string line});

vertice := RECORD
    string id := XMLTEXT('id');
    string label := XMLTEXT('label');
END;

edge := RECORD
    string source := XMLTEXT('source');
    string target := XMLTEXT('target');
END;

vertices := PARSE(p, line, vertice, XML('vertice'));
data_vertices := output(vertices, NAMED('graph_vertice'));

edges := PARSE(p, line, edge, XML('edge'));
data_edges := output(edges, NAMED('graph_edges'));

parsetree := Visualizer.Relational.Network('graph', 'graph_vertices',,,,, 'graph_edges',,,,);