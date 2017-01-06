import subprocess
import os
from scripts.autoUploader.settings import ldsPath, writeTxt, writeError

lds = ldsPath()

#UPLOAD AND MOVE BASED OFF ID (ADVANCED)
def UploadTranscriptReplacebyID(directoryChosen, comment, sourceDataset, destinationDataset):

    for fileName in os.listdir(directoryChosen):
        if fileName.endswith(".csv"):

                #THIS cmd will upload and move source -> destination
                cmd = [
                       "python " + lds +
                       " audio put -i " +
                       str(fileName[:-4]) +' -t ' +
                       str(directoryChosen) + '/' +
                       str(fileName) +
                       ' -c ' + ' "' + comment + '"  -s ' +
                       sourceDataset + ' -d '
                       + destinationDataset
                       ]
                try:
                    # Executes command
                    proc= subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,)
                    # Turns output into a variable for logging possibly ..
                    upload = proc.communicate()[0]

                    ##write files uploaded to lds
                    writeTxt(fileStuff=fileName)

                except Exception as e:
                    print str(e)
                    writeError(errorStuff=fileName + " " + str(e))
