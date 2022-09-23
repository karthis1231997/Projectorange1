from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pageObjects.login_page import Login
from utilities.verify_user import Verify
from utilities.readProperties import Readconfig
import time
import logging


class Test_orange():
    baseurl = Readconfig.getorangeurl()
    username = Readconfig.getuserid()
    password = Readconfig.getpassword()
    fname = "ram"
    mname = "kumar"
    lname = "sri"
    creat_user = "success"
    creat_password = "Qwerty@123"
    imgss = "C:\\Users\\hkarthis\\PycharmProjects\\Projectoneorange\\testData\\download.png"
    logging.basicConfig(filename="C:\\Users\\hkarthis\\PycharmProjects\\Projectoneorange\\logs\\logs.txt")
    logger = logging.getLogger()


    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        login_page_obj=Login(self.driver)
        time.sleep(3)
        login_page_obj.set_username(self.username)
        login_page_obj.set_password(self.password)
        login_page_obj.click_login()
        self.driver.save_screenshot("C:\\Users\\hkarthis\\PycharmProjects\\Projectoneorange\\screenshots\\image2.png")
        self.logger.warning("*******log-in success***********")
        login_page_obj.click_add_emp()
        self.driver.implicitly_wait(10)
        #login_page_obj.imgs_send()
        login_page_obj.set_firsname(self.fname)
        login_page_obj.set_midmane(self.mname)
        login_page_obj.set_lastname(self.lname)
        time.sleep(3)
        login_page_obj.checkbox_info()
        login_page_obj.set_create_username(self.creat_user)
        login_page_obj.set_create_password(self.creat_password)
        login_page_obj.set_creat_c_pass(self.creat_password)
        login_page_obj.click_empsave()
        time.sleep(2)
        login_page_obj.click_admin()
        time.sleep(3)
        login_page_obj.search_username(self.creat_user)
        login_page_obj.search_click()
        #data0=login_page_obj.get_rec()
        #data1=login_page_obj.get_datas()
        data2=login_page_obj.get_sys_user()
        name = data2
        ver_user = Verify(self.driver)
        ver_user.ver_user(name)
        login_page_obj.log_out_one()
        login_page_obj.log_out_two()
        login_page_obj.set_username(self.creat_user)
        login_page_obj.set_password(self.creat_password)
        login_page_obj.click_login()


