from os import system
from Image.ImageDecode import ImageDecode
from Image.ImageEncode import ImageEncode
from Text.TextEncode import TextEncode
from Text.TextDecode import TextDecode
system('cls')    

#----------- MENU DRIVER--------------#

while True:
    print("---------------------------------\n          STEGANOGRAPHY\n---------------------------------")
    n=(input("\n1--> Encode Text\n2--> Encode Image\n3--> Decode Text\n4--> Decode Image\n5--> Exit\n\n\nChoice:-"))
    if(n=='1'):
        TextEncode()
    elif(n=='2'):
        ImageEncode()
    elif(n=='3'):
        TextDecode()
    elif(n=='4'):
        ImageDecode()
    elif(n=='5'):
        break  
    else:
        print("Invalid input")  
    system('cls')        