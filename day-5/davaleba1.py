
# #ფუნქციის გრაფიკი y=2
# def route(x,y):
#     if y == 2:
#          return True
#     else:
#          return False
    
# x = int(input("enter the x coordinate: "))
# y = int(input("enter the y coordinate: "))

# print(route(x, y))

def divide(arr):
    my_sum = 0
    for element in  arr:
        my_sum += element
    
    return my_sum/len(arr)

arr = []
ammount_of_numbers = int(input("შეიყვანეთ რამდენი რიცხვის შეყვანა გსურთ: "))
for i in range(ammount_of_numbers):
    num = int(input("enter num" + str(i+1) + ":"))
    arr.append(num)
    
print(divide(arr))

    



