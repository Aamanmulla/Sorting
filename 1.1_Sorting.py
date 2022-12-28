lst_1=[]
lst_2=[]
n=int(input("Enter the number of subjects:"))
for i in range(0,n):
    subject=str(input("Enter name of subject: "))
    lst_1.append(subject)
    score=int(input("Enter the score: "))
    lst_2.append(score)

# print(lst_1)
# print(lst_2)
data= list(zip(lst_1,lst_2))
print("\nInput:\n",data,"\n")
data.sort(key=lambda a:a[1])
print("\nOutput:\n",data,"\n")