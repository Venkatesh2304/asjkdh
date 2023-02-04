def binary_to_octal(binary):
    binary = "".join(binary)
    zeros = len(binary) - len(binary.lstrip('0'))
    octal = "0"*zeros +  format(int(binary, 2), 'o')#.zfill(len(binary)//3*3)
    return [ int(i) for i in octal ] 

def octal_to_binary(octal):
    octal = "".join(octal)
    zeros = len(octal) - len(octal.lstrip('0'))
    binary = "0"*zeros + format(int(octal, 8), 'b')#.zfill(len(octal)*3)
    return binary

#binary_to_octal("0000101")
#octal_to_binary(x)
