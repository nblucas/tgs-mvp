import smtplib
import email.message

def enviar_email():
    corpo_email = """  
    
    """                                           # Corpo do e-mail em html

    msg = email.message.Message()
    msg['Subject'] = " "                          # Assunto do e-mail
    msg['From'] = ' '                             # E-mail do Cozinhapp
    msg['To'] = ' '                               # E-mail do cliente
    password = ' '                                # Senha de uso unico do e-mail
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar_email()
