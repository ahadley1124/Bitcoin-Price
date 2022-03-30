import websockets
import asyncio
import json

#create a connection to the coinbase websocket
async def connect_to_websocket():
    async with websockets.connect('wss://ws-feed.exchange.coinbase.com') as websocket:
        await websocket.send(json.dumps({
            "type": "subscribe",
            "product_ids": ["BTC-USD"],
            "channels": ["ticker"]
        }))
        while True:
            message = await websocket.recv()
            print(message["price"])

#send an email when the price of bitcoin changes by more than 100 dollars
async def send_email(price, current_time):
    import smtplib, ssl
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "ahadley1124@gmail.com"  # Enter your address
    receiver_email = "austinhadley2004@gmail.com"  # Enter receiver address
    password = 'wzkbhmjuzssnyihx'
    message = """\
    Subject: Bitcoin Update:\n\n\
    At: {current_time}, The price of bitcoin is: {price}""".format(current_time=current_time, price=price)
    #send the email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

#run the program
asyncio.get_event_loop().run_until_complete(connect_to_websocket())