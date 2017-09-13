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

if __name__ == '__main__':
    pass
#r = getRawJSON('BT-D139-44CF')
