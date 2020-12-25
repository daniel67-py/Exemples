#!/usr/bin/python3
#-*- coding: utf-8 -*-

import smtplib, ssl

# ce script permet d'envoyer un email assez basique en utilisant les modules smtplib et ssl
# il utilise un serveur SMTP Gmail, et ne supporte que les caractères ascii. Les caractères
# utf-8 et unicode non supportés par ascii seront automatiquement remplacés par un ?.

def envoi_texte(emetteur, mot_de_passe, destinataire, texte):
    smtp_adress = 'smtp.gmail.com'
    smtp_port = 465
    email_adress = emetteur
    email_password = mot_de_passe
    email_receiver = destinataire
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_adress, smtp_port, context = context) as server:
        print("email en cours d'envoi")
        server.login(email_adress, email_password)
        server.sendmail(email_adress, email_receiver, texte.encode('ascii', 'replace'))

    print('email envoyé !')
