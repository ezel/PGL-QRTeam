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

def getTeamInfoFromRaw(rawPage):
    rawInfoList = rawPage['battleTeamUseTrainerRankingInfo']
    # filter the info
    # no filter
    return rawInfoList

def getAllRankingInfo():
    page = 1
    raw = getRawJSON(page)
    results = []
    totalCount = raw['totalCount']
    while(raw['totalCount'] > 0):
        results.extend(getTeamInfoFromRaw(raw))
        page += 1
        totalCount += raw['totalCount']
        raw = getRawJSON(page)
    return results

def saveAllRankingInfoToFile(fpath="web/js/data.js"):
    raw = getAllRankingInfo()
    with open(fpath, 'a') as openfile:
        openfile.write('rl=')
        json.dump(raw, openfile)
        openfile.write(';\ntd=[];\n')
    return raw

def retrieveTeamCdFromFile(fpath="web/js/data.js"):
    with open(fpath) as rfile:
        rline = rfile.readline()
        try:
            info = json.loads(rline[3:-2])
        except json.decoder.JSONDecodeError:
            info = json.loads(rline[3:])
    return [i['battleTeam']['battleTeamCd'] for i in info]

if __name__ == '__main__':
    pass
#    r = getAllRankingInfo()
#    print(r, len(r))
