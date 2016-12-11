import pickle
# open the file in write mode (w)
phonebook_dict = {}
myfile = open('phonebook.pickle', 'w')
# dump the contents of the phonebook_dict into myfile - the open file
pickle.dump(phonebook_dict, myfile)
# close myfile
myfile.close()
# open the file in read mode (r)
myfile = open('phonebook.pickle', 'r')
# load the contents from the file and store it in the phonebook_dict variable
phonebook_dict = pickle.load(myfile)

def contacts():
    print('1. Look up an entry')
    print('2. Set an entry')
    print('3. Delete an entry')
    print('4. List all entries')
    print('5. Quit')
    choice = int(raw_input('What do you want to do (1-5)? '))

    while choice != 5:

        if choice == 1:
            per_name = raw_input("What is the person's name?: ")
            print phonebook_dict[per_name]
            contacts()

        elif choice == 2:
            per_name = raw_input("Enter the person's name: ")
            per_number = raw_input("Enter the person's number: ")
            extra_numbers = raw_input("Would you like to add additional numbers? (Yes or No) ")

            if extra_numbers == "Yes":
                print('1. Enter a cell phone number: ')
                print('2. Enter the home number: ')
                print('3. Enter the work number: ')
                choice = int(raw_input('What do you want to do (1-3)? '))
                if choice == 1:
                    cell_number = raw_input("Enter the cell number: ")
                    phonebook_dict[per_name] = per_number, cell_number
                    return phonebook_dict

                elif choice == 2:
                    home_number = raw_input("Enter the home number: ")
                    phonebook_dict[per_name] = per_number, home_number
                    return phonebook_dict

                elif choice == 3:
                    work_number = raw_input("Enter the work number: ")
                    phonebook_dict[per_name] = per_number, work_number
                    return phonebook_dict

            phonebook_dict[per_name] = per_number
            contacts()

        elif choice == 3:
            per_name = raw_input("Enter the person's name you want to delete: ")
            del phonebook_dict[per_name]
            contacts()

        elif choice == 4:
            entries = phonebook_dict.items()
            print entries
            contacts()
        else:
            break

contacts()
