const Web = require('websocket').w3cwebsocket;
const ws = new Web('wss://ws-feed.exchange.coinbase.com');
var firstPrice = 0;
const recipients = 'austinhadley2004@gmail.com';

ws.onerror = function(e) {
    console.log('Error: ' + e.data);
}

ws.onclose = function() {
    console.log('Reconnecting...');
    ws = new Web('wss://ws-feed.exchange.coinbase.com');
}

ws.onopen = function() {
    ws.send(JSON.stringify({
        "type": "subscribe",
        "product_ids": ["BTC-USD"],
        "channels": ["ticker"]
    }));
}

ws.onmessage = function(e) {
    var data = JSON.parse(e.data);
    if(firstPrice == 0) {
        firstPrice = data.price;
    }
    else {
        // when the price changes by more than .25%, change the firstPrice variable
        checkPrice(data.price, .25, recipients);
    }
}

// send an email to a list of recipients
function sendEmail(recipients, subject, body) {
    var nodemailer = require('nodemailer');
    var transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {
            user: 'ahadley1124@gmail.com',
            pass: 'wzkbhmjuzssnyihx'
        }
    });

    var mailOptions = {
        from: 'ahadley1124@gmail.com',
        to: recipients,
        subject: subject,
        text: body
    };

    transporter.sendMail(mailOptions, function(error, info){
        if (error) {
            console.log(error);
        } else {
            console.log('Email sent: ' + info.response);
        }
    });
}

// send an email if the price changes by a certain percentage
function checkPrice(price, percent, recipients) {
    var change = (price - firstPrice) / firstPrice;
    if(change > percent) {
        sendEmail(recipients, 'Price Change', 'The price has changed by ' + change + '%');
        firstPrice = price;
    }
}

// start the websocket connection
ws.onopen();
