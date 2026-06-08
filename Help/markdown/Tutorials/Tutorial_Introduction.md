[← Help Contents](../index.md) | [📘 NLP++ Textbook](../NLP++_Textbook.md)

# Tutorial Introduction

## Tutorial Structure

Six tutorials guide you through the basics of VisualText™. You should follow them in order; each takes about an hour.

The tutorials generally build on each other, so that the analyzer used in Tutorial 2 is the one that was created in Tutorial 1.  Because of this, if you change file names, variable names, etc., from what is presented in a tutorial, later tutorials may not work as described.  However, the release provides six tutorial analyzer projects, one for each tutorial, so that you could start Tutorial 2 with the analyzer built by Tutorial 1, and so on.

## Tutorial Analyzers

NOTE: In some versions of VisualText, the zipped tutorial analyzers are absent or obsolete, so it is best to start from scratch with Tutorial 1.

The tutorial analyzer projects are in folders named

```
C:\Program Files\TextAI\VisualText\docs\tutorialN
```

where N is the tutorial number.  So, for example, the analyzer created by following Tutorial 1 resides at

```
C:\Program Files\TextAI\VisualText\docs\tutorial1\myAnalyzer1.zip
```

(Note: The assumed installation location is C:\Program Files. The exact path to these files will of course depend on where you installed the software.) If you do not have decompression software to access these files, you can download WinZip from a website such as:

http://www.winzip.com

If you need to look at working code or start a new tutorial in sync with the documentation, you can copy the tutorial analyzer in question out of the docs folder in the install directories and into the working directory.  We've set up the working directory for the tutorial analyzers to be:

```
C:\apps\myAnalyzerFolder\
```

Suppose you wanted to start Tutorial 3 with a clean copy of the analyzer created in Tutorial 2. You would go to the install directory containing the zipped tutorial, in this case:

```
C:\Program Files\TextAI\VisualText\docs\tutorial2
```

and unzip the myAnalyzer2.zip file. (When unzipping your files, it is best to keep the unzipped files in a different directory than the working directory.) When you unzip the file, it uncompresses to the folder called myAnalyzer.

Place the myAnalyzer folder into the working directory:

```
C:\apps\myAnalyzerFolder\
```

Since the first tutorial starts from scratch, you cannot start out Tutorial 1 in this way.

## Additional Notes

Here are a few extra notes before starting the tutorials.

- You can view the Help documentation outside of VisualText.  You can find it in the Start button under Programs, or at the location

```
C:\Program Files\TextAI\VisualText\Help.chm
```

- The toolbars and windows presented in this tutorial are assumed to be in the same position as they are when you first launch VisualText. As you will learn in the Interface section, toolbars and windows can be moved around to different locations. If you have experimented with the VisualText interface before starting this tutorial, the toolbar graphics may not precisely match what you see in these tutorials.

- ![](../../helps/Tutorials/GO.gif) The right-arrow symbol, such as the one at the beginning of this line, points you to the next action you have to take in executing a tutorial.

## Tutorial Description

Six tutorials guide you through the basics of creating an analyzer. Along the way, you will also be introduced to various tools and aspects of the VisualText work environment. Below is a description of each tutorial.  You may find it useful to scan through the tutorials to familiarize yourself with the content before actually starting the tutorials.

- [Tutorial 1](tutorial1/tutorial.md): Creating new analyzers

- [Tutorial 2](tutorial2/tutorial2.md): Sampling data and automatically generating analyzer rules

- [Tutorial 3](tutorial3/tutorial3.md): Creating analyzer rules by hand

- [Tutorial 4](tutorial4/tutorial4.md): Using input and output files

- [Tutorial 5](tutorial5/tutorial5.md): Introduction to NLP++™

- [Tutorial 6](tutorial6/tutorial6.md): Working with rule types and rule construction
