# -*- coding: utf-8 -*-
import math
import os
import random
import time
import cv2
import openpyxl
import pyautogui
import selenium
from lxml import etree
from selenium import webdriver
from selenium.webdriver import ActionChains

# from selenium.webdriver.common. keys import Keys
pyautogui.FAILSAFE = True
filepath = './picture'  # 文件存储目录
url = 'https://www.douyin.com/'

opt = webdriver.ChromeOptions()
opt.add_experimental_option('excludeSwitches', ['enable-automation'])
opt.add_argument('profile-directory=Default')
# opt.add_argument('--headless')

def main():
    if not os.path.exists(filepath):
        os.mkdir(filepath)
    cookies = get_cookiess()
    # cookies = load_cookiess()  #调试用
    for i in range(1000):
        run(cookies)
    
 # 加载cookies    
def load_cookiess():
    with open('cookie.txt','r',encoding='utf-8') as f:
        result = f.read()
    return eval(result)

# 保存cookies 
def get_cookiess():
    bro = webdriver.Chrome(executable_path='/Users/apple/anaconda3/bin/chromedriver-2', options=opt)
    bro.get(url)
    print('请登录')
    time.sleep(60)
    result = bro.get_cookies()
    with open('cookie.txt','w',encoding='utf-8') as f:
        f.write(str(result))
    bro.quit()
    return result


def run(cookies):
    all_info_list = []
    bro = webdriver.Chrome(executable_path='/Users/apple/anaconda3/bin/chromedriver-2', options=opt)
    bro.get(url)
    for i in cookies:
        bro.add_cookie(i)
    bro.get(url)
    bro.maximize_window() #放大页面
    bro.implicitly_wait(5)
    comment_flag =  bro.find_elements_by_class_name('P9gNnSUG') #滑块验证破解
    try:
        count = 0
        while comment_flag == []:
            print('滑块破解中...')
            bro.save_screenshot(filepath+f'/yemian{count}.png')
            xiaohuakuai = bro.find_element_by_xpath('//img[@class="captcha_verify_img_slide react-draggable sc-VigVT ggNWOG"]')
            tupian = bro.find_element_by_css_selector('img[id="captcha-verify-image"]')
            offset = get_offset(count)
            if offset == 0:
                bro.find_element_by_xpath('//span[@class="secsdk_captcha_refresh--text sc-bwzfXH gBXrMn"]').click()
                count += 1
                time.sleep(3)
            else:               
                 #print(offset)
                count += 1
                move_x(bro,xiaohuakuai,offset)
                time.sleep(6)
                comment_flag =  bro.find_elements_by_class_name('P9gNnSUG')
                print(comment_flag)
        print('已破解')

        time.sleep(10)
        # close_login(bro)
        # close_youshang(bro)
        
        
        goto_next(bro)  #下一个视频
        open_this_comment(bro) #打开评论
            
        video_count = 500
        
        for i in range(video_count):
            if isExit(bro) == False:
                close_login(bro)
                time.sleep(1)
                # #如果当前是视频的话
                # if bro.find_elements_by_class_name('gh3k9fia') != []:

                #刷新评论的次数
                for j in range(30):
                    if bro.find_elements_by_xpath('//div[@class="KyLjQrjE"]')==[]:
                        more_comment()
                        if isExit(bro) == True:
                            break
                    else:
                        print("评论已到头")
                        break
                all_info_list.append(get_info(bro))
                print(all_info_list)
                print('='*50)
                pass_this_video(bro)
                if isExit(bro) == True:      #跳过验证 重新加载页面
                    break
            else:
                break
                
            # else:
            #     goto_next(bro)
            #     continue
        
        # print(all_info_list)
        save_file(all_info_list)
        print('爬虫结束')  
    except Exception as e:            #保存退出前的数据
        print(e)
        temp = get_info(bro)
        if all_info_list != []:
            if all_info_list[-1] != temp:
                all_info_list.append(temp)
            save_file(all_info_list)
        
    # time.sleep(10)
    bro.quit()
 
 
#显示更多评论
def more_comment():
    screenWidth, screenHeight = pyautogui.size()
    pyautogui.moveTo(screenWidth*5/6, screenHeight/2)
    pyautogui.scroll(random.randint(-8000,-6000))
    # time.sleep(random.random()*0.5)
    

#打开当前评论区
def open_this_comment(bro):
    comment_flag =  bro.find_elements_by_xpath('//div[@class="P9gNnSUG"]')
    comment_flag[0].click()
    time.sleep(1)
    #点击继续看评论
    jixukanpinglun_list = bro.find_elements_by_xpath('//button[@class="q6zgm94p k-vFWw3W FDOWibym scan__button scan__button-continue"]')
    if jixukanpinglun_list != []:
        jixukanpinglun_list[0].click()
        print('继续看评论')

#关闭登录框    
def close_login(bro):
    time.sleep(1)
    login_lst = bro.find_elements_by_class_name('login-pannel__header')
    if login_lst == []:
        return
    else:
        close_lst = bro.find_elements_by_class_name('dy-account-close')
        close_lst[0].click()
        print('登录通知已关')
        return
    
