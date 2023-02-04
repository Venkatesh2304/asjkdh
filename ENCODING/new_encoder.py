original_msg = input()
msg_in_bits = [int(i) for i in original_msg]
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
print(encode_msg)