# POStagger

**NOTE:** We are no longer bundling and distributing this third party tagger, as its licensing is incompatible with the commercial uses of VisualText.

Our most recent part-of-speech tagger that keys off our TAIParse general analyzer for English is described at [TAIParse.](TAIParse.md)

The POStagger analyzer project can be found in VisualText\apps.  As an example, it invokes the LexTagger part-of-speech tagger from UMIST, which is available in VisualText\apps\LexTagger-1.0 and also by contacting the author, Argyris Vasilakopoulos, for updates and documentation at

[a.vasilakopoulos@postgrad.umist.ac.uk](mailto:a.vasilakopoulos@postgrad.umist.ac.uk)

The POStagger analyzer consists of only two passes.  The first is the default tokenize pass that initiates all VisualText analyzers.  The second pass looks like

@CODE user::postagger(); @@CODE

which invokes the LexTagger software with the current input file, then parses the result and layers it into the analyzer's current parse tree.  The handshake code can be found in POStagger\User, within the Ucode.cpp and Umisc.cpp files.

In order to use the analyzer, you'll need to edit the **run.bat** and the **Properties.txt** files within the LexTagger-1.0 folder, in order to fix the pathnames for your machine.  You'll also need to edit the paths in the User project to point to your copy of LexTagger.

Note that the current handshake code in the User project copies the input file to the LexTagger-1.0\test folder.  A more elegant handshake would write out the Properties.txt file for each input, so that large input files won't need to be copied.

Other part-of-speech taggers could easily be swapped in for LexTagger with some editing of the example handshake in the User project.
