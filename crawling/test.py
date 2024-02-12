import json
import time
from time import sleep
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


url = 'https://map.naver.com/v5/search'
driver = webdriver.Chrome()  # 드라이버 경로
driver.get(url)
key_word = ['경기도', '강원도', '충청북도', '충청남도', '경상북도', '경상남도', '전라북도', '전라남도',
            '서울', '인천', '대전', '대구', '부산', '울산', '광주', '제주']  # 지역 키워드


def time_wait(num, code):
    try:
        wait = WebDriverWait(driver, num).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, code)))
        sleep(4)
        return wait
    except:
        print(code, '태그를 찾지 못하였습니다.')
        driver.quit()
        return None
    

def path_search(num, code) :
    try :
        value = WebDriverWait(driver, num).until(
                EC.presence_of_element_located((By.XPATH, code)))
        sleep(4)
        return value
    except :
        print(code, '찾지 못함')
        driver.quit()
        return None

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

# csv파일 만들기
def add_file(key_word) :
    df = pd.read_json(f'./store_data.json')
    df.index = df.index + 1
    
    # csv파일로 저장
    csv_filename = f'{key_word} 바디프로필 임시.csv'
    df.to_csv(csv_filename, encoding = 'euc-kr')
    print(f'============={key_word} 바디프로필 csv파일 완성=============')

    # CSV 파일을 읽기
    df = pd.read_csv(f'{key_word} 바디프로필 임시.csv', encoding='euc-kr')
    # 중복된 행을 제거
    df.drop_duplicates(subset='상호명', inplace=True)
    # 스튜디오 아닌 것 제거
    df = df[df['종류'].isin(['프로필사진전문', '사진,스튜디오' ])]
    # 인덱스를 재설정
    df.reset_index(drop=True, inplace=True)
    # 수정된 데이터프레임을 CSV 파일로 저장
    df.to_csv(f'{key_word} 바디프로필.csv', index=False, encoding='euc-kr')
    print(f'============={key_word} 바디프로필 csv파일 수정 완료!!=============')

