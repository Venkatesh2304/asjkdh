def dec_to_base(num,base):  #Maximum base - 36
    base_num = ""
    while num>0:
        dig = int(num%base)
        if dig<10:
            base_num += str(dig)
        else:
            base_num += chr(ord('A')+dig-10)  #Using uppercase letters
        num //= base

    base_num = base_num[::-1]  #To reverse the string
    return base_num

def binary_to_octal(binary):
    binary = "".join(binary)
    zeros = len(binary) - len(binary.lstrip('0'))
    x = dec_to_base(int(binary, 2), 4) 
    x = "".join( [ str(int(i)*3) for i in x ] ) 
    if x != "0" : octal = "0"*zeros + x  #.zfill(len(binary)//3*3)
    else : octal = "0"*zeros 
    return [ int(i) for i in octal ] 

def octal_to_binary(octal):
    octal = "".join(octal)
    zeros = len(octal) - len(octal.lstrip('0'))
    d = [0,0,1,1,1,2,2,2,3,3,3]
    x = [ str( d[int(i)] )  for i in octal ]
    x = format(int( "".join(x), 4), 'b')
    if x != "0" : binary = "0"*zeros + x #.zfill(len(octal)*3)
    else : binary = "0"*zeros
    return binary

#binary_to_octal("0000101")
#octal_to_binary(x)
