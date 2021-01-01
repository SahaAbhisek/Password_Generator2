import random
import string

s1=string.ascii_lowercase
s2=string.ascii_uppercase
s3=string.digits
s4=string.punctuation

s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))

# One can either shuffle the list s first and take the first plen characters
# or one can just choose plen numbers randomly from the sample s

#random.shuffle(s)

plen=int(input("Enter your password length:\n"))

print("Your password is:")
#print(''.join(s[0:plen]))
print(''.join(random.sample(s,plen)))