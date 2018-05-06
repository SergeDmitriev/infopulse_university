def send_mail(sender, pwd, receiver, title, message):
    """
    To send mail, first activate this - https://myaccount.google.com/lesssecureapps
    """
    import smtplib

    FROM = sender
    PWD = pwd
    TO = receiver
    SUBJECT = title
    BODY = message
    MSG = 'Subject: {0}\n\n{1}'.format(SUBJECT, BODY)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        try:
            server.starttls()
            server.login(FROM, PWD)
            server.sendmail(FROM, TO, MSG)
            print('Message send successfully!')
        except Exception as e:
            print('Exception occurred:', e)


if __name__ == '__main__':
    send_mail('from@gmail.com', 'password', 'to@gmail.com', 'Letter title', 'I did it!')
