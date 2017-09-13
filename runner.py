import sys

def help():
    content = "The main\n" + \
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

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        help()
    elif sys.argv[1] == 'raw':
        if len(sys.argv) <= 3:
            error('usage: raw rpage|team ARGs')
        elif sys.argv[2] == 'rpage':
            from crawl import RankingList as rl
            print(rl.getRawJSON(sys.argv[3]))
        elif sys.argv[2] == 'team':
            from crawl import TeamDetail as td
            print(td.getRawJSON(sys.argv[3]))
        else:
            error('usage: raw rpage|team ARGs')
    elif sys.argv[1] == 'download':
        if len(sys.argv) <= 3 or sys.argv[2] == 'all':
            pass
        elif sys.argv[2] == 'rank':
            pass
        elif sys.argv[2] == 'detail':
            # read ranklist

            pass
        else:
            error('usage: download rank|detail|all')
        pass
    elif sys.argv[1] == 'clean':
        pass
    else:
        help()
