import shutil
import subprocess
import os

class NLPEngine:

    def __init__(self, engineDir, analyzersDir ):
        self.engineDir = engineDir
        self.analyzersDir = analyzersDir

    def analyzerPath(self, analyzerFolder):
        return os.path.join(self.analyzersDir, analyzerFolder)
    
    def kbPath(self, analyzerFolder):    
        return os.path.join(self.analyzerPath(analyzerFolder), "kb", "user")
    
    def specPath(self, analyzerFolder):
        return os.path.join(self.analyzerPath(analyzerFolder), "spec")
    
    def outputDir(self, analyzerFolder, textPath):    
        return os.path.join(self.analyzerPath(analyzerFolder), "input", textPath+"_log")
    
    def outputFileContents(self, analyzerFolder, filename, outputFile):
        outputPath = os.path.join(self.outputDir(analyzerFolder, filename), outputFile)
        with open(outputPath, "r") as file:
            contents = file.read()
        return contents
    
    def inputFileDir(self, analyzerFolder, textPath):    
        return os.path.join(self.analyzerPath(analyzerFolder), "input", textPath)

    def analyzeFile(self, analyzerFolder, textPath, dev=False):
        self.clearLogFiles(analyzerFolder)
        analyzerPath = os.path.join(self.analyzersDir, analyzerFolder)
        textPath = os.path.join(analyzerPath, "input", textPath)
        try:
            executable_path = os.path.join(self.engineDir, "nlp.exe")
            args = [executable_path, "-ANA", analyzerPath, "-WORK", self.engineDir, textPath]
            if dev:
                args.append("-DEV")

            with open("output.txt", "w") as output_file, open("errors.txt", "w") as error_file:
                subprocess.run(args, stdout=output_file, stderr=error_file, text=True)
        
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
            return
    
    def analyzeStr(self, analyzerFolder, filename, textStr):
        inputPath = self.inputFileDir(analyzerFolder,filename)
        with open(inputPath, "w") as input_file:
            input_file.write(textStr)
        self.analyzeFile(analyzerFolder, filename, False)
        
    def isAnalyzerFolder(self, analyzerFolder):
        required_folders = ['spec', 'input', 'kb/user']
        for folder in required_folders:
            if not os.path.isdir(os.path.join(self.analyzersDir, analyzerFolder, folder)):
                return False
        return True
    
    def clearLogFiles(self, analyzerFolder):
        logPath = os.path.join(os.path.join(self.analyzersDir,analyzerFolder), "input")
        for root, dirs, files in os.walk(logPath):
            for dir in dirs:
                if dir.endswith("_log"):
                    shutil.rmtree(os.path.join(root, dir))

    def createInputDir(self, analyzer, inputFolder, clearFolder=True):
        inputPath = os.path.join(self.analyzerPath(analyzer), "input", inputFolder)
        if clearFolder and os.path.exists(inputPath):
            shutil.rmtree(inputPath)
            shutil.os.makedirs(inputPath)
        if not os.path.exists(inputPath):
            os.makedirs(inputPath)
        return inputPath