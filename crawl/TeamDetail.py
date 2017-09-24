import requests
import json
from os.path import isfile

url = 'https://3ds.pokemon-gl.com/frontendApi/battleTeam/getBattleTeamDetail'

headers = {
    'Accept-Encoding' : 'gzip, deflate, compress, br',
    'Referer' : 'https://3ds.pokemon-gl.com/rentalteam/',
    'X-Requested-With' : 'XMLHttpRequest'
    }

def getPostData(teamCd):
    requestDataList = {
        'languageId' : '2',
        'battleTeamCd' : teamCd,
        'timeStamp' : '1504881335388'
    }
    return requestDataList

def getRawJSON(teamCd):
    res = requests.post(url, data=getPostData(teamCd), headers=headers)
    return json.loads(res.text)

def checkFile(fpath='web/js/data-team.js'):
    if isfile(fpath):
        pass
    else:
        with open(fpath, 'w') as openfile:
            openfile.write('var td=[];\n')

def retrieveCurrentTeamCdFromFile(fpath="web/js/data-team.js"):
    results = []
    checkFile()
    with open(fpath) as rfile:
        rline = rfile.readline()
        while(rline):
            teamCd = rline[rline.find('[')+1:rline.find(']')].replace('"','');
            if len(teamCd) > 10 and len(teamCd) < 15:
                results.append(teamCd)
            rline = rfile.readline()
    return results

def appendTeamDetailToFile(teamCd, fpath='web/js/data-team.js'):
    raw = getRawJSON(teamCd)
    checkFile(fpath)
    with open(fpath, 'a') as openfile:
        openfile.write('td["%s"]=' % teamCd)
        json.dump(raw, openfile)
        openfile.write(';\n')
    return raw

def appendBatchTeamDetailToFile(teamCds, fpath='web/js/data-team.js'):
    result = []
    IDCount = 1
    for teamCd in teamCds:
        print('fetching team[%i]: %s ...' % (IDCount, teamCd))
        raw = getRawJSON(teamCd)
        IDCount += 1
        result.append(raw)

    checkFile(fpath)
    with open(fpath,'a') as openfile:
        for i in range(len(result)):
            openfile.write('td["%s"]=' % teamCds[i])
            json.dump(result[i], openfile)
            openfile.write(';\n')
    return result

if __name__ == '__main__':
    pass
#r = getRawJSON('BT-D139-44CF')
