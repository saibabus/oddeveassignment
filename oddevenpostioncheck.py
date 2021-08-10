numberis =list(map(int,input()))
evenpostionadd=0
oddpositionadd=0
for i in range(0,len(numberis),2):
    evenpostionadd+=numberis[i]
for i in range(1,len(numberis),2):
    oddpositionadd+=numberis[i]
if evenpostionadd==oddpositionadd:
    print("Yes")
else:
    print("No")