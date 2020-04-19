def sendmail(uid):

    # Python code to illustrate Sending mail from  
    # your Gmail account  
    import smtplib
    import random 
  
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.ehlo()
    # start TLS for security 
    s.starttls() 
  
    # Authentication 
    s.login("random@gmail.com", "4545545") 
    otp=''
    alpha=list(range(0,10))+list(map(chr,range(97,123)))
    for i in range(6):
        otp+=str(random.choice(alpha))  
    # message to be sent 
    message = "Hi ,this is the requested OTP \n\t{0}".format(otp)
  
    # sending the mail 
    s.sendmail("random@gmail", uid, message) 
  
    # terminating t
    s.quit() 
    return otp