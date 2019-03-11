import smtplib
try:
	s=smtplib.SMTP('smtp.gmail.com','587')
	s.starttls()
	sender='reshmapsakthi1234@gmail.com'
	receiver='receiver@gmail.com'
	msg="hii"
	s.login(sender,'reshmapgowda1234')
	s.sendmail(sender,receiver,msg)
except:
	print("some error occured")
else:
	print("msg sent successfully")
	s.quit()	

