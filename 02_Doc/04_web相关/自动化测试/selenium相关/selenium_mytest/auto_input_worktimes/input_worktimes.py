#! python
# -*- coding:utf-8 -*-

import time
import configparser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


CONFIGFILE = './cfg.ini'


def log_err(str):
    with open('./error.log', 'a') as f:
        f.write(time.ctime() + "==> Error: ")
        f.write(str + "\n")


def get_cfg():
    cfg = configparser.ConfigParser()
    cfg.read(CONFIGFILE, encoding="utf-8-sig")
    brws = cfg.get('browser', 'browser_type')
    url = cfg.get('login', 'weburl')
    name = cfg.get('login', 'account')
    pwd = cfg.get('login', 'password')
    level = cfg.get('auto_level', 'stop_site')
    file = cfg.get('input', 'datafile')
    return brws,url,name,pwd,level,file


def add_worktimes(dfile, web):
    cfg = configparser.ConfigParser()
    cfg.read(dfile, encoding="utf-8-sig")

    for section in cfg.sections():
        prj_clss = cfg.get(section, "project_class").strip()
        prj = cfg.get(section, "project").strip()
        mc = cfg.get(section, "maintain_class").strip()
        timeh = cfg.get(section, "hour").strip()
        rmk = cfg.get(section, "remarks").strip()

        ##
        # print(prj_clss)
        # print(prj)
        # print(mc)
        # print(timeh)
        # print(rmk)

 
        ## new worktimes
        elem = web.find_element_by_id('insertBtn')
        elem.click()


        # into new iframe, notes: it is not a newwindow, but a iframe
        web.implicitly_wait(10)
        web.switch_to_frame('layui-layer-iframe1')

        #print(web.current_window_handle)
        #print(web.window_handles)

        elem = web.find_element_by_id('firstclass')
        web.implicitly_wait(10)
        #Select(elem).select_by_value(prj_clss)
        Select(elem).select_by_visible_text(prj_clss)
        #Select(elem).select_by_index(5)
        web.implicitly_wait(10)

        elem = web.find_element_by_id('projectid')
        #elem = web.find_element_by_name('projectid')
        web.implicitly_wait(10)
        Select(elem).select_by_visible_text(prj)
        web.implicitly_wait(10)

        if prj_clss == "维护工时":
            elem = web.find_element_by_id('maintainsubs')
            #elem = web.find_element_by_name('maintainsubs')
            Select(elem).select_by_visible_text(mc)

        elem = web.find_element_by_id('worktime')
        elem.send_keys(timeh)

        elem = web.find_element_by_id('memo')
        elem.send_keys(rmk)

        subm = web.find_element_by_id('addBtn')
        subm.send_keys(Keys.ENTER)

    ## return defaut web
    #web.switch_to_default_content()


def submit_worktimes(b):
    linkbtn = b.find_element_by_link_text('提交工时')
    linkbtn.click()
    b.implicitly_wait(10)
    b.switch_to_window(b.window_handles[-1])

    ## select all, prepare submit
    #btn = b.find_element_by_id("selectall")
    #btn.click()
    #sbtns = b.find_elements_by_class_name('btn btn-primary')
    #for btn in sbtns:
    #    if btn.text == "全选":
    #        btn.click()
    #btn.send_keys(Keys.ENTER)

    cboxs = b.find_elements_by_name("_check")
    for chk in cboxs:
        if not chk.is_selected():
            chk.send_keys(Keys.SPACE)

    ## submit
    btns = b.find_elements_by_class_name('btn btn-info')
    #find_elements_by_tag_name('')
    for submit_b in btns:
        if submit_b.text == "提交":
            submit_b.click()
            break

    b.implicitly_wait(10)
    b.switch_to_window(b.window_handles[-1])
    btns = b.find_elements_by_class_name('layui-layer-btn0')
    for submit_b in btns:
        if submit_b.text == "确定":
            submit_b.click()
            break

    b.implicitly_wait(10)
    b.switch_to_window(b.window_handles[-1])
    btns = b.find_elements_by_class_name('layui-layer-btn0')
    for submit_b in btns:
        if submit_b.text == "确定":
            submit_b.click()
            break


def run(brws,url,name,pwd,level,file):
    if brws == 'Edge':
        b = webdriver.Edge()
    elif brws == 'Firefox':
        b = webdriver.Firefox()
    elif brws == 'Chrome':
        b = webdriver.Chrome()
    elif brws == 'Ie':
        b = webdriver.Ie()
    else:
        log_err("Unkonw browser type, please set it in cfg.ini file!")
        return

    b.get(url)
    elem_n = b.find_element_by_id('userName')
    elem_n.clear()
    elem_n.send_keys(name)
    elem_p = b.find_element_by_id('password')
    elem_p.clear()
    elem_p.send_keys(pwd)
    btn = b.find_element_by_id('loginBtn')
    btn.click()

    # new windows which already login.
    b.implicitly_wait(10)
    b.switch_to_window(b.window_handles[-1])

    if (level == "login"):
        return 0

    ## input
    add_worktimes(file, b)

    if (level == "add_all_tasks"):
        return 0

    #mybtn = b.find_element_by_link_text("历史记录")
    #mybtn.click()
    submit_worktimes(b)
    return 0


def main():
    brws,url,name,pwd,level,file = get_cfg()
    run(brws,url,name,pwd,level,file)


if __name__ == '__main__':
    main()
