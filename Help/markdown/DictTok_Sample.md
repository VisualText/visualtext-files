# DictTok_Sample

[All sample analyzers are in Program Files\TexAI\VisualText\apps.]

Shows how to install and use the new DICTTOK analyzer pass.

Basically you just edit the analyzer.seq file for your project by changing "tokenize" to "dicttok".

Then you need to make a knowledge base with POS information.  Or swap in the KB files from the TAIPARSE\BIN folder to the BIN folder of your analyzer project.

**WARNING:**  We assume you are using an empty or "don't care" knowledge base that comes with the analyzer project by default.  If you've built your own KB, you can rebuild it starting with the TAIParse knowledge base.  TAI support can help you start building your own KBs, just send us an email at support@textanalysis.com .
