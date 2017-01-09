import re, os


def getMovName(movieName):
    #movieName = "The.Rover.2014.1080p-720p.BluRay.x264.YIFY.Eng"
    m = re.search('[\w+\.]+', movieName)
    shortText = m.group(0)
    strs = shortText.split(".")
    names = strs[:-2]
    movname = ""
    for name in names:
        movname = movname + " " + name

    movname = movname[1:]
    return movname

def getFileName(path):
    osName = os.name
    if (osName=="posix") or (osName=="mac"):
        strs = path.split("/")
    else:
        strs = path.split("\\")
    fileName = strs[len(strs)-1]
    return fileName

if __name__ == '__main__':
    getFileName("/Users/amirwaisman/Movies/r/The.Shield.S04E08.Cut.Throat.DVDRip.XviD-Rogue.avi")
