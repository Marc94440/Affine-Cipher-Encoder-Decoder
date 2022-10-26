# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, uic
import unidecode
import re

#initialising default variable
app =QtWidgets.QApplication([])
dlg = uic.loadUi("Affine_Cypher.ui")
alphabet ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a_valuetxt="A value :"
a_wrgvaluetxt="A value is wrong"
b_valuetxt="B value :"
b_wrgvaluetxt="B value is wrong"

#Encoding function, return nothing, write the encoded message in a textEdit
def Encode (): 
    dlg.New_msg_textEdit.setText("")
    message=dlg.Message_lineEdit.text().upper()
    try :
        a,b=Get_a_and_b()
    except :
        return
    try :
        message=unidecode.unidecode(message.replace(" ", "XSPACEX"))
        message=re.sub('[^a-zA-Z]+', '', message)
        new_mess=""
        for i in range (len(message)):
            new_mess+=alphabet[(alphabet.rfind(message[i])*a+b)%26]
            if((i+1)%5==0):
                new_mess+=" "
        dlg.New_msg_textEdit.setText(str(new_mess))
    except :
        return 

#Decoding function, return nothing, write the decoded message in a textEdit
def Decode ():
        dlg.New_msg_textEdit.setText("")
        message=dlg.Message_lineEdit.text().upper()
        try :
            a,b=Get_a_and_b()
        except :
            return
        try :
            x=""
            x=Inv_a(a)
            message=unidecode.unidecode(message.replace(" ", ""))
            message=re.sub('[^a-zA-Z]+', '', message)
            new_mess=""
            for i in range (len(message)):
                new_mess+=alphabet[(((alphabet.rfind(message[i]))-b)*x)%26]
            new_mess=new_mess.replace("XSPACEX"," ")
            dlg.New_msg_textEdit.setText(str(new_mess))
        except:
            return 0
            
#This function get the a and b value from labels
def Get_a_and_b ():
        try :
            a=int(dlg.A_value_lineEdit.text())
            if(a%2==0 or a==13):
                dlg.A_value_label.setText(a_wrgvaluetxt) 
            else :
                dlg.A_value_label.setText(a_valuetxt) 
        except :
            dlg.A_value_label.setText(a_wrgvaluetxt) 
        try :
            b=int(dlg.B_value_lineEdit.text())
            if(b<0 or b>25) :
                dlg.B_value_label.setText(b_wrgvaluetxt)
            else :
                dlg.B_value_label.setText(b_valuetxt) 
        except :
            dlg.B_value_label.setText(b_wrgvaluetxt)
        return a,b


#this function find the inverse modulo of value a
def Inv_a (a):
    for i in range  (1,26,2):
        if((i*a)%26==1):
            x=i
    return x

#Connection between the two button and the encoding and decoding function
dlg.Encryption_pushButton.clicked.connect(Encode)
dlg.Decryption_pushButton.clicked.connect(Decode)

#open the application
dlg.show()
app.exec()

#All the GUI Widgets
"""
A_value_lineEdit
B_value_lineEdit
type_msg_label
A_value_label
B_value_label
Message_lineEdit
Decryption_pushButton
Encryption_pushButton
New_msg_label
New_msg_textEdit
"""