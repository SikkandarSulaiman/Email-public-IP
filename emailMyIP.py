import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from urllib2 import urlopen
from time import sleep,strftime


prev_ip = '0.0.0.0'
while True:
    ip = urlopen('http://ip.42.pl/raw').read()
    if ip == prev_ip:
        sleep(1000)
    else:
        msg = MIMEMultipart()
        From = "sender@mail.com" #Change to mail ID from which you need to send
        To = "receiver@mail.com" #Change to the receiving mail ID
        #Both can be same
        
        msg['From'] = From
        msg['To'] = To
        msg['Subject'] = ip

        body = "Last update "+strftime("%H:%M        %Y-%m-%d")
        msg.attach(MIMEText(body, 'plain'))

        #if sending from Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587) 
        #for yahoo
        #server = smtplib.SMTP('smtp.mail.yahoo.com', 465)
        #for hotmail
        #server = smtplib.SMTP('smtp.live.com', 465) or
        #server = smtplib.SMTP('smtp.live.com', 25)
        server.starttls()
        server.login(From, "YOUR-PASSWORD")
        text = msg.as_string()
        server.sendmail(From, To, text)
        server.quit()
        prev_ip = ip
