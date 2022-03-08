# name = "Giorgi"

# print(name[1])

# print(len(name))

# #შევამოწმოთ არის თუ არა რაიმე ასო ამ ჩვენს სახელში
# print("l" in name)

# #slicing
# surname = "Tsertsvadze"
# print(surname[2:5])
# print(surname[:2])

# #negative index
# print(surname[-6])

name = "nugzari"
surname = "dzagnidze"
my_taxt = " i am so {} "
my_taxt2 = "i am so {}"

print(name[2:5])
print(surname[:4])
print(len(name))
print(len(surname))

if (name.endswith ("shvili")):
    print(my_taxt.format("happy"))
else:
    print(my_taxt2.format("sad"))
