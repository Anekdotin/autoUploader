import os

from scripts.autoUploader.Validation import convertFiletocsv, convertFilenames, checkTranscriptions
from scripts.autoUploader.uploadandRemove import upload
from scripts.autoUploader.finishChecklist import changeExtensioncsv
from scripts.autoUploader.settings import folderlist, proj, comment, writeTxt
from scripts.autoUploader.emailReport import gotMail


##This program will crawl Int-Corpora, find new transcriptions and upload them to LDS
##Phase 1 = Validation
# 1. convertFileNames will look for odd filename endings
# 2. convertFiletocsv will convert an xlsx to a csv
# 3. checkTranscriptions will use a validation script to check transcriptions for
#    signalQuality, times, and various other issues

##Phase 2 = uploadandRemove
# 1. upload will use Virginians script to upload files to lds, and remove
#  the filename from the old dataset



##Phase 3 = finishChecklist
# 1. changeExtension will go into proj and add an ending to the transcriptions



##Phase 4 = Email
#1. sendmail will send an email out based off what was processed and errors recieved





#Program could be faster by 1 loop for everything..good idea or bad idea..handling errors?


def Main():
    #python 2.x
    for f, value in folderlist.iteritems():
        directoryChosen = proj + f


        print "        "
        print directoryChosen
        print value
        print f
        print "        "
        print "        "

        # Phase1:1
        convertFilenames.xlsxtocsv(directoryChosen=directoryChosen)
        # Phase1:2
        convertFiletocsv.convertcsv(directoryChosen=directoryChosen)
        # Phase1:3
        checkTranscriptions.main(directoryChosen=directoryChosen)



        # Phase2:1
        #upload.UploadTranscriptReplacebyID(directoryChosen=directoryChosen,
                                           #comment=comment,
                                           #sourceDataset=f,
                                           #destinationDataset=value)



        # Phase3:1
        changeExtensioncsv.renameExtension(directoryChosen=directoryChosen)

        # Phase4:1


        #gotMail.send_mail(
                         #send_from="edwinx.eames@intel.com",
                         #send_to=["edwinx.eames@intel.com"],
                         #subject="LDS Upload Announcement - " + gotMail.yesterday(),
                         #text=gotMail.Message(),
                         #)

##TODO Seperate logs by dataset
##TODO find actual names datasets run real trial
##TODO Put on ubuntu box
##TODO setup email / test it
##TODO clean up code
##TODO Jenkins

Main()


