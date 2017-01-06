
##This script will search each file for errors.
from scripts.autoUploader.settings import transcriptionErrors, writeError, writeTxt
import csv, os, sys, re
import shutil

postProcTags = ["startTime", "endTime", "transcription", "signalQuality"]
validSignalQualities = [
    "bike noise",
    "footfalls",
    "breathing noise",
    "user noise",
    "construction noise",
    "street noise",
    "train or subway noise",
    "plane overhead",
    "device noise",
    "other noise",
    "other speaker",
    "other language",
    "trail/forest noise",
    "ocean waves/water",
    "wind",
    "no speech",
    "no audio",
    "speech garbled",
    "off task",
    ""]


def makeCamelCase(someString):
    wordRE = re.compile(r"[A-Z]?[^A-Z\s]*")
    allWords = wordRE.findall(someString)
    for i, word in enumerate(allWords):
        allWords[i] = word.split()
    allWords = [word[0] for word in allWords if len(word) > 0]
    for i, word in enumerate(allWords):
        word = list(word)
        word = map(str.lower, word)
        if i > 0:
            word[0] = word[0].upper()
        allWords[i] = "".join(word)
    allWords = "".join(allWords)
    return allWords

def normalize(prompt):
    # get rid of noises
    prompt = re.sub(r'{(?:int|intw|spkb|fil|spk|sta)}', '', prompt)
    # get rid of unclear utterances
    #prompt = re.sub(r'{[^}]*}','', prompt)
    prompt = re.sub(r'[{}]','', prompt)
    # get rid of partial words, false starts
    prompt = re.sub(r'\([^)]*\)','', prompt)
    # compress all spaces to one space
    prompt = re.sub(r'\s+',' ', prompt)
    # remove split marker
    prompt = re.sub(r'\$','', prompt)
    # remove cutoff marker
    prompt = re.sub(r'\|','', prompt)
    # remove commas
    prompt = re.sub(r',','', prompt)
    # lowercase all characters
    prompt = prompt.lower()
    # normalize 'ok' to 'okay'
    prompt = re.sub(r'\bok\b', 'okay', prompt)
    # normalize fightclub to fight club
    prompt = re.sub(r'\bfightclub\b', 'fight club', prompt)
    prompt = re.sub(r'\bgps\b', '_g _p _s', prompt)
    prompt = re.sub(r'\brpm\b', '_r _p _m', prompt)

    # remove commas
    #prompt = re.sub(r'\,', '', prompt)
    prompt = re.sub(r'[!?\.;]', ' ', prompt)
    prompt = re.sub(r'\ba t\b', '_a _t', prompt)
    # remove leading and trailing whitespace, return only nonempty responses
    prompt = prompt.strip()
    return prompt

def checkHeaders(header):

    if header != postProcTags:
        camelCasedHeader = map(makeCamelCase, header)
        extraColumns = set(camelCasedHeader) - set(postProcTags)
        if len(extraColumns) > 0:
            pass
            #sys.stderr.write("Warning - unrecognized column headers: \n\t" + "\t".join(map(str,extraColumns)) + "\n")
        if not set(postProcTags).issubset(set(camelCasedHeader)):
            sys.stderr.write("Error - Missing column header(s): \n\t" + "\t".join(map(str, set(postProcTags) - set(camelCasedHeader))) + "\n")
            sys.exit("Terminating...")

        #extraColumns = [(i+1, h) for i, h in enumerate(header) if makeCamelCase(h) not in postProcTags]
        #sys.stderr.write("Invalid column headers: \n\t" + "\n\t".join(map(str,extraColumns)) + "\n")

def checkSignalQualities(signalQuality, lineNumber, csvFilename, directoryChosen):

    signalQualities = re.split(';|,', signalQuality)

    signalQualities = map(normalize, signalQualities)
    for signalQuality in signalQualities:
        if signalQuality not in validSignalQualities:
            print csvFilename
            print "Invalid signal quality: " + signalQuality + " on line " + str(lineNumber + 2)

            # Copy to error folder
            head, csvF = os.path.split(csvFilename)
            writeError(errorStuff=csvF+ " Invalid signal quality: " + signalQuality + " on line " + str(lineNumber + 2))
            errorFolder = transcriptionErrors()
            source =  csvFilename


            # Copy command
            shutil.copy2(source, errorFolder)

def checkSignalQualitiesofSpeech(signalQuality, lineNumber, csvFilename, directoryChosen):

    signalQualities = re.split(';|,', signalQuality)

    signalQualities = map(normalize, signalQualities)
    for signalQuality in signalQualities:
        if signalQuality == "no speech":
            #investigate if it should be no audio
            with open(csvFilename, 'rU') as csvFile:
                reader = csv.DictReader(csvFile)
                header = reader.fieldnames
                newHeaders = map(makeCamelCase, header)
                reader.fieldnames = newHeaders
                checkHeaders(header)
                startTimes, endTimes = [], []

                for line in reader:
                    if any(line[h] for h in newHeaders):  # skip empty lines
                        startTimes.append(float(line['startTime']))
                        endTimes.append(float(line['endTime']))


                if startTimes == endTimes:
                    print csvFilename
                    print 'No Speech instead of no audio!'

                    # Copy to error folder
                    head, csvF = os.path.split(csvFilename)
                    writeError(errorStuff=csvF + ' No Speech instead of no audio!')
                    errorFolder = transcriptionErrors()
                    source = csvFilename

                    # Copy command
                    shutil.copy2(source, errorFolder)

        elif signalQuality == "no audio":

            # investigate if it should be no audio
            with open(csvFilename, 'rU') as csvFile:
                reader = csv.DictReader(csvFile)
                header = reader.fieldnames
                newHeaders = map(makeCamelCase, header)
                reader.fieldnames = newHeaders
                checkHeaders(header)
                startTimes, endTimes = [], []

                for line in reader:
                    if any(line[h] for h in newHeaders):  # skip empty lines
                        startTimes.append(float(line['startTime']))
                        endTimes.append(float(line['endTime']))

                if startTimes != endTimes:
                    print csvFilename
                    print 'No audio instead of no speech!'

                    # Copy to error folder
                    head, csvF = os.path.split(csvFilename)
                    writeError(errorStuff=csvF+ ' No audio instead of no speech!')
                    errorFolder = transcriptionErrors()
                    source =  csvFilename


                    shutil.copy2(source, errorFolder)



