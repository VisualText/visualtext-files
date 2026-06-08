# Obtaining and Installing VisualText™

VisualText can be downloaded over the internet. In order to do this, contact [Text Analysis International, Inc.](../Text_Analysis_International/Contact_Information.md#Contact_Info) for the appropriate password and file name.

## Downloading VisualText

In most cases, you will download VisualText directly from the Text Analysis International website, at

http://www.textanalysis.com

You will be asked to type in your user name (usually your email address) and a password supplied when you purchased the product.  You will then select the download file and browse to a location on your machine for downloading the file.  Remember where you placed the downloaded file, as you will need to run it (e.g., by double-clicking on it) in order to install the product on you machine.  Follow the instructions in the popup screens of the installation program.

Some materials (e.g., sample tutorials) will be installed in the form of compressed .zip files. If you do not have decompression software to access these files, you can download WinZip from http://www.zdnet.com/downloads.

## Downloading via FTP

In some cases, you may be given a password and instructions for downloading material from Text Analysis International via an FTP address.

## Installing VisualText

Before starting the installation process, make sure the information on your computer is backed up.

| **Note**: If you already have a version of VisualText on your computer, you must first remove the older version before you can install the newer one, as described below. Once you have done this, restart the install program to install the newer version. |
| --- |

Start the installation process by double clicking on the VisualText program icon in the directory where you downloaded the VisualText software. This will launch the VisualText InstallShield Wizard.

**To Remove a Previous Installation of VisualText**:

- Click on the Windows **Start** button at the bottom left of your screen.

- Select **Settings** and within that select **Control Panel**. The Control Panel window opens.

- In the Control Panel window, double-click the icon labeled **Add/Remove Programs**.

- Scroll to find VisualText and double-click that entry. The VisualText InstallShield Wizard appears.

- Select '**Remove**' from the Welcome dialog box, if not already selected. Then click on **Next**.

- On the Confirm File Deletion dialog, click **OK** to completely remove the application and all the components.

- Select '**Finish**' and continue with the install as directed below.

- Old beta versions of VisualText employed a file called C:\autoexec.bat .  If you installed such a beta, you may should check that this file is cleaned of VisualText-specific definitions.  Right-click on the autoexec.bat file and select Edit to modify the file.

| **Note**: It is not necessary nor will you be prompted to reboot your machine after an earlier version of the software has been removed. |
| --- |

**To Install VisualText**:

- Double-click the installation program icon again to start the installation process.

- Before starting the installation procedure, make sure to close all open programs.

- Double-click the install program and follow the prompts from the InstallShield Wizard Welcome dialog.

- Click **Yes** to confirm the license agreement.

- On the Customer Information dialog, supply your name and company name. Leave serial number as is.

- Select a destination **folder** for the installation.  The default is C:\Program Files\TextAI.

- For Setup Type, select **typical**.

- In the Select Program Folder, select VisualText for Program Folders and Administrative Tools for Existing Folders.

- On the Start Copying Files dialog, select **Next**. (The InstallShield Wizard will finish the installation.)

- If present, select "**Yes, restart my computer now**" on the Reboot dialog. (Make sure to close all open applications before rebooting.)

If you are installing VisualText and there was an older version on your machine, make sure that any shortcuts you've created point to the right one. Also, note that any subdirectories and files you may have created under the VisualText path will not be removed when you remove an existing installation. Therefore, you may wish to move or delete those old files. In addition, you can delete the compressed .zip download file to save space.

## Installation Files

- Programs, libraries, help files, and the like are installed at the program location, which defaults to

```
C:\Program Files\TextAI\VisualText\
```

Note: This default location is the assumed installation location in the [tutorials](../Tutorials/Tutorial_Introduction.md) and discussions in this documentation.

- For user-built analyzers (as in the tutorials) the default working directory is:

```
C:\apps
```

- The VisualText executable is **VisualText.exe** and is located in

```
C:\Program Files\TextAI\VisualText\bin\VisualText.exe.
```

- The VisualText™ Help file is **Help.chm** and is located in

```
C:\Program Files\TextAI\VisualText\Help\Help.chm.
```

- The** tutorial analyzers**, which can be used in tandem with the Help, are in zip files located in

```
C:\Program Files\TextAI\VisualText\docs
```

The VisualText installation program creates a program folder containing the VisualText icon, Help documentation, and Release Notes in the Start menu under Programs > VisualText.

## Release Report

A Release Report containing known issues and notes on features can be found in a file called ReleaseNotes.txt in the docs folder:

```
C:\Program Files\TextAI\VisualText\docs\ReleaseNotes.txt
```

To see a related list in the Help, refer to [Programming Notes and Issues](Caveats_and_Limitations.md).
