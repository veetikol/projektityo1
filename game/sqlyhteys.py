'''Syötä alle user- ja password-muuttujien arvojen tilalle omat kirajutumistietosi'''
import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='****',
    password='****',
    autocommit=True
    )