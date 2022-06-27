

from posixpath import split
from re import I


def view():
   with open ("Data.txt",'r') as OUT:
    for goo in OUT :
        user,passs = goo.split('|') 
        print ("email:",user+ " | "+ "password:" ,passs)

def add():
    name= input ("email:... ")
    pwd = input("Password:... ")

    with open ("Data.txt",'a') as IN:
       IN.write(name + '|'  +pwd+  "\n")




Master_pwd= input("Please Enter Your Master Password.. ")
    
if Master_pwd != "rubberduck":
    print (" Pleas Make Sure You Entered a Right Password "+ "\n" +" Thank You ...." )
    quit()
else: 
    while True:
        option= input("1-Add Password \n" + "2-View \n" + "3-Quit \n")
        if option == '1':
                add()
        elif option == '2':
            view() 
        else: 
            quit()


    
    
