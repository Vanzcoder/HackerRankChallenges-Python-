if __name__ == '__main__':
    N = int(input("Please enter the number of commands: "))
    list1 = []
    for i in range(N):
        command = input("Enter (remove, insert, append, sort, pop, reverse or print), then position (if needed), then value: ")
        command = command.split()
        if command[0] == "remove":
            list1.remove(int(command[1]))
        elif command[0] == "insert":
            list1.insert(int(command[1]), int(command[2]))
        elif command[0] == "append":
            list1.append(int(command[1]))
        elif command[0] == "sort": #doesn't take #, just sorts from least to greatest
            list1.sort()
        elif command[0] == "pop": #doesn't take #, just removes last
            list1.pop()
        elif command[0] == "reverse":
            list1.reverse()
        elif command[0] == "print":
            print(list1)
        else: 
            print ("I DON\'T KNOW WHAT YOUR SAYING!")
            i += 1 # if you make a typo, this would give you a second chance
