import datetime

#-----------------------------------
#TEST

proj = ('/Users/eeamesX/work/transcriptions/')

#datasets on proj : final dataset destination
folderlist = {'testFolder1':'ExpertSessionLogs_English',
              'testFolder2': 'ExpertSessionLogs_Spanish',
              'testFolder3': 'ExpertSessionLogs_German'
              }

#Where daily logs go
logpath = '/Users/eeamesX/work/scripts/autoUploader/Logs/'
txtfileName = str(datetime.date.today()) +".txt"



#PRODUCTION
#-----------------------------------


#proj = ''

# Location of where transcriptions land
#folderlist = {'UnspecifiedHardware_ExpertSessionLogs_English':'ExpertSessionLogs_English',
              #'FightClub_PVT2_Prod_English_Untranscribed': 'ExpertSessionLogs_English',
              #'FightClub_DVT4_German_Untranscribed': 'ExpertSessionLogs_English'
              #}

#logpath = ''

#-----------------------------------


#Comment that appears on LDS
comment='Autoingester - Added transcription Changed Dataset'




#This function returns destination of where the transcriptions with errors go
def transcriptionErrors():
    pathtofiles = '/Users/eeamesX/work/scripts/autoUploader/error/errorFiles'
    return pathtofiles

#The path to lds script
def ldsPath():
    abspathofDir = '/Users/eeamesX/work/ingestion/lds.py'
    return abspathofDir

# Error txt file
def writeError(errorStuff):
    with open(logpath + txtfileName, "a") as outputFile:
        outputFile.write(errorStuff+ '\n')


# Log file
def writeTxt(fileStuff):
    with open(logpath + txtfileName, "a") as outputFile:
        outputFile.write(fileStuff + '\n')
