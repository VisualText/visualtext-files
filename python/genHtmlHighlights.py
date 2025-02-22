import shutil
import os
from nlpengine import NLPEngine

def moveFiles(sourcePath, fileExtension, destPath, clearFolder=True):
    for file in os.listdir(sourcePath):
        if file.endswith(fileExtension):
            full_file_path = os.path.join(sourcePath, file)
            if os.path.isfile(full_file_path):
                shutil.copy(full_file_path, destPath)

def deleteHightlightFiles(analyzerPath):  
    deleteFileExtensions(os.path.join(analyzerPath,"spec"), ".html")
    deleteFileExtensions(os.path.join(analyzerPath,"kb","user"), ".html")
    deleteFileExtensions(os.path.join(analyzerPath,"input","text.txt_log"), ".html")

def deleteFileExtensions(folder, fileExtension):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(fileExtension):
                os.remove(os.path.join(root, file))

engineDir = os.getcwd()
nlp = NLPEngine(engineDir,os.path.join(engineDir,"analyzers"))
nlp2 = NLPEngine(engineDir,os.path.join(engineDir,"colorizers"))

analyzer_folders = [name for name in os.listdir(nlp.analyzersDir) if os.path.isdir(os.path.join(nlp.analyzersDir, name))]
for analyzer in analyzer_folders:
    analyzerPath = nlp.analyzerPath(analyzer)
    if not nlp.isAnalyzerFolder(os.path.join(nlp.analyzersDir, analyzer)):
        continue

    if analyzer != "date-time":
        continue
    
    deleteHightlightFiles(analyzerPath)
    print(f"Processing {analyzer}...")
    nlp.analyzeInput(analyzer, "text.txt", True)

    colorizer_folders = [name for name in os.listdir("colorizers") if os.path.isdir(os.path.join("colorizers", name))]
    for colorizer in colorizer_folders:
        if colorizer in ["tree", "nlp", "dict", "kb"]:
            print(f"  Processing {colorizer}...")
            colorizerPath = nlp2.analyzerPath(colorizer)
            htmlPath = nlp2.createInputDir(colorizer,"html",True)
            filesPath = nlp2.createInputDir(colorizer,"files",True)

        if colorizer == "tree":
            sourcePath = nlp.inputTextLog(analyzer, "text.txt")
            moveFiles(sourcePath, ".tree", filesPath)
            nlp2.analyzeInput(colorizer, "files", True)
            moveFiles(htmlPath, ".html", sourcePath)
        elif colorizer == "nlp":
            sourcePath = nlp.specPath(analyzer)
            moveFiles(sourcePath, ".nlp", filesPath)
            nlp2.analyzeInput(colorizer, "files", True)
            moveFiles(htmlPath, ".html", sourcePath)
        elif colorizer == "dict":
            sourcePath = nlp.kbPath(analyzer)
            moveFiles(sourcePath, ".dict", filesPath)
            nlp2.analyzeInput(colorizer, "files", True)
            moveFiles(htmlPath, ".html", sourcePath)
        elif colorizer == "kb":
            # KBB files in the KB folder
            sourcePath = nlp.kbPath(analyzer)
            moveFiles(sourcePath, ".kbb", filesPath)
            nlp2.analyzeInput(colorizer, "files", True)
            moveFiles(htmlPath, ".html", sourcePath)

            # KBB files text.txt_log folder
            sourcePath = nlp.inputTextLog(analyzer, "text.txt")
            moveFiles(sourcePath, ".kbb", filesPath)
            nlp2.analyzeInput(colorizer, "files", True)
            moveFiles(htmlPath, ".html", sourcePath)

print("Done!")