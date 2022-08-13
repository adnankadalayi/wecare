import os
import random
from twilio.rest import Client

def generate_otp():
    print(os.environ["PATH"])

    account_sid = 'ACe3f88ce90341561def57fbb8b601e699'
    auth_token = 'fa8af45db1c1850d405c685a0787ee49'
    # client = Client(settings.ACCOUNT_SIF, settings.AUTH_TOKEN)
    client = Client(account_sid, auth_token)

    otp = random.randrange(1000,9999)
    print(otp)

    message = client.messages.create(
                                body='Your OTP code is ' + str(otp),
                                from_='+19097265332',
                                to='+919497099873'
                            )
    print(message.body)
    print(message.sid)


