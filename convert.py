def textToBinary(data):
    print("Converting text to binary...")
    data_prime = ''.join(format(i, 'b') for i in bytearray(data, encoding = 'utf-8'))
    # print(data_prime)
    return data_prime