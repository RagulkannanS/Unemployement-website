# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 13:27:53 2019

@author: naz xzawiz

"""'''
import mysql.connector
from mysql.connector import Error


mydb = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  passwd = '',
  database = 'startup')
df = pd.read_sql_query("select * from start", mydb)
print(df)'''

from gtts import gTTS
#import os
#path = ("")


a = "Crop You have selected is : Banana   Expected Year of production : 2020   District to be known : Coimbatore   Predicted value : 517701.36518085375 tons per unit"
tts = gTTS(text= a , lang='en')
tts.save("C:/wamp64/www/employee - Copy/int.mp3")
#os.system("mpg321 C:/Users/Lokesvaran/.spyder-py3/a.mp3")

from playsound import playsound
playsound('C:/wamp64/www/employee - Copy/int.mp3')

