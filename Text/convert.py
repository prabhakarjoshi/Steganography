############# covert from decimal to base =36 #################

def dec_to_base(num):  
    base_num = ""
    while num>0:
        dig = int(num%36)
        if dig<10:
            base_num += str(dig)
        else:
            base_num += chr(ord('A')+dig-10)  
        num //= 36

    base_num = base_num[::-1]  #reverse the string
    return base_num


############# covert from 36 base to any decimal #################

def base_to_dec(num_str):
    num_str = num_str[::-1]
    num = 0
    for k in range(len(num_str)):
        dig = num_str[k]
        if dig.isdigit():
            dig = int(dig)
        else:  
            dig = ord(dig.upper())-ord('A')+10
        num += dig*(36**k)
    return num