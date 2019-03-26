#! python
# -*- coding:utf-8 -*-

import time
import configparser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


CONFIGFILE = './cfg.ini'
#URL = 'https://www.chaojibiaoge.com//index.php/Index/loginregister/action/login'
URL = 'http://old.chaojibiaoge.com/index.php/Oa/Index/loginregister/action/login/hideheader/true'
#URL = 'http://www.baidu.com'

def login_name_pwd():
    cfg = configparser.ConfigParser()
    cfg.read(CONFIGFILE, encoding="utf-8-sig")
    name = cfg.get('login', 'name')
    pwd = cfg.get('login', 'password')
    brws = cfg.get('browser', 'browser_type')
    return brws,name,pwd

def get_employee_info():
    cfg = configparser.ConfigParser()
    cfg.read(CONFIGFILE, encoding="utf-8-sig")
    department = cfg.get('inpus', 'department')
    sub_department = cfg.get('inpus', 'sub_department')
    employee_name = cfg.get('inpus', 'employee_name')
    employee_id = cfg.get('inpus', 'employee_id')
    overtime_reason = cfg.get('inpus', 'overtime_reason')
    grp = cfg.get('inpus', 'mygroup')
    return department,sub_department,employee_name,employee_id,overtime_reason,grp

def open_web(browser, name, pwd):
    # for firefox, fast open
    # profile = webdriver.FirefoxProfile()
    # profile.set_preference("browser.startup.homepage", "about:blank")
    # profile.set_preference("startup.homepage_welcome_url", "about:blank")
    # profile.set_preference("startup.homepage_welcome_url.additional", "about:blank")

    if browser == 'Edge':
        b = webdriver.Edge()
    elif browser == 'Firefox':
        b = webdriver.Firefox()
    elif browser == 'Chrome':
        b = webdriver.Chrome()
    elif browser == 'Ie':
        b = webdriver.Ie()
    else:
        return

    b.get(URL)
    elem_n = b.find_element_by_id('_login_username')
    elem_n.clear()
    elem_n.send_keys(name)
    elem_p = b.find_element_by_id('_login_password')
    elem_p.clear()
    elem_p.send_keys(pwd)
    btn = b.find_element_by_id('_btn_signup')
    btn.click()

    # new windows which already login.
    b.implicitly_wait(10)
    b.switch_to_window(b.window_handles[-1])

    elems = b.find_elements_by_class_name('filename')
    #print(elems)

    # find 10F file
    e_10Fs = []
    datestr = time.strftime('%m').lstrip('0') + '.' + time.strftime('%d').lstrip('0')
    for el in elems:
        #print(el.text)
        if el.text.startswith('10F') and (datestr in el.text):
            e_10Fs.append(el)
    if len(e_10Fs) == 1:
        e_10Fs[0].click()
    else:
        # not find or match more then one.
        return

    # new windows which already login.
    b.implicitly_wait(10)
    b.switch_to_window(b.window_handles[-1])

    elem = b.find_element_by_id('unifile_unisheet_table_action_add')
    elem.click()

    # new windows which already login.
    b.implicitly_wait(10)
    b.switch_to_window(b.window_handles[-1])

    # write name to table
    department,sub_department,employee_name,employee_id,overtime_reason,grp = get_employee_info()
    elem = b.find_element_by_id('unifile_unisheet_table_autoform_column_1')
    elem.send_keys(department)
    elem = b.find_element_by_id('unifile_unisheet_table_autoform_column_2')
    elem.send_keys(sub_department)
    elem = b.find_element_by_id('unifile_unisheet_table_autoform_column_3')
    elem.send_keys(employee_name)
    elem = b.find_element_by_id('unifile_unisheet_table_autoform_column_4')
    elem.send_keys(employee_id)
    elem = b.find_element_by_id('unifile_unisheet_table_autoform_column_5')
    elem.send_keys(overtime_reason)
    elem = b.find_element_by_id('unifile_unisheet_table_autoform_column_6')
    elem.send_keys('1')

    elem = b.find_element_by_id('unifile_unisheet_table_autoform_column_7')
    if elem.tag_name == 'select':
        Select(elem).select_by_value(grp)
    else:
        return

    subm = b.find_element_by_id('unifile_unisheet_table_autoform_savebutton')
    #subm.click() ## Error: Element is obscured
    subm.send_keys(Keys.ENTER)

#    b.quit()

def main():
    browser,name,pwd = login_name_pwd()
    open_web(browser, name, pwd)

if __name__ == '__main__':
    main()