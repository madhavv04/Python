f = open("e_commerece_using_main.py","r")
d = f.read()
f.close()

# data comes from another file

f1= open("e_commerce_copy.py","w")
f1.write(d)
f1.close()
