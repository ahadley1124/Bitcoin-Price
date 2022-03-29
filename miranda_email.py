def email(price):
    import smtplib, ssl

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "ahadley1124@gmail.com"  # Enter your address
    receiver_email = "3177523032@vzwpix.com"  # Enter receiver address
    password = 'wzkbhmjuzssnyihx'
    message = """The current price of bitcoin is """ + price

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)