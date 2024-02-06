import json
import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


url = 'https://map.naver.com/v5/search'
driver = webdriver.Chrome()  # 드라이버 경로
driver.get(url)
key_word = '경기도 바디프로필'  # 검색어

# css 찾을때 까지 10초대기
def time_wait(num, code):
    try:
        wait = WebDriverWait(driver, num).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, code)))
    except:
        print(code, '태그를 찾지 못하였습니다.')
        driver.quit()
    return wait

# frame 변경 메소드
def switch_frame(frame):
    driver.switch_to.default_content()  # frame 초기화
    driver.switch_to.frame(frame)  # frame 변경

# 페이지 다운
def page_down(num):
    body = driver.find_element(By.CSS_SELECTOR, 'body')
    body.click()
    for i in range(num):
        body.send_keys(Keys.PAGE_DOWN)

# css를 찾을때 까지 10초 대기
time_wait(10, 'div.input_box > input.input_search')

# 검색창 
search = driver.find_element(By.CSS_SELECTOR, 'div.input_box > input.input_search')
search.send_keys(key_word)  
search.send_keys(Keys.ENTER)  

sleep(1)

# frame 변경
switch_frame('searchIframe')
page_down(40)
sleep(3)

# 가게 리스트
store_list = driver.find_elements(By.CSS_SELECTOR, 'li.VLTHu')
# 페이지 리스트
next_btn = driver.find_elements(By.CSS_SELECTOR, '.zRM9F> a')

# 시작시간
start = time.time()
print('----------크롤링 시작-----------')

# 딕셔너리 생성
store_data = []

# 크롤링 (페이지 리스트 만큼)
for btn in range(len(next_btn))[1:]:  # next_btn[0] = 이전 페이지 버튼 (무시)
    store_list = driver.find_elements(By.CSS_SELECTOR, 'li.VLTHu')
    names = driver.find_elements(By.CSS_SELECTOR, '.YwYLL')  # 상호명

    for data in range(len(store_list)):  
        print(data)

        sleep(1)
        try:
            # 상호명 초기화
            store_name = ''

            # 상호명 가져오기
            store_name = names[data].text
            print(store_name)

            # 주소 버튼 누르기
            address_buttons = driver.find_elements(By.CSS_SELECTOR, '.lWwyx > a')
            address_buttons.__getitem__(data).click()
            sleep(1)

            # 주소 눌렀을 때 도로명 나오는 span
            # 도로명 주소 저장
            first_span_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.zZfO1')))
            first_span_text = first_span_element.text
            road_address = first_span_text[3:-2]
            print("도로명 주소:", road_address)

            # 딕셔너리에 데이터 추가
            store_data.append({'상호명': store_name, '주소': road_address, '지역' : '경기도'})
            print(f'{store_name} ...완료')

            sleep(1)
        
        # 에러 발생 시 (현재 list range 에러 발생)
        except Exception as e:
            print(e)
            print('ERROR!' * 3)

            # 에러 발생 시 넘어감
            continue
            
    if names[-1]:  # 마지막 리스트면 다음 페이지
        next_btn[-1].click()
        sleep(2)

    else:
        print('페이지 인식 못함')
        break
        
    # 다음 페이지 버튼 누를 수 없으면 종료
    if not next_btn[-1].is_enabled():
        break

print('[데이터 수집 완료]\n소요 시간 :', time.time() - start)
driver.quit()  # 작업이 끝나면 창을 닫는다.

# 딕셔너리를 JSON 파일로 저장
with open('store_data.json', 'w', encoding='utf-8') as f:
    json.dump(store_data, f, indent=4, ensure_ascii=False)
