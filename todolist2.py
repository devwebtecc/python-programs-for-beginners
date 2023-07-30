user_input = input('random')
data =[]


def show_menu():
    print('1. add an item')
    print('2. add an  dpne')
    print('3. add an  view')
    print('4. exit')



while user_input != '4':
    user_input = input('enter your choice :')


    if user_input =='1':
       item =input('what is to be done')
       data.apped(item)
        print('added item' item) 
    elif user_input=='2':
       print('mark as done')
    elif user_input=='3':
        for item in data:
           print(item)
    elif user_input=='4': 

        print('good by!')
    else:
        print('please enter your  choise 1,2,3 or 4')

