import os
import shutil
from scripts.autoUploader.settings import transcriptionErrors, writeError


def xlsxtocsv(directoryChosen):
    print "xlstocsv"
    print '   ===                    '
    print '      ===             '
    print '         ===          '
    print '            ===       '
    print '                      '
    print '                      '

    ##FUTURE replace with a dictionary, slow here
    for f in os.listdir(directoryChosen):

        if f.endswith(".xlsx"):
            if not f.startswith("processed"):
                if f.endswith(".asr.continu0us Transcriptionist=HJ.xlsx"):
                    newfile = f.replace(' Transcriptionist=HJ.xlsx', '.xlsx')

                    if newfile != f:

                        source = directoryChosen + '/' + f
                        dest2 = directoryChosen + '/' + newfile
                        os.rename(source, dest2)

                elif f.endswith(".asr.continous Transcriptionist=HJ.xlsx"):
                    newfile = f.replace('.asr.continous Transcriptionist=HJ.xlsx', '.asr.continuous.xlsx')

                    if newfile != f:
                        source = directoryChosen + '/' + f
                        dest2 = directoryChosen + '/' + newfile
                        os.rename(source, dest2)

                elif f.endswith(" Transcriptonist=HJ.xlsx"):
                    newfile = f.replace(' Transcriptonist=HJ.xlsx', '.xlsx')
                    print f
                    if newfile != f:
                        source = directoryChosen + '/' + f
                        dest2 = directoryChosen + '/' + newfile
                        os.rename(source, dest2)

                elif f.endswith(" Transcriptionis=HJ.csv"):
                    newfile = f.replace('Transcriptionis=HJ.csv', '.asr.continuous.xlsx')
                    print f
                    if newfile != f:
                        source = directoryChosen + '/' + f
                        dest2 = directoryChosen + '/' + newfile
                        os.rename(source, dest2)
                elif f.endswith(" Transccriptionist=HJ.csv"):
                    newfile = f.replace(' Transcriptionis=HJ.csv', 'Transcriptionist=HJ.csv')
                    print f
                    if newfile != f:
                        source = directoryChosen + '/' + f
                        dest2 = directoryChosen + '/' + newfile
                        os.rename(source, dest2)

                elif f.endswith(" Transcriptionist=HJ.xlsx"):
                        newfile = f.replace(' Transcriptionist=HJ.xlsx', '.xlsx')
                        print f
                        if newfile != f:
                            source = directoryChosen + '/' + f
                            dest2 = directoryChosen + '/' + newfile
                            os.rename(source, dest2)

                elif f.endswith(" Transcriptionist=HJ.xlsx"):

                        newfile = f.replace(' Transcriptionist=HJ.xlsx', '.xlsx')
                        print f
                        if newfile != f:
                            source = directoryChosen + '/' + f
                            dest2 = directoryChosen + '/' + newfile
                            os.rename(source, dest2)


                else:
                    #if no ending just continue
                    if len(f) == 41:
                        pass
                    else:
                        #filename Error
                        #Send to error folder if doesnt match these
                        writeError(errorStuff=f + " Invalid File name")
                        errorFolder = transcriptionErrors()
                        source = directoryChosen + '/' + f

                        #Copy command
                        shutil.copy2(source, errorFolder)

