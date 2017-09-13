import requests
import json

url = 'https://3ds.pokemon-gl.com/frontendApi/battleTeam/getBattleTeamUseTrainerRanking'

headers = {
    'Accept-Encoding': 'gzip, deflate, compress, br',
    'Referer': 'https://3ds.pokemon-gl.com/rentalteam/trainer/',
    'X-Requested-With': 'XMLHttpRequest'
    }

def getPostData(page=1):
    requestDataList = {
        'timezone' : 'Asia&Tokyo',
        'languageId' : '2',
        'battleType' : '2',
        'rankingType' : '1',
        'displayNumber' : '10',
        'page' : page,
        'timeStamp' : '1504881335388',
    }
    #requestDataString = "&".join(requestDataList)
    return requestDataList

def getRawJSON(page=1):
    res = requests.post(url, data=getPostData(page), headers=headers)
    return json.loads(res.text)

def getAllRankingInfo():
    page = 1
    raw = getRawJSON(page)
    results = []
    while(raw['totalCount'] > 0):
        results.extend(raw['battleTeamUseTrainerRankingInfo'])
        page += 1
        raw = getRawJSON(page)
    return results

if __name__ == '__main__':
    pass
#    r = getAllRankingInfo()
#    print(r, len(r))
