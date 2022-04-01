#create websocket connection
import websocket
import json

#connect to coinbase websocket
ws = websocket.create_connection("wss://ws-feed.exchange.coinbase.com")

#subscribe to the BTC-USD ticker
ws.send(json.dumps({
    'type' : 'subscribe',
    'product_ids' : ['BTC-USD'],
    'channels' : ['ticker']
}))

#constantly listen for messages and print the price from the json message
while True:
    message = [json.loads(ws.recv())]
    message_length = len(message)
    for i in range(message_length):
        print(message[4]['price'])
