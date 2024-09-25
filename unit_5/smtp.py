import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('pooja71414@gmail.com','')
msg='this is demo of smtp server.'

s.sendmail('pooja71414@gmail.com','kinjal71414@gmail.com',msg)
print('mail send successfully..')

s.quit()