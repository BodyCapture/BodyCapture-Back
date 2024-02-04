import pandas as pd
import requests
import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

# 바디프로필 URL
'''
BP_Kyonggi_URL = 'https://map.naver.com/p/search/%EA%B2%BD%EA%B8%B0%EB%8F%84%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84%20?c=15.00,0,0,0,dh'
BP_Gangwon_URL = 'https://map.naver.com/p/search/%EA%B0%95%EC%9B%90%EB%8F%84%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84%20?c=15.00,0,0,0,dh'
BP_Chungcheong_N_URL = 'https://map.naver.com/p/search/%EC%B6%A9%EC%B2%AD%EB%B6%81%EB%8F%84%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84?c=15.00,0,0,0,dh'
BP_Chungcheong_S_URL = 'https://map.naver.com/p/search/%EC%B6%A9%EC%B2%AD%EB%82%A8%EB%8F%84%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84?c=15.00,0,0,0,dh'
BP_Gyeongsang_N_URL = 'https://map.naver.com/p/search/%EA%B2%BD%EC%83%81%EB%B6%81%EB%8F%84%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84?c=15.00,0,0,0,dh'
BP_Gyeongsang_S_URL = 'https://map.naver.com/p/search/%EA%B2%BD%EC%83%81%EB%82%A8%EB%8F%84%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84?c=15.00,0,0,0,dh'
BP_Jeolla_N_URL = 'https://map.naver.com/p/search/%EC%A0%84%EB%9D%BC%EB%B6%81%EB%8F%84%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84?c=15.00,0,0,0,dh'
BP_Jeolla_S_URL = 'https://map.naver.com/p/search/%EC%A0%84%EB%9D%BC%EB%82%A8%EB%8F%84%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84?c=15.00,0,0,0,dh'
BP_Seoul_URL = 'https://map.naver.com/p/search/%EC%84%9C%EC%9A%B8%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84?c=15.00,0,0,0,dh'
BP_Incheon_URL = 'https://map.naver.com/p/search/%EC%9D%B8%EC%B2%9C%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84?c=15.00,0,0,0,dh' 
BP_Daejeon_URL = 'https://map.naver.com/p/search/%EB%8C%80%EC%A0%84%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84?c=15.00,0,0,0,dh'
BP_Daegu_URL = 'https://map.naver.com/p/search/%EB%8C%80%EA%B5%AC%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84?c=15.00,0,0,0,dh'
BP_Busan_URL = 'https://map.naver.com/p/search/%EB%B6%80%EC%82%B0%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84?c=15.00,0,0,0,dh'
BP_Ulsan_URL = 'https://map.naver.com/p/search/%EC%9A%B8%EC%82%B0%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84?c=15.00,0,0,0,dh'
BP_Gwangju_URL = 'https://map.naver.com/p/search/%EA%B4%91%EC%A3%BC%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84?c=15.00,0,0,0,dh'
BP_Jeju_URL = 'https://map.naver.com/p/search/%EC%A0%9C%EC%A3%BC%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84?c=15.00,0,0,0,dh'
'''

# URL list
# BP_URL_list = [BP_Kyonggi_URL, BP_Gangwon_URL, BP_Chungcheong_N_URL, BP_Chungcheong_S_URL, BP_Gyeongsang_N_URL, BP_Gyeongsang_S_URL
#            , BP_Jeolla_N_URL, BP_Jeolla_S_URL, BP_Seoul_URL, BP_Incheon_URL, BP_Daejeon_URL, BP_Daegu_URL, BP_Busan_URL, BP_Ulsan_URL,
#            BP_Gwangju_URL, BP_Jeju_URL]

