import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders 
fromaddr = "reshmapsakthi1234@gmail.com"
toaddr = "reshmapgowda1234@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "send the attachments"
body="attachment"
msg.attach(MIMEText(body, 'plain'))
filename = "msg.py"
attachment = open("/home/bl215/Reshma/msg.py","rb")
p = MIMEBase('application','octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(p)
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()  
s.login(fromaddr, "reshmapgowda1234")
text = msg.as_string()
s.sendmail(fromaddr, toaddr, text)
s.quit() 