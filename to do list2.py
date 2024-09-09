#To-Do list

l1=['Walk','Eat','Study']
while True:
    class tdl:
        def _init_(self,n):
            self.n=n
        
        def display(self):
            print("To Do List: ")
            for i, task in enumerate(l1):
               print((i+1),task)
            print("\n")
               
        def add(self,ad):
            self.ad=ad
            l1.append(ad)
            print("Task Added Successfully\n")
        
        def delete(self,dell):
            self.dell=dell
            sm=dell-1
            l1.pop(sm)
            print("Task Deleted Successfully\n")
        
    print("1.Add Task\n2.Delete Task\n3.Display Tasks\n4.Exit")
    n=int(input("Enter your choice : "))   
    s1=tdl()
    if n==1:
        a=input("Enter task to add: ")
        s1.add(a)
    elif n==2:
        b=int(input("Enter task number to delete: "))
        s1.delete(b)
    elif n==3:
        s1.display()
    elif n==4:
        print("Be disciplined")
        break
    else:
        print("Please Enter Valid Input !!!\n")






