import os

#This will change the file name of all files that have been processed
def renameExtension(directoryChosen):

    for f in os.listdir(directoryChosen):
        if not f.startswith("processed"):
            if f.endswith(".csv"):

                #getfilename + directory
                infilename = os.path.join(directoryChosen,f)
                # getfilename
                oldbase = os.path.splitext(f)
                # Newname
                newname = directoryChosen + '/' +'processed-' + oldbase[0] + ".csv"
                #function to rename files
                os.rename(infilename, newname)

            elif f.endswith(".xlsx"):
                # getfilename + directory
                infilename = os.path.join(directoryChosen, f)
                # getfilename
                oldbase = os.path.splitext(f)
                # Newname
                newname = directoryChosen + '/' + 'processed-' + oldbase[0] + ".xlsx"
                # function to rename files
                os.rename(infilename, newname)

            else:
                pass



