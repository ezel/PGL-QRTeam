import requests
import json

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

def appendTeamDetailToFile(teamCd, fpath='web/js/data.js'):
    raw = getRawJSON(teamCd)
    with open(fpath, 'a') as openfile:
        openfile.write('td["%s"]=' % teamCd)
        json.dump(raw, openfile)
        openfile.write(';\n')
    return raw

def appendBatchTeamDetailToFile(teamCds, fpath='web/js/data.js'):
    result = []
    IDCount = 1
    for teamCd in teamCds:
        print('fetching team[%i]: %s ...\n' % (IDCount, teamCd))
        raw = getRawJSON(teamCd)
        IDCount += 1
        result.append(raw)

    with open(fpath,'a') as openfile:
        for i in range(len(result)):
            openfile.write('td["%s"]=' % teamCds[i])
            json.dump(result[i], openfile)
            openfile.write(';\n')
    return result

if __name__ == '__main__':
    pass
#r = getRawJSON('BT-D139-44CF')
