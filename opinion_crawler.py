import requests
from bs4 import BeautifulSoup
from datetime import datetime

import numpy as np
import pandas as pd

class CrawlWithCode:
    
    def __init__(self, code, BASE_URL='https://finance.naver.com/item/board.nhn?code='):
        """
        code: str/해당 주식의 종목 코드/ex.(삼성전자:'005930')
        BASE_URL: str/기본 URL 주소/구조변경 시 수정 필요 
        """
        self.code = code
        self.BASE_URL = BASE_URL
        self.date = []
        self.title = []
        self.opinion = []
        self.thumbs_up = []
        self.thumbs_down = []      
        
    def page_saver(self, page):
        """
        지정한 page 번호에 있는 게시글의 5가지 항목을 크롤링
        크롤링 항목(1): 작성일시
        크롤링 항목(2): 제목
        크롤링 항목(3): 의견
        크롤링 항목(4): 공감
        크롤링 항목(5): 비공감       
        """
        url = self.BASE_URL + self.code + "&page=" + str(page)
        html = requests.get(self.BASE_URL + self.code + "&page=%d" % page)
        soup = BeautifulSoup(html.text, 'lxml')
        
        dates = soup.select('#content > div.section.inner_sub > table.type2 > tbody > tr > td:nth-of-type(1) > span') # 날짜 가져오기
        titles = soup.select('#content > div.section.inner_sub > table.type2 > tbody > tr > td.title > a') # 제목 가져오기
        opinions = soup.select('#content > div.section.inner_sub > table.type2 > tbody > tr > td.tc > span') # 의견 가져오기
        thumbs_up = soup.select('#content > div.section.inner_sub > table.type2 > tbody > tr > td:nth-of-type(6) > strong') # 공감
        thumbs_down = soup.select('#content > div.section.inner_sub > table.type2 > tbody > tr > td:nth-of-type(7) > strong') # 비공감   


        date = [datetime.strptime(d.text.replace(".",""), '%Y%m%d %H:%M') for d in dates]
        title = [t.get("title") for t in titles]
        opinion = [o.text for o in opinions]
        up = [thumb_up.text for thumb_up in thumbs_up]
        down = [thumb_down.text for thumb_down in thumbs_down]
        

        self.date += date
        self.title += title
        self.opinion += opinion
        self.thumbs_up += up
        self.thumbs_down += down
        
    def toexcel(self, filename, PATH):
        """
        filename의 형식: example.xlsx에서 확장자 제거하고 example만 입력
        PATH 의 형식: "C:\\Users\\Username\\Dir\\"
        
        지정된 경로에 yyyymmdd_코드명.xlsx 파일 생성
        """
        filename = datetime.today().strftime("%Y%m%d_%H_%M_%S") +"_"+ filename
        PATH += "{}.xlsx".format(filename)
        data = pd.DataFrame({'작성일시':self.date, '의견':self.opinion, '제목': self.title, '공감': self.thumbs_up, '비공감': self.thumbs_down} )
        data.to_excel(PATH, sheet_name = self.code, engine='xlsxwriter')
        
