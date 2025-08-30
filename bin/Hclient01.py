# IMPORTS
import os
import time
import random
# LOGO, CREDITS & INITIAL PHRASES
# characters    . ┌ - ┐ | └ ┘
print("┌----┐   ┌----┐")
print("|....|   |....|")
print("|....│   |....|c")
print("|....│   |....|l                                    by MKlabs")
print("|....└---┘....|i                                    devs: MrMaxX, Marcocve")
print("|....┌---┐....|e")
print("|....|   |....|n")
print("|....|   |....|t                                    eula: hclienteula.netlify.app")
print("|....|   |....|")
print("└----┘   └----┘")
print("")
#GREETINGS
print("Welcome to Hclient! please enter your password:")
print('')
#PASSWORD CHECK
password = input()
print('')
if password == 'adminMKlabs':
    print("Hclient loading...")
    print("")
    time.sleep(10)
    print("")
    print('select an option:')
    print("1 = passgen, 2 = btcadressgen, 3 = cardnumbergen, 4 = nmap local ip scan")
    print("")
    usrchoice = input()
    print("")
    # PASSGEN
    if usrchoice == "1":
        print("passgen loading...")
        print("")
        time.sleep(10)
        print("how many passwords do you want to generate?")
        print()
        usrpinput = int(input())
        print("")
        print("press ENTER to execute")
        input()
        print("")
        pgcharacters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890*#_!$%&'
        for i in range(usrpinput): print(
            random.choice(pgcharacters) + random.choice(pgcharacters) + random.choice(pgcharacters) + random.choice(
                pgcharacters) + random.choice(pgcharacters) + random.choice(pgcharacters) + random.choice(
                pgcharacters) + random.choice(pgcharacters) + random.choice(pgcharacters) + random.choice(
                pgcharacters) + random.choice(pgcharacters) + random.choice(pgcharacters) + random.choice(
                pgcharacters) + random.choice(pgcharacters) + random.choice(pgcharacters) + random.choice(
                pgcharacters) + random.choice(pgcharacters) + random.choice(pgcharacters) + random.choice(
                pgcharacters) + random.choice(pgcharacters))
    # BTCADRESSGEN
    if usrchoice == '2':
        print('adressgen loading...')
        print('')
        time.sleep(10)
        print('how many adresses do you want to generate?')
        print('')
        usrainput = int(input())
        print('')
        print('press ENTER to execute')
        input()
        print('')
        btcagcharacters = 'abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ123456789'
        for i in range(usrainput): print(random.choice(btcagcharacters) + random.choice(btcagcharacters) + random.choice(
            btcagcharacters) + random.choice(btcagcharacters) + random.choice(btcagcharacters) + random.choice(
            btcagcharacters) + random.choice(btcagcharacters) + random.choice(btcagcharacters) + random.choice(
            btcagcharacters) + random.choice(btcagcharacters) + random.choice(btcagcharacters) + random.choice(
            btcagcharacters) + random.choice(btcagcharacters) + random.choice(btcagcharacters) + random.choice(
            btcagcharacters) + random.choice(btcagcharacters) + random.choice(btcagcharacters) + random.choice(
            btcagcharacters) + random.choice(btcagcharacters) + random.choice(btcagcharacters) + random.choice(
            btcagcharacters) + random.choice(btcagcharacters) + random.choice(btcagcharacters) + random.choice(
            btcagcharacters) + random.choice(btcagcharacters) + random.choice(btcagcharacters) + random.choice(
            btcagcharacters) + random.choice(btcagcharacters) + random.choice(btcagcharacters) + random.choice(
            btcagcharacters) + random.choice(btcagcharacters) + random.choice(btcagcharacters) + random.choice(
            btcagcharacters) + random.choice(btcagcharacters) + random.choice(btcagcharacters) + random.choice(
            btcagcharacters) + random.choice(btcagcharacters) + random.choice(btcagcharacters) + random.choice(
            btcagcharacters) + random.choice(btcagcharacters) + random.choice(btcagcharacters) + random.choice(
            btcagcharacters) + random.choice(btcagcharacters) + random.choice(btcagcharacters) + random.choice(
            btcagcharacters) + random.choice(btcagcharacters) + random.choice(btcagcharacters) + random.choice(
            btcagcharacters) + random.choice(btcagcharacters) + random.choice(btcagcharacters) + random.choice(
            btcagcharacters) + random.choice(btcagcharacters) + random.choice(btcagcharacters) + random.choice(
            btcagcharacters) + random.choice(btcagcharacters) + random.choice(btcagcharacters) + random.choice(
            btcagcharacters) + random.choice(btcagcharacters) + random.choice(btcagcharacters) + random.choice(
            btcagcharacters) + random.choice(btcagcharacters) + random.choice(btcagcharacters))
    # CARNUMBERGEN
    if usrchoice == "3":
        print("cardnumbergen loading...")
        print("")
        time.sleep(10)
        print("which card do you want to generate?")
        print("")
        print("1 = Visa")
        print("2 = Mastercard")
        print("3 = American Express")
        print("")
        cng = input()
        print("")
        # VISA
        if cng == "1":
            print("VISA")
            vcn1 = random.randint(000, 999)
            vcn2 = random.randint(0000,9999)
            vcn3 = random.randint(0000,9999)
            vcn4 = random.randint(0000,9999)
            vced1 = random.randint(1, 12)
            expyear = "2025", "2026", "2027", "2028", "2029", "2030", "2031"
            vced2 = random.choice(expyear)
            vcvv = random.randint(000, 999)
            print("")
            print("card number: 4" + str(vcn1) + '-' + str(vcn2) + '-' + str(vcn3) + '-' + str(vcn4))
            print("exp date: " + str(vced1) + "/" + str(vced2))
            print("cvv: " + str(vcvv))
        # MASTERCARD
        if cng == "2":
            print("MASTERCARD")
            mcn1 = random.randint(000, 999)
            mcn2 = random.randint(0000,9999)
            mcn3 = random.randint(0000,9999)
            mcn4 = random.randint(0000,9999)
            vced1 = random.randint(1, 12)
            expyear = "2025", "2026", "2027", "2028", "2029", "2030", "2031", "2032"
            vced2 = random.choice(expyear)
            vcvv = random.randint(000, 999)
            print("")
            print("card number: 5" + str(mcn1) + '-' + str(mcn2) + '-' + str(mcn3) + '-' + str(mcn4))
            print("exp date: " + str(vced1) + "/" + str(vced2))
            print("cvv: " + str(vcvv))
        # AMERICAN EXPRESS
        if cng == "3":
            print('AMERICAN EXPRESS')
            acn1 = random.randint(000, 999)
            acn2 = random.randint(0000,9999)
            acn3 = random.randint(0000,9999)
            acn4 = random.randint(0000,9999)
            vced1 = random.randint(1, 12)
            expyear = "2025", "2026", "2027", "2028", "2029", "2030"
            vced2 = random.choice(expyear)
            vcvv = random.randint(000, 999)
            print("")
            print("card number: 3" + str(acn1) + '-' + str(acn2) + '-' + str(acn3) + '-' + str(acn4))
            print("exp date: " + str(vced1) + "/" + str(vced2))
            print("cvv: " + str(vcvv))
    # NMAP LOCAL IP SCAN