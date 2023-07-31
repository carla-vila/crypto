
from presentCipher import genrateCipherText, generateRoundKeys, addRoundKey, sBoxLayer

def callPresentCipher():
    print('ANSWER', genrateCipherText('00'*32, '0'*80))
    print(bin(3 ^ 5)[2:].zfill(5))
    #generateRoundKeys('01'*80)
    #print(addRoundKey('101', '110'))

def test1():
    #string = '12345678998765432112345'
    #string2 = string[-5:-2]
    #print(string2)
    generateRoundKeys('0'*80)
    
#test1()
callPresentCipher()

       