import requests
import argparse
import time
import json
import StringIO
import gzip
import csv
import shutil
import codecs
import requests
import gzip
import six
from bs4 import BeautifulSoup
import io
from io import StringIO
from bs4 import BeautifulSoup
from six.moves import urllib
import sys

import requests
import argparse
import time
import json
import StringIO
import gzip
import csv
import codecs
#REFERENCE: https://github.com/automatingosint/osint_public/blob/master/commoncrawl/commoncrawler.py
reload(sys)
sys.setdefaultencoding('utf8')

# parse the command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--domain", required=True, help="The domain to target ie. cnn.com")
args = vars(ap.parse_args())

domain = args['domain']

# list of available indices
index_list = ["2019-01","2019-02","2019-03","2019-04"]


#
# Searches the Common Crawl Index for a domain.
#
def search_domain(domain):
    record_list = []

    print "[*] Trying target domain: %s" % domain

    for index in index_list:

        print "[*] Trying index %s" % index

        cc_url = "http://index.commoncrawl.org/CC-MAIN-%s-index?" % index
        cc_url += "url=%s&matchType=domain&output=json" % domain

        response = requests.get(cc_url)

        if response.status_code == 200:

            records = response.content.splitlines()

            for record in records:
                record_list.append(json.loads(record))

            print "[*] Added %d results." % len(records)

    print "[*] Found a total of %d hits." % len(record_list)

    return record_list


#
# Downloads a page from Common Crawl - adapted graciously from @Smerity - thanks man!
# https://gist.github.com/Smerity/56bc6f21a8adec920ebf
#
def download_page(record):
    offset, length = int(record['offset']), int(record['length'])
    offset_end = offset + length - 1

    # We'll get the file via HTTPS so we don't need to worry about S3 credentials
    # Getting the file on S3 is equivalent however - you can request a Range

    prefix = 'https://commoncrawl.s3.amazonaws.com/'

    # We can then use the Range header to ask for just this set of bytes
    resp = requests.get(prefix + record['filename'], headers={'Range': 'bytes={}-{}'.format(offset, offset_end)})
   
    # What we have now is just the WARC response, formatted:
    raw_data = StringIO.StringIO(resp.content)
    f = gzip.GzipFile(fileobj=raw_data)

    # What we have now is just the WARC response, formatted:
    data = f.read()

    soup = BeautifulSoup(data,'html.parser')
    f1 = open('output_file.txt','a')  
    a_tags = soup.find_all('a')
    for tag in a_tags:
        p_tags=soup.find_all('p') 
        for p_tag in p_tags:
            f1.write(str(p_tag))
    f1.close()
    # What we have now is just the WARC response, formatted:


record_list=search_domain(domain)
for record in record_list:
    download_page(record)
