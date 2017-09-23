import requests
import json

url = 'https://3ds.pokemon-gl.com/frontendApi/battleTeam/getBattleTeamUseTrainerRanking'
url_season = 'https://3ds.pokemon-gl.com/frontendApi/battleTeam/getBattleTeamSeasonRanking'

headers = {
    'Accept-Encoding': 'gzip, deflate, compress, br',
    'Referer': 'https://3ds.pokemon-gl.com/rentalteam/trainer/',
    'X-Requested-With': 'XMLHttpRequest'
    }

def getPostData(page=1, rankingType=1, seasonId=False):
    requestDataList = {
        'timezone' : 'Asia&Tokyo',
        'languageId' : '2',
        'battleType' : '2',
        'rankingType' : rankingType,  # 1:all, 2:season, 3:week, 4:day;
        'displayNumber' : '10',
        'page' : page,
        'timeStamp' : '1504881335388',
    }
    if (seasonId):
        requestDataList['seasonId'] = seasonId;
    #requestDataString = "&".join(requestDataList)
    return requestDataList

def getRawJSON(page=1, rankingType=1, seasonId=False):
    if seasonId:
        res = requests.post(url_season, data=getPostData(page, rankingType, seasonId), headers=headers)
    else:
        res = requests.post(url, data=getPostData(page, rankingType), headers=headers)
    return json.loads(res.text)

def getTeamInfoFromRaw(rawPage, rankingType=1, seasonId=False):
    rawInfoList = 0
    prefix_append = 0
    # set prefix
    if rankingType == 1:
        rawInfoList = rawPage['battleTeamUseTrainerRankingInfo']
        prefix_append = 'A.'
    elif rankingType == 2:
        rawInfoList = rawPage['battleTeamSeasonRankingInfo']
        prefix_append = 'S' + str(seasonId)[-1] + '.'
    elif rankingType == 3:
        rawInfoList = rawPage['battleTeamUseTrainerRankingInfo']
        prefix_append = 'W.'
    elif rankingType == 4:
        rawInfoList = rawPage['battleTeamUseTrainerRankingInfo']
        prefix_append = 'D.'

    # filter the info
    for item in rawInfoList:
        # add A/S/W/D on ranking
        item['ranking'] = prefix_append + str(item['ranking'])
    return rawInfoList

""" fetch raw data each page -> filter -> combine(extend) """
def getTotalRankingInfo(rankingType=1, seasonId=False):
    page = 1
    raw = getRawJSON(page, rankingType, seasonId)
    results = []
    totalCount = raw['totalCount']
    while(raw['totalCount'] > 0):
        results.extend(getTeamInfoFromRaw(raw, rankingType, seasonId))
        page += 1
        totalCount += raw['totalCount']
        raw = getRawJSON(page, rankingType, seasonId)
    return results

def getAllRankingInfoList():
    # fetch all info into a list
    all_info = []
    for i in range(1, 5):
        print('fetching ... %i/%i ...' %(i, 4) )
        info = 0
        if i == 2:
            # for season ranking , add season id (201-20x)
            for j in range(201, 207):
                print('fetching ... season %i ...' % j )
                info = getTotalRankingInfo(i, j)
                all_info.append(info)
        else:
            info = getTotalRankingInfo(i)
            all_info.append(info)
    return all_info

""" combine all info (a/s/w/d) to one raw """
def combineAllRankingInfo(infoLists):
    infos = infoLists.pop(0)
    # current teamCd
    teamCds = [t['battleTeam']['battleTeamCd'] for t in infos]
    for info in infoLists:
        # new teamCd to add
        newCds = [t['battleTeam']['battleTeamCd'] for t in info]
        for k in range(len(newCds)):
            if newCds[k] in teamCds:
                # find infos[k]
                idx = teamCds.index(newCds[k])
                # update ranking
                infos[idx]['ranking'] += ','+ info[k]['ranking']
                pass
            else:
                # append new team
                teamCds.append(newCds[k])
                infos.append(info[k])

    return infos

def saveAllRankingInfoToFile(fpath="web/js/data.js"):
    infoLists = getAllRankingInfoList()
    infos = combineAllRankingInfo(infoLists)
    with open(fpath, 'a') as openfile:
        openfile.write('rl=')
        json.dump(infos, openfile)
        openfile.write(';\ntd=[];\n')
    return infos

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
