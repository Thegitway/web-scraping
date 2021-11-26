from flask import Flask, render_template, request
import json
app= Flask(__name__)
filename = 'covid16112020.json'
@app.route('/',methods=['GET'])
def index():
    return(render_template('index.html'))
@app.route('/',methods=['POST'])
def result():
    country1 = request.form['country1']
    country2 = request.form['country2']
    country3 = request.form['country3']

    casesCountry1 = getCases(country1)
    casesCountry2 = getCases(country2)
    casesCountry3 = getCases(country3)
    print(casesCountry1)

    deathsCountry1 = getDeaths(country1)
    deathsCountry2 = getDeaths(country2)
    deathsCountry3 = getDeaths(country3)
    print(deathsCountry1)

    dateLabels = getDates(country1)
    print(dateLabels)

    return(render_template('index.html',country1=country1,country2=country2,country3=country3,casesCountry1=casesCountry1,CasesCountry2=casesCountry2,casesCountry3=casesCountry3,dateLabels=dateLabels))
def getCases(country):
    with open(filename) as json_file:
        jsonData=json.load(json_file)
        caseList=[]
        for record in jsonData['records']:
            if record['countryterritoryCode']==country:
                caseList.append(int(record['cases']))
    return (list(reversed(caseList)))
def getDeaths(country):
    with open(filename) as json_file:
        jsonData=json.load(json_file)
        deathsList=[]
        for record in jsonData['records']:
            if record['countryterritoryCode'] == country:
                deathsList.append(int(record['deaths']))
        return (list(reversed(deathsList)))

def getDates(country):
    with open(filename) as json_file:
        jsonData=json.load(json_file)
        dateList=[]
        for record in jsonData['records']:
            if record['countryterritoryCode'] == country:
                dateList.append(record['dateRep'])
        return (list(reversed(dateList)))
if __name__ == '__main__':
    app.run(host='localhost',debug=True)