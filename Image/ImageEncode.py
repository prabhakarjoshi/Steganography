from tkinter import Tk, filedialog
import cv2
import msvcrt

def ImageEncode():  

    def edit_image(): 
        tmp=0
        for i in range(rows):
            for j in range(cols):
                for k in range(wid):


                    if binary_message[tmp]=='0':
                        if img[i][j][k]%2!=0:
                            img[i][j][k]+=1
                    elif(binary_message[tmp]=='1'):
                        if img[i][j][k]%2==0:
                            img[i][j][k]+=1

                    tmp+=1
                    if tmp>=len(binary_message):
                        return                


    msg=input("Enter the message:")
    binary_message= '0'.join(format(ord(i), '08b') for i in msg)+'1'
    
    root=Tk()
    name=filedialog.askopenfilename(title='Select tmphe image') 
    root.withdraw()
    img = cv2.imread(name, 1)
    rows,cols,wid= img.shape[0],img.shape[1],img.shape[2]

    if len(binary_message) >rows*cols*wid:
        print("Size of image is small compared tmpo message")
        exit()

    edit_image()

    cv2.imwrite('Data/Sample.bmp',img) 
    print("\n----------Encoded Successfully----------\n")
    print("press any key to continue")
    msvcrt.getch()