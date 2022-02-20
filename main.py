import requests

#http://api.wolframalpha.com/v2/query?appid=YGV9XJ-RH825P558W&input=solve+3x-7%3D11&podstate=Result__Step-by-step+solution&format=plaintext&includepodid=Result&output=json

def formatEq(eq):
    return eq.replace('=', '%3D')
eq = "3x+5%3D11"
webInfo = requests.get("http://api.wolframalpha.com/v2/query?appid=YGV9XJ-RH825P558W&input=solve+3x-7%3D11&podstate=Result__Step-by-step+solution&format=plaintext&includepodid=Result&output=json")
#print(webInfo.status_code) 200 if works 410 if not
dictInfo = webInfo.json()

print('\n'+dictInfo['queryresult']['pods'][0]['subpods'][0]['plaintext'])
print('\n'+dictInfo['queryresult'][ 'pods'][0]['subpods'][1]['plaintext'])


print(dictInfo)
def getAnswer(problem, apiData):
   return apiData['queryresult']['pods'][0]['subpods'][0]['plaintext']

def getSolution(problem, apiData):
    return apiData['queryresult'][ 'pods'][0]['subpods'][1]['plaintext'])