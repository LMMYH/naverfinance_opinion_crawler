import os
import argparse
import requests
from bs4 import BeautifulSoup
from datetime import datetime

import pandas as pd
from opinion_crawler import Crawl_with_code

def argparser():
    p = argparse.ArgumentParser()
    p.add_argument('--code', required=True, type=str, help='크롤링 대상 종목코드')
    p.add_argument('--DIR', required=True, type=str, help='저장될 디렉토리')
    p.add_argument('--maxpage', required=True, type=int, help='크롤링할 최대 페이지수')
    p.add_argument('--company_name', required=True, type=str, help='저장될 파일명')


    config = p.parse_args()
    return config

def main():
    config = argparser()

    crawler = Crawl_with_code(config.code)
    for i in range(config.maxpage):
        crawler.page_saver(i)
        show_status =  "현재 {} 페이지 진행 중".format(i+1)
        print(show_status, end=len(show_status)*'\b', flush=True)
     
    crawler.toexcel(config.company_name, config.DIR)
    

if __name__ == '__main__':
    main()