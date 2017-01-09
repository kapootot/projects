import os

def removeSubs(fname, file):
    if file.endswith(".he.srt") or file.endswith(".srt"):
    	os.remove(fname)
    	print("Removed: " + fname)

def rename(fname, file):
	newext = ".he.srt"
	if fname.endswith(".srt"):
		print("Renamed: " + fname)
		root, ext = os.path.splitext(fname)
		print(root)
		os.rename(fname, root+newext)
		print("Renamed: " + fname)

def walk(rootdir):
    for root, dirs, files in os.walk(rootdir):
        for file in files:
            fname = os.path.join(root, file)
            removeSubs(fname, file)
            #rename(fname, file)

root = "/Users/amirwaisman/Movies/"

walk(root)