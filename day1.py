laptops = int(input ("Enter the number of laptops: "))
mens = int(input ("Enter the number of mens: "))
tables = int(input ("Enter the number of tables: "))
while(laptops!=0 and mens!=0 and tables!=0):
    print("The company wants:")
    l=int(input("Enter number of laptops needed by company:"))
    m=int(input("Enter number of mens needed by company:"))
    t=int(input("Enter number of tables needed by company:"))  
    if(l<=laptops):
        print("The %d number of laptops are allocated to the company." %(l))
        laptops = laptops - l;
    else:
        print("The demand of the company cannot be fullfilled.")   
    if(m<=mens):
        print("The %d number of mens are allocated to the company." %(m))
        mens = mens - m;
    else:
        print("The demand of the company cannot be fullfilled.") 
    if(t<=tables):
        print("The %d number of tables are allocated to the company." %(t))
        tables = tables - t;
    else:
        print("The demand of the company cannot be fullfilled.") 
print("The remaining number of laptops are %d, mens are %d and tables are %d." %(laptops,mens,tables))        


students = {
    "name" : "Aarya Gupta",
    "age" : 20,
    "major" : "Biotechnology",
}

print("Name:",students["name"])
print("Age:",students["age"])
print("Major:",students["major"])

students["age"] = 21 
print("Updated Dictionary:",students)


data = [1,2,3,4,5]
data.append(6)
data.remove(3)
print(data)

import numpy as np
arr = np.array([1,2,3,4,5])
squared = arr**2
mean = np.mean(arr)
print("Squared:",squared)
print("Mean:",mean)


with open("data.txt","r") as file:
    data = file.read()
    processed_data = data.upper()
with open("processed_data.txt", "w") as file:
    file.write(processed_data)
    print("File processing completed.")