sBox = {
    '0000': '1100',
    '0001': '0101',
    '0010': '0110',
    '0011': '1011',
    '0100': '1001',
    '0101': '0000',
    '0110': '1010',
    '0111': '1101',
    '1000': '0011',
    '1001': '1110',
    '1010': '1111',
    '1011': '1000',
    '1100': '0100',
    '1101': '0111',
    '1110': '0001',
    '1111': '0010'
}
keyArr = ['0'] * 32
arrPerm = [0, 16, 32, 48, 1, 17, 33, 49, 2, 18, 34, 50, 3, 19, 35, 51, 4, 20, 36, 52, 5, 21, 37, 53, 6, 22, 38, 54, 7, 23, 39, 55, 8, 24, 40, 56, 9, 25, 41, 57, 10, 26, 42, 58, 11, 27, 43, 59, 12, 28, 44, 60, 13, 29, 45, 61, 14, 30, 46, 62, 15, 31, 47, 63]

def generateRoundKeys(key):
    from0to3 = ''
    global keyArr
    keyArr = ['0'] * 32
    keyArr[0] =  key[:-16]
    curretKey = key
    
    #[1,32)
    for j in range(1, 32):
        #[-19:], [:-19)
        rotated_string = curretKey[-19:] + curretKey[:-19]
        from0to3 = sBox.get(rotated_string[:4])
        from_20to_16 = bin((int(rotated_string[-20:-15], 2) ^ (j)))[2:].zfill(5)
        rotated_string = from0to3 + rotated_string[-76:-20]+ from_20to_16 + rotated_string[-15:]
        curretKey = rotated_string
        keyArr[j] =  rotated_string[:-16]
        
# Two bit strings ener and a number exits
def addRoundKey(state,ki):
    print(hex(int(keyArr[ki], 2))[2:].zfill(16))
    binaryNumberState = int(state, 2)
    binaryNumberKi = int(keyArr[ki], 2)
    #print(bin(binaryNumberState ^ binaryNumberKi)[2:].zfill(64))
    return bin(binaryNumberState ^ binaryNumberKi)[2:].zfill(64)
    

def sBoxLayer(state):
    newChar = ''
    hexString = hex(int(state, 2))[2:].zfill(16)
    for char in hexString:
        newChar =  newChar + sBox.get(bin(int(char, 16))[2:].zfill(4))
    return newChar
        
def pLayer(state):
    my_stringarr = ['a'] * 64
    for i in range(0, 64):
        my_stringarr[arrPerm[i]] = state[i]
    return ''.join(my_stringarr)

def genrateCipherText(plaintext, key):
    print(keyArr)
    currentState = plaintext
    generateRoundKeys(key)
    print(keyArr)
    #[0,32)
    for i in range(0, 31):
        RoundKeyState = addRoundKey(currentState,i)        
        sBoxLayerState = sBoxLayer(RoundKeyState)        
        pLayerState = pLayer(sBoxLayerState)
        currentState = pLayerState
        print('Round: ', i, hex(int(currentState, 2))[2:].zfill(16), 'length: ', len(hex(int(currentState, 2))[2:]) )
    cipherText = addRoundKey(currentState,31)
    return hex(int(cipherText, 2))[2:]

