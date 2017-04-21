#!/usr/bin/env python3

import requests
import argparse
try:
    from termcolor import cprint
except ImportError:
    def cprint(text, color):
        print(text)

def main(args):
    url = "https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/{}".format(args.module)
    r = requests.get(url)
    if r.status_code == 200:
        cprint("YES", "green")
        print("{} is typed\n{}".format(args.module, url))
    elif r.status_code == 404:
        cprint("NO", "red")
        print("{} is NOT typed".format(args.module))
    else:
        cprint("UGH", "yellow")
        print("Hmmm... there was an issue: {}".format(url))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check if DefinitelyTyped has typings for an npm module')
    parser.add_argument('module', help='an npm module')
    main(parser.parse_args())
