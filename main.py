# Q1. Create one variable containing following type of data:
a = "Suraj"
l = [1, 2, 3, 4, 5, "Suraj", "Sarate", 1.5, False]
f = 1.100
t = ("Suraj", "Sarate", "Suraj")



# Q2. Given are some following variables containing data:
var1 = ''  # Data type is str
var2 = '[DS, ML, Python]'  # Data type is str
var3 = ['DS', 'ML', 'Python']  # Data type is list
var4 = 1.  # Data type is float



# Q3. Explain the use of the following operators using an example:
# (i) / Use of this operator for Divide 2 operands
# (ii) % Use of this operator for get Modulus (remainder) from 2 operands
# (iii) // This operator will divide the first argument by the second and round the result down to the nearest whole number
# (iv) ** The operator that can be used to perform the exponent arithmetic in Python is



# Q4. Create a list of length 10 of your choice containing multiple types of data. Using for loop print the
# element and its data type.
li = [1, 2, 3, 4, 5, "Suraj", "Sarate", 1.5, False, [5, 4, 3, 2, 1]]

for i in li:
    if type(i) == list:
        for j in i:
            print(j)
    else:
        print(i)



# Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many
# times it can be divisible.

A = 10
B = 3
while A % B == 0:
    count = A // B
    print("The number of times {} is divisible by {} is {}".format(str(A), str(B), str(count)))
    break
else:
    print("A is not divisible by B")



# Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is
# divisible by 3 or not.

li_25 = range(1, 26)
for i in li_25:
    if i % 3 == 0:
        print(i)



# Q7. What do you understand about mutable and immutable data types? Give examples for both showing
# this property.

# Mutable data types can be changed after they are created. This means that you can change the value of a mutable
# object, or add or remove elements from it. Examples of mutable data types in Python include lists, dictionaries,
# and sets.

# Immutable data types cannot be changed after they are created. This means that you cannot change the value of an
# immutable object, or add or remove elements from it. Examples of immutable data types in Python include strings,
# tuples, and numbers.
