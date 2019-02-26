import hashlib
import sys
print(hashlib.sha1('password' + ' ' + 'password').hexdigest())

#print("Please enter a hash:")
#hashInput = str(sys.argv[1])

hashInput = sys.argv[1]

def space():

    counter1 = 0
    counter2 = 0

    with open("passwords.txt", 'r') as passwords:
        for line in passwords:
            counter1 += 1
            with open("passwords1.txt", 'r') as passwords1:
                for line2 in passwords1:
                    counter2 +=1
                    values = line.split()  # convert to string array
                    str1 = ''.join(values)  # covert to string
                    m = hashlib.sha1()  # initialize hash
                    value = line2.split()  # covert to string array
                    str2 = ''.join(value)  # convert to string
                    m.update(str1 + ' ' + str2)  # m is now a hash of str1 plus a space plus str2(a line from passwords1)
                    #print("counter1 " + str(counter1))
                    #print("counter2 " + str(counter2))
                    if m.hexdigest() == hashInput:  # checks if hash of str1+ " " + str2 equals hashInput
                            print("found")  # if so, print str1 and str2
                            print(str1 + ' ' + str2)

space()


print(passwordDictionary[hashInput])