# naverfinance_opinion_crawler
네이버 금융 종목토론실 게시글 크롤링

### 1. 사용법:
```
python main.py [args]
[args] --code CODE --DIR DIRECTORY --maxpage MAXPAGE --company_name COMPANY_NAME

```

- args 부분의 `CODE` `DIRECTORY` `MAXPAGE` `COMPANY_NAME`을 자신의 데이터에 맞게 수정하여 입력

- `code` 크롤링하고자 하는 대상 주식의 종목코드(ex. 삼성전자 -> 005930)

- `DIR` 저장하고자 하는 폴더(단, 마지막에 \\\를 꼭 붙여준다)

- `MAXPAGE` 1페이지부터 시작하여 크롤링할 마지막 페이지

- `COMPANY_NAME` 엑셀파일명에 들어갈 회사 이름

### 2. 사용 예시:
```
python main.py --code 005930 --DIR C:\\Users\\Username\\Dir1\\ --maxpage 100 --company_name SamsungElectronics

```
### 3. 실행 결과:
```
20190422_23_40_53_SamsungElectronics.xlsx
```
- `C:\\Users\\Username\\Dir1\\yyyymmdd_hh_mm_ss_COMPANY_NAME.xlsx` 해당 경로에 엑셀파일 생성됨

### 4. 추가 설치해야 할 패키지:
- BeautifulSoup, Requests
```
pip install beautifulsoup4
pip install requests
```
- 엑셀 파일 저장엔진
```
pip install xlsxwriter
```
