import msvcrt as m
from Text.FileReader import FileReader
from Text.convert import base_to_dec

def TextDecode():    
    cover_list=FileReader("Cover File")
    trikey=FileReader("Key")

    ########### DECRYPTING STEP 1 ###############
    secondary2_key=base_to_dec(trikey)
    ########### DECRYPTING STEP 2 ###############
    primary2_key=''
    while secondary2_key!=0:
        temp=secondary2_key%100
        secondary2_key=secondary2_key//100
        primary2_key=chr(temp)+primary2_key 
    
    ########### DECRYPTING STEP 3 ###############

    decrypted_msg=''
    i=0
    for char in primary2_key:
        while cover_list[i][0]==cover_list[i][-1]:
            i+=1
        if(cover_list[i][0]==char):
            decrypted_msg+='0'
        else:
            decrypted_msg+='1'    
        i+=1   
    ########### DECRYPTING STEP 4 ###############
    orig_msg=''
    i=0
    while i< len(decrypted_msg):
        orig_msg+= chr(int(decrypted_msg[i:i+8],2))
        i=i+8          
    print("Message:-->",orig_msg)
    print("press any key to continue")
    m.getch()

    
        