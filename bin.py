def int_bin(value:str , bits: int):
    if not value.isdigit():
        raise Exception("Invalid Number")
    
    int_value = int(value)
    bin_text = bin(int_value).replace("0b", "")

    while len(bin_text) < bits:
        bin_text = '0' + bin_text

    return bin_text

def encrypt(string: str, bits: int):
    chars = "abcdefghijklmnopqrstuvwxyz"
    
    encrypted = []
    for c in string.replace(" ", ""):
        if c in chars:
            for i in str(chars.index(c)):
                encrypted.append(int_bin(i, bits))
        elif c.isdigit():
            encrypted.append(int_bin(c, bits))
        else:
            encrypted.append('0'*bits)
        
    return "".join(encrypted)

print(encrypt("teste 123 444 aaasfsadfsd bom dia!!!!", 4))