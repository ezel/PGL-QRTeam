import sys
import os
from crawl import RankingList as rl
from crawl import TeamDetail as td

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

def download_detail_from_rankfile(fpath):
    teamCds = rl.retrieveTeamCdFromFile(fpath)
    td.appendBatchTeamDetailToFile(teamCds, 'web/js/data-team.js')

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
            clean()
            rl.saveAllRankingInfoToFile()
            download_detail_from_rankfile('web/js/data-rank.js')
        elif sys.argv[2] == 'rank':
            rl.saveAllRankingInfoToFile()
        elif sys.argv[2] == 'detail':
            # read ranklist
            fpath = 'web/js/data-rank.js'
            download_detail_from_rankfile(fpath)
        else:
            error('usage: download rank|detail|all')
        pass
    elif sys.argv[1] == 'clean':
        clean()
    else:
        help()