#关闭右上角登录提示
def close_youshang(bro):
    time.sleep(0.5)
    
    close_lst = bro.find_elements_by_class_name('login-guide__close')
    if close_lst == []:
        return
    else:
        close_lst[0].click()
        print('右上角登录通知已关')
        return
    
#滑块验证 
def move_x(bro,xiaohuakuai,offset):
    cishu = random.randint(3,8)
    every_max = math.ceil(offset/cishu)
    now_offset = 0
    action = ActionChains(bro)
    action.click_and_hold(xiaohuakuai)
    for i in range(cishu):
        every_offset = random.randint(10,every_max)
        time.sleep(0.2)
        action.move_by_offset(every_offset,0)
        now_offset += every_offset
    time.sleep(0.3)
    action.move_by_offset(offset-now_offset,0)
    action.release().perform()
    
#刷下一个视频   
def goto_next(bro):
    # if bro.find_elements_by_class_name('gh3k9fia') != []:
    #     pass_this_video(bro)
    # elif bro.find_elements_by_class_name('_2O5h0MA3') != []:
    #     pass_this_live(bro)
    pyautogui.press('DOWN')
        
        
def get_offset(count):
    min_area = 11000
    max_area = 13000
    img_src = f'./picture/yemian{count}.png'
    final_fold = './picture/result'
    final1 = final_fold+f'/{count}.png'
    if not os.path.exists(final_fold):
        os.mkdir(final_fold)
    img0 = cv2.imread(img_src)
    h1,w1 = img0.shape[0:2]
    x1 = math.ceil(w1*0.2)
    y1 = math.ceil(h1*0.2)
    x2 = math.ceil(x1+w1*0.6)
    y2 = math.ceil(y1+h1*0.6)
    img1 = img0[y1:y2,x1:x2]
    img2 = cv2.Canny(img1,180,240)
    contours, hierarchy = cv2.findContours(img2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
    img4 = img1[y:y+h,x:x+w]
    width,height = img4.shape[0:2]
    img4 = cv2.GaussianBlur(img4,(3,3),0)
    h2,w2 = img4.shape[0:2]
    y1 = math.ceil(0.18*h2)
    y2 = math.ceil(y1+0.6*h2)
    x1 = math.ceil(0.05*w2)
    x2 = math.ceil(x1+0.9*w2)
    img6 = img4[y1:y2,x1:x2]
    img7 = cv2.Canny(img6,400,600)
    contours, hierarchy = cv2.findContours(img7,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    offset = 0
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        if min_area<w*h<max_area and 400>x>100:
            offset = x
    if offset == 0:
        return 0
    else:
        print(offset)
        cv2.line(img6,(offset,0),(offset,h2),(0,0,255),2)
        cv2.imwrite(final1,img6)
        bili = 0.015
        result = (offset-math.ceil(width*bili))/2
        print(result)
        return result
 #跳过当前视频   
def pass_this_video(bro):
    sp = bro.find_element_by_class_name('gh3k9fia')
    action = ActionChains(bro)
    action.click_and_hold(sp)
    time.sleep(0.3)
    action.move_by_offset(0,random.randint(-200,-100))
    time.sleep(0.3)
    action.move_by_offset(0,random.randint(-200,-100))
    time.sleep(0.3)
    action.release().perform()
#跳直播
def pass_this_live(bro):
    sp = bro.find_element_by_class_name('_2O5h0MA3')
    action = ActionChains(bro)
    action.click_and_hold(sp)
    time.sleep(0.3)
    action.move_by_offset(0,random.randint(-200,-100))
    time.sleep(0.3)
    action.move_by_offset(0,random.randint(-200,-100))
    time.sleep(0.3)
    action.release().perform()


#读取信息
# all_info_list=[]
def get_info(bro):
    pagetext = bro.page_source
    tree = etree.HTML(pagetext)
    comment = tree.xpath('//span[@class="RgarU4oC"]//text()')
    final_comment = []
    if comment != []:
        for cmt in comment:
            if '@' not in cmt:
                final_comment.append(cmt)
    final_comment = ' '.join(final_comment).replace('\'','').replace('[','').replace(']','')
    introduce = ''.join(tree.xpath('//div[@class="title"]//span[@class="mzZanXbP"]//text()')).strip()
    info_list =[introduce,final_comment]
    # print(info_list)
    # print('-'*20)
    return info_list
#     all_info_list.append(info_list)
#     time.sleep(1)

#确认验证框出现
def isExit(bro):
    flag_lst = bro.find_elements_by_xpath('//div[@role="dialog"]')
    if flag_lst == []:
        return False
    else:
        print(flag_lst)
        return True
    
 #保存数据到文档   
def save_file(data):
    wb = openpyxl.Workbook()
    header = ['视频内容','评论']
    sheet = wb.active
    sheet.append(header)
    for i in data:
        sheet.append(i)

    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    wb.save(f'douyin{now}.xlsx')

if __name__=='__main__':
    main()
    
