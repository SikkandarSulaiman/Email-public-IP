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
        From = "sikkandarsulaiman@gmail.com"
        To = "sikkandarsulaiman@gmail.com"
        msg['From'] = From
        msg['To'] = To
        msg['Subject'] = ip

        body = "Last update "+strftime("%H:%M        %Y-%m-%d")
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(From, "ilove10dulkar")
        text = msg.as_string()
        server.sendmail(From, To, text)
        server.quit()
        prev_ip = ip
