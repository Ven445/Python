import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers =['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']
password = int(input("Enter desired number of letters?\n"))
symbol = int(input("Enter desired number of symbols?\n"))
number = int(input('Enter desired number of numbers?\n'))   
pwd_list = []
for char in range(0,password):
    pwd_list.append(random.choice(letters))   
for char in range(0,symbol):
    pwd_list.append(random.choice(symbols))       
for char in range(0,number):
    pwd_list.append(random.choice(numbers))
    random.shuffle(pwd_list) 
    pwd = ''.join(pwd_list) 
print("Generated password:",{pwd})      
