from os import error

vaccine = {33:{"COWIN":0,"COVIDSHIELD":0}}
register = {999:["anakha",{"COWIN":0,"COVIDSHIELD":0}]}

def registation(name,phone,vax,pin):

    if phone not in register.keys():
        register.update({phone:[name,{"COWIN":0,"COVIDSHIELD":0}]})
    temp = register[phone][1]
    if vax == 1:
        if temp['COWIN'] <2:
            vaxins = vaccine[pin]
            if vaxins['COWIN'] <=0:
                print("no slotes are currently available .please wait or try with another PIN")
                reg()
            temp['COWIN'] = temp['COWIN'] +1
            print("-- slot added --")
            vaxins['COWIN'] -= 1
        else:
            print("only vaccine 2 vaccines are alowed for 1 phone number")
            start_menu()
    elif vax==2:
        if temp['COVIDSHIELD'] <2:
            vaxins = vaccine[pin]
            if vaxins['COVIDSHIELD'] <=0:
                print("no slotes are currently available .please wait or try with another PIN")
                reg()
            temp['COVIDSHIELD'] +=1
            print("-- slot added --")
            vaxins['COVIDSHIELD'] -= 1
        else:
            print("only vaccine 2 vaccines are alowed for 1 phone number")
            start_menu()
    start_menu()

def reg():
    pin = int(input("enter pincode: "))
    if pin not in vaccine.keys():
        print("sorry, no vaccines are available in this PIN")
        print("")
        start_menu()
    name = input("enter name: ")
    phone = int(input("enter phone: "))

    temp = vaccine[pin]
    print("")
    print("vaccine availability")
    print(1,"COWIN            "+ str(temp['COWIN']))
    print(2,"COVIDSHIELD      "+ str(temp['COVIDSHIELD']))
    vax = int(input("choose from above: "))
    registation(name,phone,vax,pin)

def vaccin(name,number,pin):
    if pin not in vaccine.keys():
        vaccine.update({pin:{"COWIN":0,"COVIDSHIELD":0}})
    temp = vaccine[pin]
    if name == 1:
        temp['COWIN'] += number
    else:
        temp["COVIDSHIELD"] += number
    print("--  added successfully --")
    start_menu()


def add_vaccine():
    print("select vaccine for adding")
    print("1. COWIN")
    print("2. COVIDSHIELD")
    try:
        name = int(input("choose vaccine: "))
        number = int(input("no.of vaccine: "))
        pin = int(input("enter pincode: "))

        vaccin(name,number,pin)
    except:
        print("invalid input addvaccine in this pincode")

def start_menu():
    print("1. admin pannel")
    print("2. register for vaccine")
    print("3. End")
    try:
        x = int(input("Choose from above: "))
        print("########welcome########")
        if x == 1:
            add_vaccine()
        elif x == 2:
            reg()
        elif x == 100:
            print("vaccine: ",vaccine)
            print("register: ",register)
            start_menu()
        else:
            print(" thank you ")
            return None
    except:
        print("invalid input")
        start_menu()

def start():
    print("#################")
    print(" ---vaccination--- ")
    print("")
    start_menu()
    print("#################")

start()