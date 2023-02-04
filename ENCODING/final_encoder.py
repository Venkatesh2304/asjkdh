def encoder(msg_in_bits):
    msg_len = len(msg_in_bits)
    encode_msg = []
    encode_msg_len = 0

    k = 0
    curr_power = 1
    while k < msg_len:
        encode_msg_len += 1
        if encode_msg_len == curr_power:       
            encode_msg = [' '] + encode_msg     
            curr_power = curr_power*2   
        else:
            encode_msg = [msg_in_bits[msg_len-k-1]] + encode_msg
            k += 1

    p=0
    L = len(encode_msg)
    while p<L:    
        if encode_msg[p] == ' ':
            r=0
            q = L-p
            for i in range(0,p):
                if (L-i) % (2*q) >= q:
                    r += encode_msg[i]
            encode_msg[p] = r % 2    
        p += 1

    return(encode_msg)

original_msg = input()
original_msg = original_msg.split()
msg1_in_bits = [int(i) for i in original_msg[0]]
msg2_in_bits = [int(i) for i in original_msg[1]]

# encoded_msg1 = encoder(msg1_in_bits)
# encoded_msg2 = encoder(msg2_in_bits)

# print(encoded_msg1,encoded_msg2)

msg1_len = len(msg1_in_bits)
msg1_len_binary = []
temp = msg1_len
while temp > 0 :
    msg1_len_binary.append(temp % 2)
    temp = temp // 2
# print(msg1_len_binary)

msg1_len_binary += [0]*(5-len(msg1_len_binary))
# print(msg1_len_binary)

# encode_len = encoder(msg1_len_binary)
# print(encode_len)


final_encoded_msg = encoder(msg1_len_binary+msg1_in_bits+msg2_in_bits)
print(final_encoded_msg)
