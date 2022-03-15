#ალგორითმი რაის ამოცანის ამოხსნისთვის საჭირო პროცედურების მიმდევრობა

#ფუნქცია არის ალგორითმი რომელსაც აქვს კონკრეტული სახელი და არის გამოყენებადი
#resuable
#გამოძახებადი 
#იმით გამოირჩევა რომ შეგვიძლია მობვაგვაროთ სხვადასხვა არგუმენტებს 

#გავიარეთ ეს ფუნქციები:
#print
#input

# def Hello(name):
#     print("Hello" + name)
    
# Hello(" Cercva ")


# def multyply(a, b):
#     return a * b

# print(multyply(5, 10))


# def ricxvebi(a, b, c):
#     sum = 0
#     for i in range(len(a, b, c)):
#         sum += a, b, c[i]
        
#     return sum/len(a, b, c)
    
    
   

 
# def my_mean(arr):
#     my_sum = 0
#     for element in arr:
#         my_sum += element

#     return my_sum/len(arr)



arr = []
ammount_of_numbers = int(input("შეიყვანეთ რამდენი რიცხვის შეყვანა გსურთ: "))

for i in range(ammount_of_numbers):
    x = int(input("შეიყვანეთ რიცხვი " + str(i+1) + " სიისთვის: "))
    arr.append(x)


print(my_mean(arr))