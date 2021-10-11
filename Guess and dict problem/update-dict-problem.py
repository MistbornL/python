my_dict = {"Name":'Lasha', 'Age': 21, }

while True:
    key_input = input("Enter Key: ")
    if key_input in my_dict.keys():
        update = input("Enter new Key to update Value: ")
        if update.isdigit():
            my_dict[key_input] = int(update)
            print(my_dict) 
            break
        else:
            my_dict[key_input] = update 
            print(my_dict)
            break  

    else:
        value = input("Enter value: ")
        if value.isdigit():
            my_dict[key_input] = int(value)
        else:
            my_dict[key_input] = value    
        print(my_dict)
        break