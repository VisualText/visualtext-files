# Deployment

Analyzers can run inside VisualText, as standalone programs, or embedded within other programs.  See the [Compiled and Standalone Analyzers](VisualText_Basics/Compiled_and_Standalone_Analyzers.md) topic for technical details.

Analyzers built with VisualText are now readily available.  See the Apps tab of our website above for [TAIParse](TAIParse.md), our advanced analyzer for general English text.  TAIParse currently performs accurate part-of-speech tagging (93+% in internal blind tests) and also supports chunking, parsing, and semantic analysis of text.  Passes that use HTML and/or strip it out are available and can easily be extended.

A [Resume Analyzer](Resume_Analyzer.md) prototype at about 80% accuracy (internal blind testing) is also available on the web site.  TAI has constructed numerous other analyzers that will be made available periodically at the Apps tab.

A bridge enabling **.NET** programs to call analyzers is also available.  See the VisualText\apps\DotNetTest and DotNetWeb folders in the product installation for sample deployments.  These use the libraries DotNetAPI and DotNetBridge, both in VisualText\bin.

VisualText now supports analyzers that process **Unicode**, addressing all the world's languages (and mixed-language texts).

A **Java** bridge is not part of the release, but examples of Java programs calling C++ libraries are readily available on the Web.  If you need help with that, please contact us.

A Gnu/C++/Linux version of the VisualText runtime libraries, enabling analyzers to run on **Linux** platforms, is available.

Questions?  Contact us at support@textanalysis.com, 1-949-376-8507.  Business line at 1-877-235-6259.
