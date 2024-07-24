import random
import string
length = int(input("Enter the expected length of your password: "))
while length<=0:
    print("Kindly enter a positive integer greater than zero..")
characters = string.ascii_letters + string.digits + string.punctuation
passw = random.sample(characters,length)
mainpass = ''.join(passw)
print(f"Generated password of length{(length)}:{mainpass}")
