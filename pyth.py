for i in range(6):
    print(i) 
    if i == 4: 
      break

# else tells when loop completes successfully 
else: 
  print("Sorry on i")


# Exception  handling 

a = input("Enter no")

try:
   for value in range(1, 11):
    print(value * int(a) )
except Exception as e:
    print("Inavlid")

# Finally Clause  ---> while  returning function  

finally: 
    print("AOD")


# Enumerate --> it gives the index  

demo = [12, 13, 41 , 54, 67]

for index , dem  in enumerate(demo):
    print(index)
    if (index == 3):
         print("Hmmm")
