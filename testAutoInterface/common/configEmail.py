__author__ = '791399137'
import os
#import win32com.client as win32
import datetime
import sys
sys.path.append("..")
import readConfig
import getpathInfo
# import readConfig
# import getpathInfo
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
#SMTP服务器
SMTPSever = "smtp.qq.com"
#发邮件的地址
sender = "545775627@qq.com"
receiver = "791399137@qq.com"
#发送这邮箱的密码
passwd = "gfmrflywrvvzbgai"


read_conf = readConfig.ReadConfig()
subject = read_conf.get_email('subject')#从配置文件中读取，邮件主题
app = str(read_conf.get_email('app'))#从配置文件中读取，邮件类型
addressee = read_conf.get_email('addressee')#从配置文件中读取，邮件收件人
content = read_conf.get_email('content')
#cc = read_conf.get_email('cc')#从配置文件中读取，邮件抄送人
mail_path = os.path.join(getpathInfo.get_Path(), 'result', 'report.html')#获取测试报告路径
print(mail_path)
class send_email():
    def outlook(self):
        ret=True
        try:
            # content = """
            #         执行测试中……
            #         测试已完成！！
            #         生成报告中……
            #         报告已生成……
            #         报告已邮件发送！！
            #         """
            msg=MIMEMultipart()
            msg.attach(MIMEText(content, 'plain', 'utf-8'))
            msg['From']=formataddr(["发件人昵称",sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To']=formataddr(["收件人昵称",addressee])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject']=str(datetime.datetime.now())[0:19]+'%s' %subject#邮件主题                # 邮件的主题，也可以说是标题
            attachment = MIMEApplication(open(mail_path, 'rb').read())
            attachment.add_header('Content-Disposition', 'attachment', filename='report.html')
            msg.attach(attachment)
            server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
            server.login(sender, passwd)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(sender,[addressee,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()# 关闭连接
        except Exception:# 如果 try 中的语句没有执行，则会执行下面的 ret=False
            ret=False
        return ret


if __name__ == '__main__':# 运营此文件来验证写的send_email是否正确
    print(subject)
    ret=send_email().outlook()
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")
