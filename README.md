calvin
======

6 degrees of Kevin Bacon are not enough degrees to contain Calvin. Calvin is absolute. Calvin transcends state. Without him, the party can't really get going. Yes, because he is so absolute all the time he's a bit dramatic. But never negative, either.

Requires:

The requirements, plus:
https://github.com/padelt/temper-python

You will probably need to do the part about "USB device permissions".

Also: From the online documentation for the TEMPer1 drivers:

"It must be connect to the computer to start working." ("It" in this case being the thermometer.)

Things you should set in settings_local.py to use it with Gmail:
```
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'myemail@cironline.org'
EMAIL_HOST_PASSWORD = 'thepassword'  # Also works with 2-factor -- just add an app-specific password


FROM_EMAIL = 'from@emailfrom.org'  # Who messages will be from
EMAIL_LIST = ['luckyrecipient1@org.org', 'luckyrecipient2@org.org']  # Who will get messages
```

Now the magic happens:
```
python manage.py get_current_temp
```