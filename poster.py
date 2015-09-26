#!/usr/bin/env python

"""poster

Usage:
  poster <url> <post_data>
  poster <url> <post_data> -n <num>
  poster allows you to post to a url with certaiin post_data.
Examples:
  poster <url>
Options:
  -v --version      Print the version number
  -n --num_process  Number of processes
"""

from multiprocessing import Process
import requests
from docopt import docopt

__author__ = 'Daniel'

N = 100


class Poster(Process):
    def __init__(self, url, data=None):
        self.client = requests.session()
        self.common_headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip,deflate,sdch",
            "Accept-Language": "en-US,en;q=0.8,zh;q=0.6,zh-CN;q=0.4",
            "Cache-Control": "max-age=0",
            "Content-Type": "application/json",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36"
        }
        self.url = url
        self.data = data
        super(Poster, self).__init__()

    def post(self):
        response = self.client.post(self.url, json=self.data,
                                    headers=self.common_headers)
        return response

    def run(self):
        while True:
            response = self.post()
            print response.text


if __name__ == "__main__":
    options = docopt(__doc__, version='poster 0.0.1')
    url = options['<url>']
    data = options['<post_data>']
    n = N
    if options['--num_process']:
        n = int(options['<num>'])

    print "running with number of processes: %d" % n
    for i in xrange(n):
        Poster(url, data).start()
