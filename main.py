import string
import random
if __name__ == "__main__":
    s1 = string.ascii_lowercase
    #print(s1)
    s2 = string.ascii_uppercase
    #print(s2)
    s3 = string.ascii_letters
    #print(s3)
    s4 = string.punctuation
    #print(s4)
    s5 = string.digits

    plen = int(input("Enter Password lenght\n"))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    s.extend(list(s5))

    #print(s)
    random.shuffle(s)
    #print(s)
    print("Your Password is : ")
    print("".join(s[0:plen]))

