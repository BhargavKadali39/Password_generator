# pip install cowsay

import cowsay
import string as s
from random import *

n=int(input("Enter length of password :\n->"))

if(n<8):
    print('Min of 8 characters are must for a secure password\ndefault value 8 is assigned\n')
    n=8


cond = str(input('Do u want to include special symbols in your passcode. \n type "y/n"\n->').lower())

ch = s.ascii_letters + s.digits

if cond == 'y':
    ch = ch + s.punctuation
    
passw = "".join(choice(ch)for x in range(0,n))

cowsay.tux(passw)
