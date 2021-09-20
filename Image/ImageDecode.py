from tkinter import Tk, filedialog
import cv2
import msvcrt


def ImageDecode():
    
    root=Tk()
    name=filedialog.askopenfilename(title='Select the image') 
    root.withdraw()
    img = cv2.imread(name, 1)
    rows,cols,wid= img.shape

    ################ Image to binary message  ##################


    
    def getmsg():
        new=''
        tmp=0
        for i in range(rows):
            for j in range(cols):
                for k in range(wid):

                    if tmp!=0 and (tmp+1)%9==0:
                        if img[i][j][k]%2!=0:
                            return new
                    elif img[i][j][k]%2==0:
                        new +='0'
                    else:    
                        new+='1'
                    tmp+=1

    binary_message=getmsg()

############ Binary to Original Message  ############

    orig_message=''
    i=0
    while i< len(binary_message):
        orig_message+= chr(int(binary_message[i:i+8],2))
        i=i+8          
    print("Message:-->",orig_message)
    print("\n----------Decoded Successfully----------\n")
    print("press any key to continue")
    msvcrt.getch()