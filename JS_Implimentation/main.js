//define mail composer library
var MailComposer = require('mailcomposer').MailComposer;
var axios = require('axios');

//return the price of BTC from coinbase api to use in other functions using axios library
function getBTCPrice() {
    return axios.get('https://api.coinbase.com/v2/prices/BTC-USD/spot')
        .then(function (response) {
            return response.data.data.amount;
        })
        .catch(function (error) {
            console.log(error);
        });
}

//get current time in month, day, year, hour, minute, second
function getTime() {
    var d = new Date();
    var month = d.getMonth() + 1;
    var day = d.getDate();
    var year = d.getFullYear();
    var hour = d.getHours();
    var minute = d.getMinutes();
    var second = d.getSeconds();
    if (month.toString().length == 1) {
        var month = '0' + month;
    }
    if (day.toString().length == 1) {
        var day = '0' + day;
    }
    if (hour.toString().length == 1) {
        var hour = '0' + hour;
    }
    if (minute.toString().length == 1) {
        var minute = '0' + minute;
    }
    if (second.toString().length == 1) {
        var second = '0' + second;
    }
    var dateTime = month + '/' + day + '/' + year + ' ' + hour + ':' + minute + ':' + second;
    return dateTime;
}

//send email to user through gmail smtp server
function sendEmail() {
    var email = 'austinhadley2004@gmail.com';
    var subject = "Bitcoin Price Alert";
    var body = "At: " + getTime() + " Bitcoin's price is :" + getBTCPrice();
    var server = "smtp.gmail.com";
    var port = 465;
    var username = "ahadley1124@gmail.com";
    var password = "wzkbhmjuzssnyihx";
    var to = email;
    var from = "ahadley1124@gmail.com";
    var mail = new MailComposer();
    mail.setMessageOption({
        from: from,
        to: to,
        subject: subject,
        body: body
    });
    mail.buildMessage(function(message) {
        var data = {
            message: message,
            server: server,
            port: port,
            username: username,
            password: password
        };
        mail.sendMail(data, function(error, response) {
            if (error) {
                console.log(error);
            } else {
                console.log(response);
            }
        });
    });
}

//log the date and price of bitcoin to the console
function log() {
    console.log(getTime() + " " + getBTCPrice());
}

//send an email and log the date and price of bitcoin to the console every minute
setInterval(function() {
    sendEmail();
    log();
}, 60000);
