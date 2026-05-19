tasks =[]

while True:
    print("=====TO DO APP====")
    print("1.ADD task")
    print("2.View task")
    print("3.Delete task")
    print("4.exit")

    choice = input("Enter choice: ")

    if choice == '1':
        task = input('Enter task: ')
        tasks.append(task)
        print('Task added')

    elif choice == '2':
        print('\nYour task')
        for i,t in enumerate(tasks):
            print(f"{i+1}.{t}")
    
    elif choice =='3':
        try:
            index = int(input('Enter task number to delete: '))
            if 0<index<=len(tasks):
                removed = tasks.pop(index-1)
                print(f"Deleted: {removed}")
            else:
                print('Invalid task number')
            
        except ValueError:
            print("Please valid task number")

    elif choice == '4':
        print('Exiting...')
        break
    
    else:
        print('Invalid option')
