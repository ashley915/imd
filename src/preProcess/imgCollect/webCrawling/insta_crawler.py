import requests
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os, sys
import ast

def craw(search):
    #driver path 설정
    driver = webdriver.Chrome(executable_path='/home/cjonrnd/data_preprocessing/chromedriver')
    # search = input("검색어를 입력하세요")
    url = 'http://www.instagram.com/explore/tags/'+ search
   # url = "https://www.google.co.in/search?q="+search+"&source=lnms&tbm=isch&tbs=itp:face"
    page = driver.get(url)

    #html 바디테그 다 받아오기
    time.sleep(2)
    element = driver.find_element_by_tag_name("body")
    #스크롤 다운시작
    for i in range(10):
        print(i)
        element.send_keys(Keys.PAGE_DOWN)
        # try:
        #     #페이지 버튼 다름
        #     button = driver.find_element_by_xpath("//*[@id='smb']")
        #     button.click()
        #     time.sleep(1)
        # except:
        time.sleep(1)
        pass

    time.sleep(1)

    #source page 받아오기
    source = driver.page_source
    soup = bs(source,"lxml")

    dir_name = save + "_instagram"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    # os.chdir(dir_name)
    driver.close()

    #x = 0o001
    x = 0
    image_tags = soup.findAll('img' ,class_="_2di5p")
    for everything in image_tags:
        ou = everything["src"]
        try:
            source = requests.get(ou)
            if source.status_code == 200:

                file_name =  save + "_" + str(x).zfill(5) + '.jpg'
                with open(os.path.join(dir_name,file_name), 'wb') as f:
                    print(str(x))
                    f.write(requests.get(ou).content)
                    x += 1
                f.close()
        except:
            pass
#515 이미지 약 17분

if __name__== '__main__':
    word = input("검색어를 입력하세요")
    save = input("영문파일명을 입력하세요")
    #word = sys.argv[1]
    # print(word)
    # print(type(word))
    # print('start time : ', time.strftime("%y%m%d-%H%M%S"))
    start = time.time()
    craw(word)
    end = time.time()
    print(end-start)
    # print('end time : ', time.strftime("%y%m%d-%H%M%S"))