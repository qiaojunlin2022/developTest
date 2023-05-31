# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/27 16:21
# @Author  : qiao
# @File    : test_login.py
from time import sleep
import pytest

from common import pconst
from common.util_json import readJson
from pages.login.p_login import Plogin


class TestLogin():
    def setup_method(self):
        self.plogin: Plogin = Plogin()

    def teardown_method(self):
        self.plogin.driver.quit()

    @pytest.mark.parametrize('param', readJson(pconst.const_json_login))
    def test_01_login(self,param):
        self.plogin.open_url(pconst.const_url)
        sleep(30)
        self.plogin.input_user_pass(param['user_name'], param['password'])
        sleep(1)
        self.plogin.button_login()
        sleep(1)