# URL dict
BP_URL_dict = {
    "Kyonggi": 'https://map.naver.com/p/search/%EA%B2%BD%EA%B8%B0%EB%8F%84%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84%20?c=15.00,0,0,0,dh',
    "Gangwon": 'https://map.naver.com/p/search/%EA%B0%95%EC%9B%90%EB%8F%84%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84%20?c=15.00,0,0,0,dh',
    "Chungcheong_N": 'https://map.naver.com/p/search/%EC%B6%A9%EC%B2%AD%EB%B6%81%EB%8F%84%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84?c=15.00,0,0,0,dh',
    "Chungcheong_S": 'https://map.naver.com/p/search/%EC%B6%A9%EC%B2%AD%EB%82%A8%EB%8F%84%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84?c=15.00,0,0,0,dh',
    "Gyeongsang_N": 'https://map.naver.com/p/search/%EA%B2%BD%EC%83%81%EB%B6%81%EB%8F%84%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84?c=15.00,0,0,0,dh',
    "Gyeongsang_S": 'https://map.naver.com/p/search/%EA%B2%BD%EC%83%81%EB%82%A8%EB%8F%84%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84?c=15.00,0,0,0,dh',
    "Jeolla_N": 'https://map.naver.com/p/search/%EC%A0%84%EB%9D%BC%EB%B6%81%EB%8F%84%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84?c=15.00,0,0,0,dh',
    "Jeolla_S": 'https://map.naver.com/p/search/%EC%A0%84%EB%9D%BC%EB%82%A8%EB%8F%84%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84?c=15.00,0,0,0,dh',
    "Seoul": 'https://map.naver.com/p/search/%EC%84%9C%EC%9A%B8%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84?c=15.00,0,0,0,dh',
    "Incheon": 'https://map.naver.com/p/search/%EC%9D%B8%EC%B2%9C%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84?c=15.00,0,0,0,dh',
    "Daejeon": 'https://map.naver.com/p/search/%EB%8C%80%EC%A0%84%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84?c=15.00,0,0,0,dh',
    "Daegu": 'https://map.naver.com/p/search/%EB%8C%80%EA%B5%AC%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84?c=15.00,0,0,0,dh',
    "Busan": 'https://map.naver.com/p/search/%EB%B6%80%EC%82%B0%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84?c=15.00,0,0,0,dh',
    "Ulsan": 'https://map.naver.com/p/search/%EC%9A%B8%EC%82%B0%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84?c=15.00,0,0,0,dh',
    "Gwangju": 'https://map.naver.com/p/search/%EA%B4%91%EC%A3%BC%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84?c=15.00,0,0,0,dh',
    "Jeju": 'https://map.naver.com/p/search/%EC%A0%9C%EC%A3%BC%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84?c=15.00,0,0,0,dh'
}

# 지역분류 region = 만들기###
# 지역분류는 데이터프레임 만들고 나서 합치는걸로 

body_profile_store = pd.DataFrame(columns = ['상호명', '주소'])

def body_profile_info(name, addr, link) :
    value = pd.DataFrame({'상호명' : [name],
                        '주소' : [addr],
                        '링크' : [link]})
    return value
######################################
# 스크래핑
######################################

######################################
# 다음 페이지로 이동
######################################


def next_page(url) :
  global body_profile_store
  
  driver = webdriver.Chrome()
  driver.get(url)


  while True :
    # 현재 페이지 높이 = last_height
    last_height = driver.execute_script('return document.body.scrollHeight')
    
    while True :
      # 스크롤 끝까지 내리기
      driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
      time.sleep(3)
      # 스크롤 내린 후 페이지 높이 = new_height
      new_height = driver.execute_script('return document.body.scrollHeight')
      
      if new_height == last_height :
        break
      
      last_height = new_height
      
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    store_data = []

    elements = soup.find('div', class_='Ryr1F').find_all('li')
    for i in elements :
      # 상세 정보 버튼 클릭
      xpath = "//div[@class='qbGlu']//svg[@class='Y2sSu']"
      detail_button = driver.find_element(By.XPATH, xpath)  
      detail_button.click()
      
      name = i.find('span', class_='YwYLL').get_text()  # 상호명
      addr = i.find('div', class_='zZf01')[0].get_text() # 주소
      # link = i.find()['href']  # 링크
      store_data.append(i.get_text({'상호명' : name,
                                    '주소' : addr}))
      # 상세 정보 접기
      detail_button.click()
      
    body_profile_store = body_profile_store.append(store_data, ignore_index=True)
  
    # 다음 페이지로 이동
    try :
      next_page_link = driver.find_element_by_xpath("(//div[@class='zRM9F']//a[@class='eURV2'])[2]")
      next_page_link.click()
      time.sleep(3) 
    except NoSuchElementException :
      break

# 브라우저 종료
  driver.quit()
  
k = 'https://map.naver.com/p/search/%EA%B2%BD%EA%B8%B0%EB%8F%84%20%EB%B0%94%EB%94%94%ED%94%84%EB%A1%9C%ED%95%84%20?c=15.00,0,0,0,dh'
next_page(k)

print(body_profile_store)