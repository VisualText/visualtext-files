# Writing Analyzers with VisualText

The VisualText Basics section includes a set of topics designed to help you build analyzers. As a prerequisite, we recommend you work through the Tutorials to understand the workings of the VisualText GUI. Also, working through the Corporate analyzer documentation and studying the Corporate analyzer will provide a feel for the ordering and specification of the steps, or passes, in a text analyzer.

Building text analyzers is more art than science. VisualText favors a bottom up approach to text processing, where small constructs are processed and grouped (or reduced) first, followed by identification of successively larger components of a text.

One approach that often works well for restricted domains is to create a prototype that processes a single input text end-to-end, to produce the desired analyzer output. In building such a prototype, you should strive to build each pass in as general a way as possible. Once such a prototype is built, a second input text is tested, and the analyzer is reworked so that both inputs are processed in a general way. As more inputs are handled in this fashion, the analyzer will perform better and do more with unseen texts. In a restricted domain, even a small number of representative input texts (e.g., 25-50) can yield dramatic improvements in the processing of novel texts.

Another aspect of this approach is that it is "knowledge free." For a restricted domain, you don't usually need an ontology or knowledge base for all human knowledge. You build or import knowledge as needed. The broader the domain, of course, the more the analyzer will benefit from large-coverage knowledge bases, such as WordNet.

If you are interested in pre-built generic text analysis capabilities for VisualText, you may wish to download one of the versions of TAIParse available in the Apps section of our website at

http://www.textanalysis.com/Apps/apps.html
