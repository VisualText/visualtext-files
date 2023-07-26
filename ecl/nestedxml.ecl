// Generate nested xml
import nlp from lib_nlp;

article := RECORD
  STRING title;
  STRING url;
  STRING text;
END;

articles := DATASET('~xml::files::datafiles.xml',article,XML('articles/article'));
articles;

nlpResults := RECORD
  STRING title;
  INTEGER id;
  STRING url;
  STRING text;
  STRING xmlEntities;
END;
  
nlpResults ExtractEntities(article L, INTEGER c) := TRANSFORM
  SELF.title := L.title;
  SELF.id := c;
  SELF.url := L.url;
  SELF.text := L.text;
  SELF.xmlEntities := nlp.AnalyzeText('NLPAnalzyer',L.text);
END;

entities := PROJECT(articles,ExtractEntities(LEFT,COUNTER));
entities;

entityrec := RECORD
  STRING title;
  STRING name;
  END;

parsedrec := RECORD
  STRING text;
  DATASET(entityrec) entities;
  END;

parsedrec t1(linerec L) := TRANSFORM
  SELF.text := L.text;
  SELF.entities := XMLPROJECT('entity',
                            TRANSFORM(entityrec,
                                      SELF.title := XMLTEXT('title'),
                                      SELF.name := XMLTEXT('name')))
  END;

out := PARSE(entities, xmlEntities, t1(LEFT), XML('xml'));
out;
