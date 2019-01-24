import os,sys

import pytest

sys.path.append(os.getcwd())

from base.init_driver import get_driver
from page.sms_page import SmsPage
import page
class TestSms:

    def setup_class(self):
        #1.初始化driver
        self.driver = get_driver(page.sms_app_package,page.sms_app_activity)
        #2.初始化smspage类
        self.smspage = SmsPage(self.driver)
    def teardown_class(self):
        # 1 退出driver
        self.driver.quit()

    def test_add_receive_number(self):
        # 1.点击新增按钮
        self.smspage.click_add_new_sms()
        # 2.输入接收者的内容
        self.smspage.input_receive_sms_number(5555)

    #测试短信业务方法
    @pytest.mark.parametrize("content", ['aaa', 'bbb', 'ccc'])
    def test_send_sms(self,content):
        #1.实现发送内容
        self.smspage.send_sms_content(content)
        #2.实现校验.....?





