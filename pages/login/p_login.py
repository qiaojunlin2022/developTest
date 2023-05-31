# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/27 16:13
# @Author  : qiao
# @File    : p_login.py
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from common.driver import Driver


class Plogin():
    def __init__(self):
        self.driver = Driver()
        self.odriver: WebDriver = self.driver.driver
        # 这里主要是提取分离元素，方便后期维护
        self.locator_user_name = (
            By.CSS_SELECTOR,
            "#fullscreenId > app-root > app-login > div > div.div_1 > div > nz-input-group:nth-child(1) > input")
        self.locator_password = (
            By.CSS_SELECTOR, "input.ng-pristine:nth-child(2)")
        self.locator_button_login = (
            By.CSS_SELECTOR, ".btn0 > span:nth-child(1)")

    def open_url(self, url):
        self.driver.open(url)

    # 封装基础动作-输入用户名
    def input_user_name(self, user_name):
        self.driver.send_keys(self.locator_user_name, user_name)

    # 封装基础动作-密码
    def input_pass(self, password):
        self.driver.send_keys(self.locator_password, password)

    # 封装基础动作-输入用户名+密码
    def input_user_pass(self, user_name, password):
        self.input_user_name(user_name)
        self.input_pass(password)

    # 封装业务逻辑-登陆
    def button_login(self):
        self.driver.click(self.locator_button_login)
