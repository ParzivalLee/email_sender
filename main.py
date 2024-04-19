"""
@filename main.py
@author 葛文星
@encoding utf-8
@createTime 2024-4-19
@description 自动发送邮件程序
"""

from email_sender import EmailSender
import time
import json

# 读取配置文件
with open("config.json", "rt", encoding="utf-8") as fp:
    config = json.load(fp=fp)

emailSender = EmailSender(
    email_user=config.get("server").get("user"),
    email_password=config.get("server").get("password"),
    smtp_server=config.get("server").get("smtp_server"),
)

print(f"[{time.strftime('%H:%M:%S')}]# 正在读取标题和内容")

subject = config.get("email").get("subject")
content = config.get("email").get("content")

print(f"标题：{subject}")

print(f"[{time.strftime('%H:%M:%S')}]# 正在连接邮箱服务器")
emailSender.connect()  # 连接邮箱服务器
for i in config.get("targets"):
    print(f"[{time.strftime('%H:%M:%S')}]# 正在发送邮件给 -> {i}")
    emailSender.sendText(
        target=i,
        subject=subject,
        content=content,
    )

emailSender.quit()  # 退出邮箱服务器连接
