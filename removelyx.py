from os import listdir
from os.path import isfile, join, dirname, realpath
mypath = dirname(realpath(__file__))
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlytexfiles = [f for f in onlyfiles if ".tex" in f]
print ("Checking .tex files...")
numlyxfiles = 0
for texfile in onlytexfiles:
    print("\t{}".format(texfile))
    with open(texfile, 'r+') as f:
        filetext = f.readlines()
        if len(filetext) > 0:
            if "http://www.lyx.org/" in filetext[0]:
                numlyxfiles += 1
                endheaderindex = 0
                while endheaderindex < len(filetext):
                    endheaderindex += 1
                    if "begin{document}" in filetext[endheaderindex]:
                        break
                print("\t\tRemoved LyX header")
                f.seek(0)
                f.truncate()
                f.writelines(filetext[endheaderindex+2:-2])
print("Finished checking files; {} LyX headers and footers removed".format(numlyxfiles))