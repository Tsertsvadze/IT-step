
#რიცხვების დაჯამება
def num(x):
     my_num = 0 
     for i in range(x):
           my_num += i
     return my_num

print(num(5))


#გაგება რამდენი "x" ასოა სიტყვაში
def word(anything):
    word = anything.count("i")
    return word
print(word("apple"))