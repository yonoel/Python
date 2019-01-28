def fn():
   try:
       return 1
   finally:
       return 2

# print(fn())
# print (4.5//2)
import random
# print (random.seed(3))
for i in range(1, 5):
 print(str(i) * 5)

var1 = True
var2 = False
var3 = False

if var1 or var2 and var3:
    print("True")
else:
    print("False")

for i in range(1,6):
    print (++i)