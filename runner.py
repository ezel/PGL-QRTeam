import sys
import os
from crawl import RankingList as rl
from crawl import TeamDetail as td

def help():
    content = "The main script to download or clean the QR team data from PGL site.\n" + \
              "\tdownload\t download and save team data.\n" + \
              "\t        \t RANGE: rank|detail|all .\n" +\
              "\tclean   \t clean all the old data.\n" + \
              "\traw     \t raw test data from PGL site,\n" + \
              "\t        \t TYPE: rpage|team  ARGs: page/teamCd.\n" +\
              "\t-? -h   \t this help."
    print(content)
    return

def error(msg):
    print("Error: ")
    print(msg)
    return

def download_detail_from_rankfile(fpath):
    teamCds = rl.retrieveTeamCdFromFile(fpath)
    td.appendBatchTeamDetailToFile(teamCds)
    pass

def clean():
    try:
        os.remove('web/js/data.js')
        print('data file cleaned.')
    except OSError:
        print('no data file!')

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        help()
    elif sys.argv[1] == 'raw':
        if len(sys.argv) <= 3:
            error('usage: raw rpage|team ARGs')
        elif sys.argv[2] == 'rpage':
            print(rl.getRawJSON(sys.argv[3]))
        elif sys.argv[2] == 'team':
            print(td.getRawJSON(sys.argv[3]))
        else:
            error('usage: raw rpage|team ARGs')
    elif sys.argv[1] == 'download':
        if len(sys.argv) == 2 or sys.argv[2] == 'all':
            clean()
            rl.saveAllRankingInfoToFile()
            download_detail_from_rankfile('web/js/data.js')
        elif sys.argv[2] == 'rank':
            rl.saveAllRankingInfoToFile()
        elif sys.argv[2] == 'detail':
            # read ranklist
            fpath = 'web/js/data.js'
            download_detail_from_rankfile(fpath)
        else:
            error('usage: download rank|detail|all')
        pass
    elif sys.argv[1] == 'clean':
        clean()
    else:
        help()
