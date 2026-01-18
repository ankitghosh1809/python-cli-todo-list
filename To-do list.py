def adding_tasks():
    global a
    a=[]
    while True:
        b=input("Enter the task you want to do: ")
        if b == " ":
            print("Invalid Input")
            print("Enter A task")
            break
        a.append(b.upper())
        c=input("Do you want to add more tasks(Yes/No): ")
        if c.upper()=="NO":
            print ("Your to-do list is")
            print(a)
            print ()
            break
        elif c.upper() not in ("YES","NO"):
            print ("Invalid Input")
            print ("Your to-do list is")
            print (a)
            print ()
            break
def completing_taks():
    if a==[]:
        print ("You have no tasks in your to-do list")
        return
    while True:
        d=input("Enter The Task you have completed from the To-do list: ")
        if d.upper() in a:
            a.remove(d.upper())
            if a==[]:
                print ("All tasks Completed")
                break
            else:
                print("Tasks left")
                print(a)
                e=input("Have you completed any more tasks(Yes/No): ")
                if e.upper()=="NO":
                    print("Tasks left")
                    print(a)
                    break
                elif e.upper() not in ("YES","NO"):
                    print ("Invalid Input")
                    break
        else:
            print("Entered Task not in the to do list")
adding_tasks()
completing_taks()
    
