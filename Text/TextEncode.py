
import msvcrt
from Text.FileReader import FileReader
from Text.convert import dec_to_base

def TextEncode():
    ############ CREATING COVER LIST##############
    cover_string_list=FileReader("Cover File")

    ########### ENCRYPTING STEP 1 ###############

    secret_message=input("Enter the message:")
    encrypted_message= ''.join(format(ord(i), '08b') for i in secret_message)


    ########### ENCRYPTING STEP 2 ###############

    primary_key=""
    j=0
    i=0
    if len(encrypted_message) >len(cover_string_list):
        print("error")
        exit()

    for char in encrypted_message:
        while cover_string_list[i][0]==cover_string_list[i][-1]:
            i+=1
        if char=='0':
            primary_key+=cover_string_list[i][0]
        else:
            primary_key+=cover_string_list[i][-1]
        i+=1


    ########### ENCRYPTING STEP 3 ###############

    secondary_key=""
    for i in primary_key:
        secondary_key=secondary_key+str(ord(i))

     ########### ENCRYPTING STEP 4 ###############

    trikey=dec_to_base(int(secondary_key))
    file = open("Data/key.txt",'w')
    file.write(trikey)
    file.close()
    
    print("\n----------Encoded Successfully----------\n")
    print("press any key to continue")
    msvcrt.getch()
