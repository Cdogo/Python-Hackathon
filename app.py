from flask import Flask, render_template, request
import random

import requests
from flask import Flask
#http://api.wolframalpha.com/v2/query?appid=YGV9XJ-RH825P558W&input=solve+3x-7%3D11&podstate=Result__Step-by-step+solution&format=plaintext&includepodid=Result&output=json

class ApiData:
    def __init__(self, equation):
        self.eq = equation

        self.apiData = requests.get(f"http://api.wolframalpha.com/v2/query?appid=YGV9XJ-RH825P558W&input=solve+{self.formatEq()}&podstate=Result__Step-by-step+solution&format=plaintext&includepodid=Result&output=json").json()
        
    def formatEq(self):
        return self.eq.replace('=', '%3D')

    def getAnswer(self):
        return self.apiData['queryresult']['pods'][0]['subpods'][0]['plaintext']

    def getSolution(self):
        return self.apiData['queryresult'][ 'pods'][0]['subpods'][1]['plaintext']

listQ = ["3x+5-12x=35", "3x+1=5","2x*5=10","6!","5=6x+2","10=7x+1"]
app = Flask(__name__)
ques = listQ[random.randrange(5)]
ApData = ApiData(ques)

@app.route('/')  
def index():
    return render_template("index.html") 

@app.route("/practice")
def practice():
    ques = listQ[random.randrange(5)]
    return render_template("practice.html", value = ApData.eq)

@app.route("/questions")
def questions():
    return render_template("questions.html")

@app.route("/study")
def study():
    return render_template("study.html")
    
if __name__ == "__main__":
    app.run()
#def getWebResponse():
 #   #userText = request.args.get("msg")








# eq = "3x+5%3D11"
# webInfo = requests.get("http://api.wolframalpha.com/v2/query?appid=YGV9XJ-RH825P558W&input=solve+3x-7%3D11&podstate=Result__Step-by-step+solution&format=plaintext&includepodid=Result&output=json")
# #print(webInfo.status_code) 200 if works 410 if not
# dictInfo = webInfo.json()

# print('\n'+dictInfo['queryresult']['pods'][0]['subpods'][0]['plaintext'])
# print('\n'+dictInfo['queryresult'][ 'pods'][0]['subpods'][1]['plaintext'])


# def getAnswer(problem, apiData):
#    return apiData['queryresult']['pods'][0]['subpods'][0]['plaintext']

# def getSolution(problem, apiData):
#     return apiData['queryresult'][ 'pods'][0]['subpods'][1]['plaintext']

