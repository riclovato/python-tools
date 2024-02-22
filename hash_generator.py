import hashlib

string = input('Insert a string to create a hash: ')

menu = int(input('''#### Menu - HASH TYPE: ####
                1) MD5
                2) SHA1
                3) SHA256
                4) SHA512
                Type the number of the hash type: '''))

if menu ==1:
        result = hashlib.md5(string.encode('utf-8'))
        print(f'String: {string} \nHash MD5: {result.hexdigest()}' )
elif menu ==2:
         result = hashlib.sha1(string.encode('utf-8'))
         print(f'String: {string} \nHash SHA1: {result.hexdigest()}')
elif menu ==3:
         result = hashlib.sha256(string.encode('utf-8'))
         print(f'String: {string} \nHash SHA256: {result.hexdigest()}')
elif menu ==4:
         result = hashlib.sha512(string.encode('utf-8'))
         print(f'String: {string} \nHash SHA512: {result.hexdigest()}')
else:
        print('Something went wrong. Try again.')