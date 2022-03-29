def email(price, current_time):
    import smtplib, ssl

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "ahadley1124@gmail.com"  # Enter your address
    receiver_email = "4192070762@vzwpix.com"  # Enter receiver address
    password = 'wzkbhmjuzssnyihx'
    message = """\
    Subject: Bitcoin Update:\n\n\
    At: {current_time}, The price of bitcoin is: {price}""".format(current_time=current_time, price=price)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)