import datetime

#function to get the date
def get_date():
    return datetime.datetime.now()


#function to get name and choice
def get_choice():
    global choice2,name
    name=input(("What is your name?\nAaron(1)?\nBle(2)?\nPawan(3)?\n")).lower()
    choice2= input("Press 1 for excercise\nPress 2 for food:\n")


#function to write the files
def Log():
    if name=='1' and choice2=='1':
        value=input('Type here: ')
        with open('aaron_ex.txt') as a:
            a.write(str([str(get_date())])+':'+value+'\n')
        print('Sucessfully written')
    elif name=='1' and choice2=='2':
        value= input('Type here: ')
        with open('aaron_f.txt') as a:
            a.write(str([str(get_date())])+':'+ value+'\n')
        print('Sucessfully written')
    elif name=='2' and choice2=='1':
        value= input('Type here: ')
        with open('ble_ex.txt') as b:
            b.write(str([str(get_date())])+ ':'+ value+'\n')
        print('Sucessfully written')
    elif name=='2' and choice2=='2':
        value= input('Type here: ')
        with open('ble_f.txt') as b:
            b.write(str([str(get_date())])+ ':'+ value+'\n')
        print('Sucessfully written')
    elif name=='3' and choice2=='1':
        value= input('Type here: ')
        with open('pawan_ex.txt') as p:
            p.write(str([str(get_date())])+ ':'+ value+'\n')
        print('Sucessfully written')
    elif name=='3' and choice2=='2':
        value= input('Type here: ')
        with open('pawan_f.txt') as p:
            p.write(str([str(get_date())])+ ':'+ value+'\n')
        print('Sucessfully written')
    else:
        print ('Sorry invalid input ')


#fuction to see the files
def retrieve():
    if name=='1' and choice2=='1':
        with open('aaron_ex.txt') as a:
            for i in a:
                print(i,end=' ')
    elif name=='1' and choice2=='2':
        with open('aaron_f.txt') as a:
            for i in a:
                print(i,end=' ')
    elif name=='2' and choice2=='1':
        with open('ble_ex.txt') as b:
            for i in b:
                print(i,end=' ')
    elif name=='2' and choice2=='2':
        with open('ble_f.txt') as b:
            for i in b:
                print(i,end=' ')
    elif name=='3' and choice2=='1':
        with open('pawan_ex.txt') as p:
            for i in p:
                print(i,end=' ')
    elif name=='3' and choice2=='2':
        with open('pawan_f.txt') as p:
            for i in p:
                print(i,end=' ')
    else :
        print("Wrong input ")


#main method       
choice = input("Press 1 to write in the logs\nPress 2 to retrieve data:\n")
if choice=='1':
    get_choice()
    Log()
    c=input(('Do you want to continue? Yes or No : ')).lower()
    #we need to ask again and again so while loop
    while c=='yes':
        get_choice()
        retrieve()
        c=input(('Do you still want to coninue? Yes or No: ')).lower()
    while c=='no':
        exit()
elif choice=='2':
    get_choice()
    retrieve()
    c=input(('Do you want to continue? Yes or No: ')).lower()
    #we need to ask again and again so whiile loop
    while c=='yes':
        get_choice()
        retrieve()
        c=input(('Do you still want to coninue? Yes or No: ')).lower()
    while c=='no':
        exit()