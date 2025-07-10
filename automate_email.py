import smtplib

sender_mail = input("enter sender's email :")
password = input("enter your password :")
reciever_email = input("enter reciever's email :")
subject = "your email has been hacked!"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_mail,password)
server.sendmail(sender_mail,reciever_email,subject)
quit()

print("mail sent sucessfully")




#input enter your pass enter your email enter your sender email 