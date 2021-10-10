import hashlib

hash = ''
nonce = 1
key = 'bgvyzdsv'

while hash[:6] != '000000':
    nonce += 1
    check = key+str(nonce)
    hash = hashlib.md5(check.encode('utf-8')).hexdigest()
    #print(hash)

print(nonce)

