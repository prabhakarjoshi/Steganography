from tkinter import Tk,filedialog


def FileReader(str):

    # Read a file
    root=Tk()
    name=filedialog.askopenfilename(title=str) 
    root.withdraw()
    file = open(name, 'r', encoding="utf8")
    content=''
    

    # creating string of the data

    for each in file:
        if each!='\n' :
            content+=each.upper()
    file.close()   
     
    # returning string or list as required

    if str=='Key':
        return content
    return content.split(' ')