# E-mail-public-IP

This is a python code which sends an e-mail (to your gmail) whenever your public IP changes.

The subject of the mail consists of your new IP address.
In the body of mail, the time it was changed is written.

You can send & receive in a same mail ID for privacy if you have only one mail ID.

This will be useful in places where you need external access to your computer but you don't want to buy a website or don't want to setup a dynamic DNS.

Note:
1. For gmail, python is a less secure app and by default gmail denies logging in from python.
    You can fix this problem in https://www.google.com/settings/security/lesssecureapps
2. Look at lines 26 to 32 and comment/uncomment according to the mail server you're using.
    Leave as it is if you're using Gmail.
