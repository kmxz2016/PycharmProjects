# 发邮件的库
import smtplib

# 文本
from email.mime.text import MIMEText

# import sender as sender

SMTPServer = "smtp.163.com"
# 发邮件地址
Sender = "13676480081@163.com"
# 发送者邮箱密码
passwd = "88888888m"

# 设置发送的内容
message = "Kevin is a good boy"
# 转换成邮件文本
msg = MIMEText(message)

# 标题
msg["Subject"] = "来自Kevin的问候"
# 发送者
msg["From"] = sender


#创建SMTP服务器
mailServer = smtplib.SMTP(SMTPServer,25)
#登录邮箱
mailServer.login(sender,passwd)
#发送邮件
mailServer.sendmail(sender,["13676480081@163.com"],msg.as_string())
#退出邮箱
mailServer.quit()