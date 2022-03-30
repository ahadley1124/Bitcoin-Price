from time import sleep
import send_email
import python.dianna_email as dianna_email
import miranda_email
import time
from requests import session
import json
i = 1
old_price = 0
measure_price = 0
while True:
    sess = session()
    sess.headers.update({'CB-VERSION': '2021-04-18'})
    sess.headers.update({'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'})
    url = 'https://api.coinbase.com/v2/prices/BTC-USD/spot'
    response = sess.get(url)
    data = json.loads(response.text)
    price = data['data']['amount']
    current_time = time.strftime("%B %d, %Y, %H:%M:%S")
    #keep the first price to measure the 50 dollar difference
    if i == 1:
        measure_price = price
    if old_price != price:
        print('At: ' + current_time)
        print('The price of bitcoin is: ' + price)
        print('we have found a new price {times} times'.format(times=i))
        old_price = price
        i += 1
    #send email if the price is 50 dollars higher than the first price
    measure_price_p100 = float(measure_price) + 100
    if float(price) > measure_price_p100:
        send_email.email(price, current_time)
        measure_price = price
    measure_price_m100 = float(measure_price) - 100
    if float(price) < measure_price_m100:
        send_email.email(price, current_time)
        measure_price = price
    sleep(5)