def search_data(key_word) :
    # 딕셔너리 생성 
    store_data = [] 
    # css를 찾을때 까지 10초 대기
    time_wait(10, 'div.input_box > input.input_search')
    
    # 검색창 
    search = driver.find_element(By.CSS_SELECTOR, 'div.input_box > input.input_search')
    search.send_keys(f'{key_word} 바디프로필')  
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
    print(f'btn = {len(next_btn)}')

    # 시작시간
    start = time.time()
    print('----------크롤링 시작-----------')
    
    counting = 1
    
    # 크롤링 
    for btn in range(len(next_btn))[1:] :  
        switch_frame('searchIframe')
        store_list = driver.find_elements(By.CSS_SELECTOR, 'li.VLTHu')  
        names = driver.find_elements(By.CSS_SELECTOR, '.YwYLL')  # 상호명
        store_types = driver.find_elements(By.CSS_SELECTOR, '.YzBgS')   # 가게 종류
        link_buttons = driver.find_elements(By.CSS_SELECTOR, '.ouxiq > a')  # 상세정보 링크
        
        for data in range(len(store_list)):  
            print(data + 1)       
            
            # 광고 무시하기
            # ad_search = driver.find_elements(By.CSS_SELECTOR, '.qbGlu')[data].text
            # if '광고' in ad_search :
            #     continue 
                
            try:   
                # 초기화
                store_name = ''
                road_address = ''
                phone_number = ''
                links = []
                image_urls = []
                store_type = ''
                
                # 가게 종류
                store_type = store_types[data].text
                print('type : ', store_type)
                
                # 상세 정보 버튼 누르기
                link_buttons.__getitem__(data*2).click()
                sleep(3)
                
                # 상세 정보 프레임 변경
                switch_frame('entryIframe')
                
                # 상호명 가져오기
                store_name_element = path_search(10, '//*[@id="_title"]/div/span[1]')
                store_name = store_name_element.text
                print('상호명 : ', store_name)

                # 주소 가져오기
                address_element = path_search(10,'//*[@id="app-root"]/div/div/div/div[5]/div/div[2]/div/div/div[1]/div/a/span[1]')
                road_address = address_element.text
                print('주소 : ', road_address)
                
                # 전화 번호 가져오기
                # phone_number_element = driver.find_element(By.CSS_SELECTOR, '.PIbes > div.O8qbU.nbXkr > span.xlx7Q')
                try :
                    phone_number_element = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((
                        By.CSS_SELECTOR, 'div.PIbes > div.O8qbU.nbXkr > div.vV_z_ > span.xlx7Q')))
                    # phone_number_element = path_search(10, '//*[@id="app-root"]/div/div/div/div[5]/div/div[2]/div/div/div[4]/div/span[1]')
                    phone_number = phone_number_element.text
                    print('전화번호 : ', phone_number)
                except :
                    print('번호 없음')
                    phone_number = 'None'
                
                # 링크 가져오기
                try :
                    div_link_elements = WebDriverWait(driver, 30).until(            
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.PIbes > div.O8qbU.yIPfO > div.vV_z_ a')))
                    for link_element in div_link_elements :
                        link_href = link_element.get_attribute('href')
                        links.append(link_href)
                        
                    print('링크 : ', links)
                except Exception as ee :
                    print('링크 에러발생 : ', ee)
                    links = 'None'

                # 이미지 가져오기
                try:
                    # 이미지를 포함한 div 요소 찾기
                    image_divs = driver.find_elements(By.CSS_SELECTOR, 'div.K0PDV._div')

                    # 이미지가 있는 경우
                    if image_divs:
                        for i, image_div in enumerate(image_divs, start=1):  # 시작 인덱스를 1로 지정
                            # 이미지 URL 추출
                            style = image_div.get_attribute('style')
                            url_start_index = style.find('url("') + len('url("')
                            url_end_index = style.find('")', url_start_index)
                            image_url = style[url_start_index:url_end_index]
                            image_urls.append(image_url)

                            # 이미지가 세 개 이상인 경우 루프 중단
                            if i == 3:
                                break

                        # 이미지가 없는 경우
                    else:
                        image_urls = 'None'

                    # 각 이미지 URL 출력
                    for idx, url in enumerate(image_urls, start=1):
                        print(f"이미지 URL {idx}번째 :", url)

                # 에러 발생 시 처리
                except Exception as e:
                    print("이미지 URL 추출 중 오류 발생:", e)
                    image_urls = 'None'



                
                    
                # 창 닫기
                close_button = path_search(10, '//*[@id="app-root"]/div/div/header/a')  
                close_button.click()  
                sleep(1)
                
                # 데이터 저장
                store_value = {
                    '상호명' : store_name, 
                    '종류' : store_type,
                    '주소' : road_address, 
                    '전화번호' : phone_number,
                    '링크' : links, 
                    '이미지' : image_urls,
                    '지역' : key_word} 
                store_data.append(store_value)
                
                print(f'-------------{store_name}-------------완료')
                switch_frame('searchIframe')
            
            # 에러 발생 시 
            except Exception as e:
                print(e)
                print('ERROR!' * 3)
                switch_frame('searchIframe')
                # 에러 발생 시 넘어감
                continue
        
        counting += 1     
        
        # 다음 페이지 버튼 누를 수 없으면 종료
        if not next_btn[-1].is_enabled():
            break

        if names[-1] :  # 마지막 리스트면 다음 페이지
            next_btn[-1].click()
            sleep(2)

        else :
            print('페이지 인식 못함')
            break
        
        if counting > 3 :   # 최대 3페이지까지만 서치하기 위해
            break
        
    # 딕셔너리를 JSON 파일로 저장 
    with open('store_data.json', 'w', encoding='utf-8') as f:
        json.dump(store_data, f, indent=4, ensure_ascii=False)
        
        
    print(f'{key_word} 데이터 수집 완료 \n소요 시간 : {time.time() - start}')
    
    add_file(key_word)
    
# 실행
for s in key_word :
    search_data(s)

driver.quit()  # 작업이 끝나면 창을 닫는다.
