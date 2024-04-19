"""
@filename EmailSender.py
@author 葛文星
@encoding utf-8
@createTime 2024-4-19
@description 邮件发送工具
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailSender:
    def __init__(
        self,
        email_user: str,
        email_password: str,
        smtp_server: str = "smtp.163.com",
        smtp_port: int = 587,
    ) -> None:
        """
        :param email_user: 邮箱用户名
        :param email_password: 邮箱密码
        :param smtp_server: SMTP服务器地址
        :param smtp_port: SMTP服务器端口
        """
        self.emailUser = email_user
        self.emailPassword = email_password
        self.smtpServer = smtp_server
        self.smtpPort = smtp_port
        self.isConnected = False  # 服务器是否连接了

    # 连接邮箱服务器
    def connect(self) -> None:
        """
        连接邮箱服务器
        """
        self.server = smtplib.SMTP_SSL(host=self.smtpServer, port=self.smtpPort)  # 创建邮箱服务器
        self.server.login(
            user=self.emailUser, password=self.emailPassword
        )  # 登录邮箱服务器
        self.isConnected = True  # 设置服务器为连接状态

    # 退出邮箱服务器连接
    def quit(self) -> None:
        """
        退出邮箱服务器连接
        """
        self.server.quit()
        self.isConnected = False  # 设置服务器为未连接状态

    # 发送文本内容
    def sendText(self, target: str, subject: str, content: str) -> None:
        """
        发送文本内容
        :param target: 目标邮箱
        :param subject: 邮件标题
        :param content: 邮件内容
        """
        # 配置邮件内容
        msg = MIMEMultipart()
        msg["From"] = self.emailUser
        msg["To"] = target
        msg["Subject"] = subject

        msg.attach(MIMEText(content, "plain"))

        # 发送邮件
        if self.isConnected:
            self.server.sendmail(
                from_addr=self.emailUser, to_addrs=target, msg=msg.as_string()
            )
        else:
            # 如果未连接则进行连接
            self.connect()
            self.server.sendmail(
                from_addr=self.emailUser, to_addrs=target, msg=msg.as_string()
            )

    # 发送html内容
    def sendHtml(self, target: str, subject: str, content: str) -> None:
        """
        发送html内容
        :param target: 目标邮箱
        :param subject: 邮件标题
        :param content: 邮件内容
        """
        # 配置邮件内容
        msg = MIMEMultipart()
        msg["From"] = self.emailUser
        msg["To"] = target
        msg["Subject"] = subject

        msg.attach(MIMEText(content, "html"))

        # 发送邮件
        if self.isConnected:
            self.server.sendmail(
                from_addr=self.emailUser, to_addrs=target, msg=msg.as_string()
            )
        else:
            # 如果未连接则进行连接
            self.connect()
            self.server.sendmail(
                from_addr=self.emailUser, to_addrs=target, msg=msg.as_string()
            )