def checkMarkers(transcription):
    markers = re.compile(r'{[^(?:int|intw|spkb|fil|spk|sta)]}')
    invalidMarkers = markers.findall(transcription)
    for m in invalidMarkers:
        print m, 'hi'

def checkBalancedBraces(transcription):
    openParens = 0
    for i, c in enumerate(transcription):
        if c == '{':
            openParens += 1
            print "Open Params"
        elif c == '}':
            openParens -= 1
            print "Open Params"
        elif c in ['()[]<>']:
            return -1

    return openParens

def findNonAscendingElement(l, secondList=None):
    if secondList is None:
        secondList = l
    nonAscendings = []
    for i, e in enumerate(l):
        if i == len(l)-1:
            break
        if e >= secondList[i+1]:
            nonAscendings.append(i+2)
    return nonAscendings

def findNonAscendingPairs(l, secondList):
    nonAscendings = []
    for i, e in enumerate(l):
        if e >= secondList[i]:
            nonAscendings.append(i+2)
    return nonAscendings

def findSuperLongPairs(startTimes, endTimes):
    superLongs = []
    for i, e in enumerate(startTimes):
        if (endTimes[i] - e) > 120:
            superLongs.append(i+2)
    return superLongs

def checkTimestamps(csvFilename, directoryChosen):
    # make sure there are no overlapping timestamps
    # and that everything is increasing


    with open(csvFilename, 'rU') as csvFile:
        try:
            reader = csv.DictReader(csvFile)
            header = reader.fieldnames
            newHeaders = map(makeCamelCase, header)
            reader.fieldnames = newHeaders
            checkHeaders(header)
            startTimes, endTimes = [], []
            for line in reader:
                if any(line[h] for h in newHeaders): # skip empty lines
                    startTimes.append(float(line['startTime']))
                    endTimes.append(float(line['endTime']))
            # check ascension
            nonAscendings = findNonAscendingElement(startTimes)
            if nonAscendings != []: # found non ascending elements
                print " "
                head, csvF = os.path.split(csvFilename)
                print csvF
                print "Start times are not ascending around lines " + str(nonAscendings)

                # Copy to error folder
                writeError(errorStuff=csvFilename + " Start times are not ascending around lines " + str(nonAscendings))
                errorFolder = transcriptionErrors()
                source = csvFilename

                # Copy command
                shutil.copy2(source, errorFolder)
            endNonAscendings = findNonAscendingElement(endTimes)
            if endNonAscendings != []: # found non ascending elements
                print " "
                print csvFilename
                print "End times are not ascending around lines " + str(endNonAscendings)

                # Copy to error folder
                head, csvF = os.path.split(csvFilename)
                writeError(errorStuff=csvF + " End times are not ascending around lines " + str(endNonAscendings))
                errorFolder = transcriptionErrors()
                source =  csvFilename

                # Copy command
                shutil.copy2(source, errorFolder)

            # check overlap
            nonAscendings = findNonAscendingElement(endTimes, startTimes)
            if nonAscendings != []:
                print " "
                print csvFilename
                print "End times overlap with following start times around lines " + str(nonAscendings)

                # Copy to error folder
                head, csvF = os.path.split(csvFilename)
                writeError(errorStuff= csvF + " End times overlap with following start times around lines " + str(nonAscendings))
                errorFolder = transcriptionErrors()
                source = directoryChosen + '/' + csvFilename

                # Copy command
                shutil.copy2(source, errorFolder)
            nonAscendings = findNonAscendingPairs(startTimes, endTimes)
            nonAscendings = list(set(nonAscendings) - set(endNonAscendings))
            if nonAscendings != []:
                print " "
                print csvFilename
                print "Start times not preceding end times on lines " + str(nonAscendings)

                # Copy to error folder
                head, csvF = os.path.split(csvFilename)
                writeError(errorStuff= csvF + " Start times not preceding end times on lines " + str(nonAscendings))
                errorFolder = transcriptionErrors()
                source = csvFilename

                # Copy command
                shutil.copy2(source, errorFolder)
        except Exception as e:
            print str(e)
            head, csvF = os.path.split(csvFilename)
            print csvFilename
            writeError(errorStuff=csvF + str(e))



def main(directoryChosen):
    for csvF in os.listdir(directoryChosen):

        if csvF.endswith("csv"):
            if not csvF.startswith("processed"):

                csvFilename = directoryChosen + '/' + csvF

                checkTimestamps(csvFilename, directoryChosen)

                with open(csvFilename, 'rU') as csvFile:
                    reader = csv.DictReader(csvFile)
                    header = reader.fieldnames
                    newHeaders = map(makeCamelCase, header)
                    reader.fieldnames = newHeaders

                    for lineNumber, line in enumerate(reader):

                        checkSignalQualities(line['signalQuality'], lineNumber, csvFilename, directoryChosen)
                        checkSignalQualitiesofSpeech(line['signalQuality'], lineNumber, csvFilename, directoryChosen)



