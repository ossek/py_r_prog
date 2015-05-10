from sys import argv

def pollutantmean(directory,pollutant,ids = range(1,332)):
    vals = []
    for id in ids:
        vals.extend(pollutantValuesFromFile(directory,pollutant,id))
    return sum(vals)/len(vals)

def pollutantValuesFromFile(directory,pollutant,fileid):
    content = getContent(directory,fileid)
    return pollutantValues(content,pollutant)

def pollutantValues(content,pollutant):
    col = 1 if pollutant == "sulfate" else 2
    lines = str.splitlines(content)
    vals = []
    for line in lines:
        linevals = str.split(line,",")
        val = linevals[col]
        if str.upper(val).strip() != "NA":
            vals.append(float(val))
    return vals

def getContent(directory,fileid):
    filename = padFileid(fileid)
    fileStream = open(directory + '/' + filename)
    # should be "Date sulfate nitrate id"
    header = fileStream.readline()
    content = fileStream.read()
    return content

def padFileid(fileid):
    fileidstr = str(fileid)
    while len(str(fileidstr)) < 3:
        fileidstr = '0' + fileidstr
    return fileidstr + '.csv'

if __name__ == "__main__":
    print(pollutantmean(argv))
