from sys import argv
import csv

def pollutantmean(directory,pollutant,ids = range(1,332)):
    vals = []
    for id in ids:
        vals.extend(getPollutantValues(directory,id,pollutant))
    return sum(vals)/len(vals)

def getPollutantValues(directory,fileid,pollutant):
    filename = padFileid(fileid)
    vals = []
    # headers should be "Date sulfate nitrate id"
    with open(directory + '/' + filename,newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            val = row[pollutant]
            if str.upper(val).strip() != "NA":
                vals.append(float(val))
    return vals

def padFileid(fileid):
    fileidstr = str(fileid)
    while len(str(fileidstr)) < 3:
        fileidstr = '0' + fileidstr
    return fileidstr + '.csv'

if __name__ == "__main__":
    print(pollutantmean(argv))
