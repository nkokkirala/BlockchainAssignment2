import hashlib
import sys
passwords = open("passwords.txt", 'r')
passwords1 = open("passwords.txt", 'r')


passwordDictionary = {

}


for line in passwords:
    values = line.split()
    str = ''.join(values)
    str1 = hashlib.sha1(str).hexdigest()
    passwordDictionary[str1] = str


def hashing():

    hashInput = sys.argv[1]
    print(passwordDictionary[hashInput])




hashing()
