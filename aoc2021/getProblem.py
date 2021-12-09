import argparse, sys

import requests
import re


if __name__ == '__main__':
    # Execute when the module is not initialized from an import statement.
    parser=argparse.ArgumentParser()

    parser.add_argument('--day', help='Do the bar option')
    args=parser.parse_args()
    day = int(args.day)


    url = 'https://adventofcode.com/2021/day/%s/input' % day
    print("LOADING %s" % url)
    cookies = dict(session='53616c7465645f5f28e3385d1ee5bcd41944f78a67d5adb5a429925ef83d0b03cf672306f92340ae07f692990ed20d87')
    response = requests.get(url, cookies = cookies)
    TEXT = response.text

    with open('inputs/DATA_%s.py' % day, 'w') as file:
        file.write(TEXT)
