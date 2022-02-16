i=1
num=int(input("Please enter the total:"))
f=open("numbers.txt","a")
while i <= num:
    f.write("{}\n".format(i))
    i=i+1

f.close()
print("Numbers were written.")
