#########################
# 01/2016               #
#                       #
# @author: Amir Waisman #
#########################

import os
import shutil

imageExtensions = [".arw", ".bmp", ".cr2", ".crw", ".dcm", ".dds", ".djvu", ".gif", ".jpeg", ".jpg", ".png", ".psd",
                   ".tif", ".tiff"]
rootDir = "/Users/amirwaisman/Pictures/"
outputDir = "/Users/amirwaisman/outputDir/"
sizes = []
dirs = []

def uniquePics(fname):
    outDir = createOutDir()

    fileDir = outputDir + os.path.basename(os.path.split(fname)[0])

    if not fileDir in dirs:
        if not os.path.exists(fileDir):
            os.makedirs(fileDir)

    size = os.path.getsize(fname)
    if size in sizes:
        return
    else:
        sizes.append(size)
        shutil.copy2(fname, fileDir)


def createOutDir():
    outDir = os.path.basename(outputDir)
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
    return outputDir

# method for verifying that the file is an image
def checkImageExtensions(file):
    ext = os.path.splitext(file)[1]
    if ext in imageExtensions:
        return True
    else:
        return False


# Walk function
def walk(rootdir):
    src = 0
    out = 0
    for root, dirs, files in os.walk(rootdir):
        for file in files:
            fname = os.path.join(root, file)
            if checkImageExtensions(file):
                src += 1
                uniquePics(fname)
    return (str(src))

def listFileNames(rootdir):
    for root, dirs, files in os.walk(rootdir):
        for file in files:
            if checkImageExtensions(file):
                print(file)

def countOutFiles(rootdir):
    out = 0
    for root, dirs, files in os.walk(rootdir):
        for file in files:
            if checkImageExtensions(file):
                out += 1
    return str(out)

def main():
    numSrc = walk(rootDir)
    numOut = countOutFiles(outputDir)
    print("\nNumber of source image files: " + numSrc)
    print("\nNumber of unique image files in output dir: " + numOut)

    # TO DO: List total folder sizes

    #print "\nSource files:\n"
    #listFileNames(rootDir)

    #print "\nUnique files:\n"
    #listFileNames(outputDir)

if __name__ == '__main__':
    main()