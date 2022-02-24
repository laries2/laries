range(1,1000)
c=list(range(1,1000))
print(c)
for nums in range(1,1000):
    if nums%2==0:
     print(nums)
name=input('Your Name: ')
print('Hi '+name)

weight=input("Enter your weight in Kgs: ")
convert=int(weight)/10
print("Your weight in Pounds is: " + str(convert))
is_young=False
if is_young:
    print("She is young")
else:
    print("She is old")