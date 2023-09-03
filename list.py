marks = [3, 5, 6, "Kanye", True]

print(marks[-3])
print(marks[len(marks) - 3])


if "6" in marks:
    print("Yes")
else:
    print("No")


lst = [ i for i in range(4)]

print(lst)

# tuple 
# tuple is  not mutable 

tup = (1, 5 , 6)

print(tup[0])


tuple1 = (0,1, 2, 21 ,2, 3, 1, 3, 2, 3)

res = tuple1.index(3, 4, 8)
print('Count of 3 in tuple is' , res)
