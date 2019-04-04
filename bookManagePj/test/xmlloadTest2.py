from bs4 import BeautifulSoup
import requests

# 참고 링크: https://ha-ha09.tistory.com/14

url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.xml?key=430156241533f1d058c603178cc3ca0e"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser") # 파싱

# print(soup)
# print(soup.prettify()) # 이쁘게 보기

print(soup.find_all("moviecd")) # 모든 값을 리스트로 가져옴
print(soup.find("moviecd")) # 첫번째 값만 가져옴



'''
import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()

url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.xml?key=430156241533f1d058c603178cc3ca0e"
res = http.request('GET', url)
soup = BeautifulSoup(res.data)
print(soup)
'''

'''
url = 'http://api.seibro.or.kr/openapi/service/StockSvc/getShotnByMartN1'
queryParams =  '?'+ 'ServiceKey='+ '%2Bd99u7TP60Pq2dr2dl6iXfrQJntZ8%2BuGVC%2BUJLWiCo7xzLwA%2FJ6C52EFBW7AhRGkNrwI6kOLCAfJPV2MR4tKTA%3D%3D'\
            + '&pageNo='+ '1'\
            +'&numOfRows='+ '10'\
            +'&martTpcd='+ '11'

# url = 'http://openapi-lib.sen.go.kr/openapi/service/lib/openApi'
# queryParams = '?'+'serviceKey=' +'NEl%2FjK7dxGeNFC87hNVJsnRQ358eEev7X8mCtiYcTFKlid8%2F6Q4sludx7mMD7WrccnFdmcon7Hj%2Btx4aBQ51Gw%3D%3D'\
#             +'&title='+'도둑'\
#             +'&manageCd='+'MB'\
#             +'&numOfRows='+'5'\
#             +'&pageNo='+'2'
            

result = requests.get(url)
url = url + queryParams
tree = ET.parse(url)
root = tree.getroot()
print(root)

# result = requests.get(url)
# 
# bs_obj = BeautifulSoup(result.content, "html.parser")
# print(bs_obj)
'''