
def decoder(msg_in_bits):
    msg_len = len(msg_in_bits)
               
    error_bit = []

    curr_power = 1
    for i in range(1,msg_len+1):
        if i == curr_power:
            curr_power = curr_power*2        
            r = 0
            for j in range(0,msg_len-i+1):
                q = msg_len - j            
                if q % (2*i) >= i:
                    r += msg_in_bits[j]        
            error_bit.append(r % 2)

    err_bit_num = 0
    new_power = 1
    for i in range(len(error_bit)):
        err_bit_num += new_power*error_bit[i]
        new_power = new_power*2

    err_bit_index = msg_len - err_bit_num
    if err_bit_index != msg_len:
        error_detect = True
        msg_in_bits[err_bit_index] = 1-msg_in_bits[err_bit_index]

    final_power = 1
    decode_msg = []
    for i in range(1,msg_len+1):
        if i != final_power:
            decode_msg = [msg_in_bits[msg_len-i]] + decode_msg
        else:
            final_power = 2*final_power  
    return decode_msg  


received_msg = input()
msg_in_bits = [int(i) for i in received_msg]
decode_msg = decoder(msg_in_bits)
decode_msg1_len = [i for i in decode_msg[:5]]

# print(msg1_len_bi)
# decode_msg1_len = decoder(msg1_len_bi)
# print(decode_msg1_len)

msg1_len = 0
p = 1
for i in range(0,len(decode_msg1_len)):
    msg1_len += p*decode_msg1_len[i]
    p = p*2
# print(msg1_len)

msg1 = [i for i in decode_msg[5:(5+msg1_len)]]
print(msg1)

msg2 = [i for i in decode_msg[(5+msg1_len):]]
print(msg2)