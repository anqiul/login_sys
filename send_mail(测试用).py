# -*- coding: utf-8 -*-
"""
send_mail

Author: 11653
Date: 2024/4/14
Description: 
"""
import os
from django.core.mail import send_mail, EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'login_sys.settings'

if __name__ == '__main__':

    subject, from_email, to = '邮箱测试', '13248039565@163.com', '1165363500@qq.com'
    text_content = '邮箱测试！'
    html_content = '测试部分'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()