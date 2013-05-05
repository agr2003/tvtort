import csv
import json

__author__ = 'agr'

class Fields(object):
    def __init__(self, title, titleRus, a2, a3, numberCode):
        self.title = title
        self.titleRus = titleRus
        self.a2 = a2
        self.a3 = a3
        self.numberCode = numberCode


class Country(object):
    def __init__(self, model, pk, fields):
        self.model = model
        self.pk = pk
        self.fields = fields


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if not (isinstance(obj, Country) or isinstance(obj, Fields)):
            return super(MyEncoder, self).default(obj)
        return obj.__dict__

def csvToJson( inFile, outFile ):
    out = []

    with open(inFile, 'r') as csvFile:
        #Note this reads the first line as the keys we can add specific keys with:
        csvDict = csv.DictReader(csvFile, fieldnames=['title', 'titleRus', 'a2', 'a3', 'numberCode'], restkey=None,
                                 restval=None, )
        # csvDict = csv.DictReader(csvFile, restkey=None, restval=None, )
        counter = 0
        for row in csvDict:
            if row["title"] != "title" :
                fields = Fields(title=row["title"], titleRus=row["titleRus"], a2=row["a2"], a3=row["a3"],
                                numberCode=int(row["numberCode"]))
                c = Country(model="tvtort.SeriesCountry", pk=counter, fields=fields)
                counter += 1
                out.append(c)

    if out:
        with open(outFile, 'w') as jsonFile:
            jsonFile.write(json.dumps(out, cls=MyEncoder))
    else:
        print "Error creating csv dict!"


csvToJson('./countryCodes.csv', './countryCodes.json')




