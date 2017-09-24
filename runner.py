import sys
import os
from crawl import RankingList as rl, TeamDetail as td

def help():
    content = "The main script to download or clean the QR team data from PGL site.\n" + \
              "\tdownload\t download and save team data.\n" + \
              "\t        \t RANGE: rank|detail|all .\n" +\
              "\tclean   \t clean all the old data.\n" + \
              "\t-? -h   \t this help."
    print(content)
    return

def error(msg):
    print("Error: ")
    print(msg)
    return

def download_detail_by_rankfile(fpath, teampath='web/js/data-team.js'):
    want_teamCds = rl.retrieveTeamCdFromFile(fpath)
    old = td.retrieveCurrentTeamCdFromFile(teampath)
    new = [x for x in want_teamCds if x not in old ]
    td.appendBatchTeamDetailToFile(new, teampath)

def clean(fpathArray=['web/js/data-rank.js','web/js/data-team.js']):
    for fpath in fpathArray:
        try:
            os.remove(fpath)
            print('data file cleaned.')
        except OSError:
            pass

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        help()
    elif sys.argv[1] == 'download':
        if len(sys.argv) == 2 or sys.argv[2] == 'all':
            clean(['web/js/data-rank.js'])
            rl.saveAllRankingInfoToFile()
            download_detail_from_rankfile('web/js/data-rank.js')
        elif sys.argv[2] == 'rank':
            clean(['web/js/data-rank.js'])
            rl.saveAllRankingInfoToFile()
        elif sys.argv[2] == 'detail':
            # read ranklist
            fpath = 'web/js/data-rank.js'
            download_detail_by_rankfile(fpath)
        else:
            error('usage: download rank|detail|all')
        pass
    elif sys.argv[1] == 'clean':
        clean()
    else:
        help()
