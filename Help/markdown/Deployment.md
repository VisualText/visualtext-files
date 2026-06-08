[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# Deployment

VisualText is now delivered as a VSCode language extension, so getting started takes only a few steps:

1. **Download and install Visual Studio Code** from [https://code.visualstudio.com](https://code.visualstudio.com), then launch it.
2. **Open the Extensions view** and type **`nlp`** into the extensions search box.
3. **Install the VisualText (NLP++) extension** by clicking its **Install** button. The required NLP-ENGINE is included with the extension.
4. **Click "VisualText" in the bottom panel** to open the VisualText views.
5. **Click the "cog" (gear) icon** to download and set up the NLP-ENGINE and the example analyzers.
6. **Start building analyzers.** You can now create, edit, and run NLP++ analyzers right inside VSCode.

The extension runs on **Linux, Windows, and macOS**.

▶ **Quick start video:** [Getting started with VisualText](https://youtu.be/xGbGYj9ixv4)

## Running and Distributing Analyzers

Analyzers can run inside VisualText, as standalone programs, or embedded within other programs. See the [Compiled and Standalone Analyzers](VisualText_Basics/Compiled_and_Standalone_Analyzers.md) topic for technical details.

Beginning with Version 3, analyzers and the knowledge base (KB) can be compiled to C++ libraries for faster execution and for protecting native NLP++ source code when delivering analyzers to customers. Analyzers can be compiled locally (using a C++ toolchain on your machine) or in the cloud (no local toolchain required).

VisualText supports analyzers that process **Unicode** (UTF-8 via the ICU C++ package), addressing all the world's languages and mixed-language texts, including emojis.

## Questions?

Contact us at [contact@visualtext.org](mailto:contact@visualtext.org), or join the discussion on our [Discourse forum](https://nlp.discourse.group).
