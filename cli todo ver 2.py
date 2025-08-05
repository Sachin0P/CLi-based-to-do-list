import os

print("Welcome to CLI ToDo")
if not os.path.isfile("todo.txt"):
    fl=open('todo.txt','w')
    fl.close()

if not os.path.isfile("done.txt"):
    fl=open('done.txt','w')
    fl.close()

fl=open('todo.txt','r')
A=[]
for line in fl:
    A.append(line.strip())

fl.close()
fl=open('done.txt','r')
B=[]
for line in fl:
    B.append(line.strip())
fl.close()

print('what shall we do')
o=int(input("1.View the list\n2.Add tasks to the list\n3.Check a task as done\n4.Clear the whole list\n"))
if o==1:
    print("\n\nthe todo list")
    for i in A:
        print(i)
elif o==2:
    while True:
        s=input("Enter the task entre DONE when completed\n")
        if s=="DONE":break
        A.append(s)
        print("\n\nToDo")
        for i in A:
            print(i )
elif o==3:
    for i in A:
        print(i)
    n=int(input("\n\nNumeric value of the task which is to be checked: "))
    t=A[n-1]
    B.append(t)
    A.pop(n-1)
    print("\n\nToDo")
    for i in A:
        print(i)
    print("\n\nDone")
    for i in B:
        print(i)
elif o==4:
    A.clear()
    B.clear()
else:
    print("Invalid option")

fl=open("todo.txt",'w')
for i in A:
    fl.write(i+"\n")
fl.close()
fl=open("done.txt",'w')
for i in B:
    fl.write(i+"\n")
fl.close()



