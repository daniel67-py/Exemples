#!/usr/bin/python3
#-*- coding: utf-8 -*-

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ce script permet d'envoyer un sms via un serveur SMTP Gmail
# la fonction demande en argument : l'adresse email de l'emetteur (une adresse gmail),
# le mot de passe du compte, le destinataire du mail, le texte contenu dans le message
# et pour finir, son objet.

def envoi_gmail(emetteur, mot_de_passe, destinataire, texte_html, objet):
    smtp_adress = 'smtp.gmail.com'
    smtp_port = 465
    email_adress = emetteur
    email_password = mot_de_passe
    email_receiver = destinataire

    message = MIMEMultipart("alternative")
    message["Subject"] = objet
    message["From"] = email_adress
    message["To"] = email_receiver

    texte_html = "<p>" + texte_html + "</p>"

    html_mime = MIMEText(texte_html, 'html')

    message.attach(html_mime)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_adress, smtp_port, context = context) as server:
        print("email en cours d'envoi")
        server.login(email_adress, email_password)
        server.sendmail(email_adress, email_receiver, message.as_string())

    print('email envoyé !')
