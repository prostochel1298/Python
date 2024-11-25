import json, urllib.request, urllib.error,pandas as pd
class WordstatParser:
    def __init__(self, url, token, username):
        self.url = url
        self.token = token
        self.username = username
        
    def getClientUnits(self):
        data = {
            'method': 'GetClientsUnits',
            'token': self.token,
            'param': [self.username]
        }
        data = json.dumps(data, ensure_ascii=False).encode('utf8')
        request = urllib.request.urlopen(self.url,data) 
        response = json.loads(request.read().decode('utf8'))
        return response

    def createReport(self, phrases, geo = []):
        data = {
            'method': 'CreateNewWordstatReport',
            'token': self.token,
            'param': {
                'Phrases': phrases,
                'GeoID': geo
                }
        }
        data = json.dumps(data, ensure_ascii=False).encode('utf8')
        request = urllib.request.urlopen(self.url,data) 
        response = json.loads(request.read().decode('utf8'))
        return response
    
    def getReportList (self):
        data = {
            'method': 'GetWordstatReportList',
            'token': self.token    
        }
        data = json.dumps(data, ensure_ascii=False).encode('utf8')
        request = urllib.request.urlopen(self.url,data) 
        response = json.loads(request.read().decode('utf8'))
        return response
        
    def readReport (self, reportID):
        data = {
            'method': 'GetWordstatReport',
            'token': self.token,
            'param': reportID
        }
        data = json.dumps(data, ensure_ascii=False).encode('utf8')
        request = urllib.request.urlopen(self.url,data) 
        response = json.loads(request.read().decode('utf8'))
        return response
    
    def deleteReport (self, reportID):
        data = {
            'method': 'DeleteWordstatReport',
            'token': self.token,
            'param': reportID
        }
        data = json.dumps(data, ensure_ascii=False).encode('utf8')
        request = urllib.request.urlopen(self.url,data) 
        response = json.loads(request.read().decode('utf8'))
        return response

    #def save(self, report):
        #parse = []

        #for i in range(len(report['data'])):
            #for j in report['data'][0]['SearchedWith']:
                #parse.append(j)
                #break
       
       # df = pd.DataFrame(parse)  
        #df.to_excel(r"C:\Users\Admin\Documents\WS.xlsx",index = False)

        