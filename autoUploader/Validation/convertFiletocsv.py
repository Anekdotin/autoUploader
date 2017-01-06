import os
from scripts.autoUploader.settings import transcriptionErrors
import shutil


##This function converts xlsx to csv ..
# ***Requires xlsx2csv****

def convertcsv(directoryChosen):
    print "convertcsv"
    print '   ===                    '
    print '      ===             '
    print '         ===          '
    print '            ===       '
    print '                      '
    print '                      '
    for f in os.listdir(directoryChosen):
        if f.endswith(".xlsx"):
            if not f.startswith("processed"):
                try:
                    csvfile = str(f[:-5] + ".csv")
                    cmd = str('xlsx2csv ' + directoryChosen + '/' + f + ' ' + directoryChosen + '/' + csvfile )
                    os.system(cmd)

                except Exception:

                    # Copy to error folder

                    errorFolder = transcriptionErrors()
                    source = directoryChosen + '/' + f

                    # Copy command
                    shutil.copy2(source, errorFolder)


