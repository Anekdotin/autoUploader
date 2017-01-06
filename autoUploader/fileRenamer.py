import os
directoryChosen = '/Users/eeamesX/work/transcriptions/testFolder1'
directoryChosen2 = '/Users/eeamesX/work/transcriptions/testFolder2'
directoryChosen3 = '/Users/eeamesX/work/transcriptions/testFolder3'




for f in os.listdir(directoryChosen):
    if f.endswith(".csv"):
        # getfilename + directory
        infilename = os.path.join(directoryChosen, f)
        # getfilename

        oldbase = os.path.splitext(f)
        # Newname

        newname = directoryChosen + '/' + oldbase[0] + ".xlsx"

        # function to rename files
        print infilename
        print newname
        os.rename(infilename, newname)

for f in os.listdir(directoryChosen2):
    if f.endswith(".csv"):
        # getfilename + directory
        infilename = os.path.join(directoryChosen2, f)
        # getfilename

        oldbase = os.path.splitext(f)
        # Newname

        newname = directoryChosen2 + '/' + oldbase[0] + ".xlsx"

        # function to rename files
        print infilename
        print newname
        os.rename(infilename, newname)


for f in os.listdir(directoryChosen3):
    if f.endswith(".csv"):
        # getfilename + directory
        infilename = os.path.join(directoryChosen3, f)
        print (infilename)
        # getfilename
        oldbase = os.path.splitext(f)
        print(oldbase)
        # Newname
        newname = directoryChosen3 + '/' + oldbase[0] + ".xlsx"
        print(newname)
        # function to rename files
        os.rename(infilename, newname)