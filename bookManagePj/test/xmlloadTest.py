import requests
from bs4 import BeautifulSoup
''' 주식정보서비스 ''' 
url = 'http://api.seibro.or.kr/openapi/service/StockSvc/getShotnByMartN1'
queryParams =  '?'+ 'ServiceKey='+ '%2Bd99u7TP60Pq2dr2dl6iXfrQJntZ8%2BuGVC%2BUJLWiCo7xzLwA%2FJ6C52EFBW7AhRGkNrwI6kOLCAfJPV2MR4tKTA%3D%3D'\
            + '&pageNo='+ ''\
            +'&numOfRows='+ ''\
            +'&martTpcd='+ '12'
              
# 전부 다 필수값임!!!     
#  martTpcd :  11.유가증권시장, 12.코스닥, 13.K-OTC, 14.코넥스, 50.기타시장


''' 서울특별시교육청 공공도서관 소장도서정보 '''

# url = 'http://openapi-lib.sen.go.kr/openapi/service/lib/openApi'
# queryParams = '?'+'serviceKey=' +'NEl%2FjK7dxGeNFC87hNVJsnRQ358eEev7X8mCtiYcTFKlid8%2F6Q4sludx7mMD7WrccnFdmcon7Hj%2Btx4aBQ51Gw%3D%3D'\
#             +'&title='+'도둑'\
#             +'&manageCd='+'MB'\
#             +'&numOfRows='+'5'\
#             +'&pageNo='+'2'

## 요청변수(Request Parameter)
            
# title, manageCd : 필수항목

# manageCd: 
# MA    강남도서관/ MB    강동도서관/ MC    강서도서관/ MD    개포도서관/ ME    고덕평생학습관/
# MF    고척도서관/ MG    구로도서관/ MH    남산도서관/ MV    노원평생학습관/ MJ    도봉도서관/
# MK    동대문도서관/ ML    동작도서관/ MX    마포평생아현분관/ MM    마포평생학습관/ MP    서대문도서관/
# MW    송파도서관/ MN    양천도서관/ MQ    어린이도서관/ MR    영등포평생학습관/ MS    용산도서관/
# MT    정독도서관/ MU    종로도서관
# title을 빈 공란으로 두면 전체 데이타 조회 가능???
            
result = requests.get(url)
url = url + queryParams

result = requests.get(url)
 
bs_obj = BeautifulSoup(result.content, "html.parser")
print(bs_obj.prettify())