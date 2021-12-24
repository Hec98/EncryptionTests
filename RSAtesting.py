from rsa import newkeys, encrypt, decrypt
from rsa.key import PublicKey, PrivateKey
  
# generate public and private keys with 
# rsa.newkeys method,this method accepts 
# key length as its parameter
# key length should be atleast 16

publicKey, privateKey = newkeys(512)
# print(f'{type(publicKey)}\n{publicKey}\n{privateKey}')

# print(publicKey['n'], publicKey['e'])
# print(privateKey['n'], privateKey['e'], privateKey['d'], privateKey['p'], privateKey['q'])


# PublicKey(n, e)
# PrivateKey(n, e, d, p, q)

# publicKey = PublicKey(int(7735748025422789312465383451065835686830325904843157496450656117421219560759237669371105461992143001983007841221127053688215508672026663744177221356384319), int(65537))

# privateKey = PrivateKey(int(7735748025422789312465383451065835686830325904843157496450656117421219560759237669371105461992143001983007841221127053688215508672026663744177221356384319), int(65537), int(7172006435642676677521234781424405178258044040834568146876395262990840614332539794934841321536033318293166939829360750405038938824482006589529188394519833), int(6414976373245042629181291258134261083991568806979784518438542598546178376224510891), int(1205888778902801916147107848462473842250060704462346702977858057129509309))

# this is the string that we will be encrypting
message = "hello geeks"
  
# rsa.encrypt method is used to encrypt 
# string with public key string should be 
# encode to byte string before encryption 
# with encode method
encMessage = encrypt(message.encode('utf8'), publicKey)

encMessageJ = {
    'enc': encMessage
}

#print(message)
  
print("original string: ", encMessageJ['enc'])
print("encrypted string: ", encMessage)
  
# the encrypted message can be decrypted 
# with ras.decrypt method and private key
# decrypt method returns encoded byte string,
# use decode method to convert it to string
# public key cannot be used for decryption
decMessage = decrypt(encMessageJ['enc'], privateKey).decode('utf8')
  
print("decrypted string: ", decMessage)
