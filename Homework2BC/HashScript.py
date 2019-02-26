import hashlib
import time
import sys
passwords = open("passwords.txt", 'r')
passwords = open("passwords1.txt", 'r')


def hashing():
    start = time.time()
    i = 0
    for line in passwords:
        i += 1
        values = line.split()
        str1 = ''.join(values)
        if hashlib.sha1(str1).hexdigest() == hashInput:
            print("Password was found") #tells if found
            print("Password is: " + str1) #prints the original string password
            print("Number of attempts is:" + str(i)) #prints the line number its found on. The i'th iteration
            print("Time Taken:" + str(time.time() - start))


def hash1(h):
    result = " "
    for line in passwords:
        values = line.split()
        str1 = ''.join(values)
        if hashlib.sha1(str1).hexdigest() == h:
            result = str1
            break
    return result


def leet(w):
    start = time.time()
    i = 0
    for line in passwords:
        i += 1
        values = line.split()
        str1 = ''.join(values)
        m = hashlib.sha1()
        m.update(w+str1)
        if m.hexdigest() == hashInput:
            print(str1)
            print(w+str1 + " is " + hashInput)
            print("Number of attempts is:" + str(i))
            print("Time Taken:" + str(time.time()-start))




if len(sys.argv) > 2:
       hashInput = sys.argv[1]
       word = sys.argv[2]
       leet(hash1(word))
elif len(sys.argv) > 1:
        hashInput = sys.argv[1]
        hashing()



