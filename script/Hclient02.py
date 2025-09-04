# COPYRIGHT: Hclient, a multi tool python program for general tech purposes.    Copyright (C) 2025  Kevin De Togni, MKlabs
# LICENSE: distribuited on the GNU general public license 3.0v license
# IMPORTS
import os
import random
# LOGO, CREDITS & INITIAL PHRASES
print('Hclient, a multi tool python program for general tech purposes.    Copyright (C) 2025  Kevin De Togni, MKlabs')
print('distribuited on the GNU general public license 3.0v license')
print('          _________    _________')
print('         /        /   /        /')
print('        /        /   /        /')
print('       /        /   /        /')
print('      /        /___/        / _________    ____       ____  _________   ____     ____  _____________           by MKlabs developer team')
print('     /                     / /        /   /   /      /   / /   _____/  /    |   /   / /            /           devs: MrMaxX, Marcocve')
print('    /        ____         / /   _____/   /   /      /   / /   /____   /     |  /   / /____    ____/')
print('   /        /   /        / /   /        /   /      /   / /    ____/  /   |  | /   /      /   /                 official website:')
print('  /        /   /        / /    |_____  /   /      /   / /    /      /   /|  |/   /      /   /                  officialmklabsveneto.netlify.app')
print(' /        /   /        /  |         / /   /____  /   / /    /____  /   / |      /      /   /')
print('/________/   /_______ /   | _______/ /________/ /___/ /_________/ /___/  |_____/      /___/                    version: 0.2 BETA')
print('')
print('some features only work on linux and its recommended to run Hclient as root or some feature will not work!')
print('')
print('select an option:')
print('1 = passgen, 2 = btcadressgen, 3 = cardnumbergen, 4 = nmap local ip scan, 5 =  system information, 6 = pkg updater')
print('')
usrchoice = input()
print('')
# PASSGEN
if usrchoice == '1':
    print('how many passwords do you want to generate?')
    print('')
    usrpinput = int(input())
    print('')
    print("press ENTER to execute")
    input()
    print('')
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
elif usrchoice == '2':
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
elif usrchoice == '3':
    print('which card do you want to generate?')
    print('')
    print('1 = Visa')
    print('2 = Mastercard')
    print('3 = American Express')
    print('')
    cng = input()
    print('')
    # VISA
    if cng == '1':
        print('VISA')
        vcn1 = random.randint(000, 999)
        vcn2 = random.randint(0000,9999)
        vcn3 = random.randint(0000,9999)
        vcn4 = random.randint(0000,9999)
        vced1 = random.randint(1, 12)
        expyear = '2025', '2026', '2027', '2028', '2029', '2030', '2031'
        vced2 = random.choice(expyear)
        vcvv = random.randint(000, 999)
        print('')
        print('card number: 4' + str(vcn1) + '-' + str(vcn2) + '-' + str(vcn3) + '-' + str(vcn4))
        print('exp date: ' + str(vced1) + '/' + str(vced2))
        print('cvv: ' + str(vcvv))
    # MASTERCARD
    elif cng == '2':
        print('MASTERCARD')
        mcn1 = random.randint(000, 999)
        mcn2 = random.randint(0000,9999)
        mcn3 = random.randint(0000,9999)
        mcn4 = random.randint(0000,9999)
        vced1 = random.randint(1, 12)
        expyear = '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032'
        vced2 = random.choice(expyear)
        vcvv = random.randint(000, 999)
        print('')
        print('card number: 5' + str(mcn1) + '-' + str(mcn2) + '-' + str(mcn3) + '-' + str(mcn4))
        print('exp date: ' + str(vced1) + '/' + str(vced2))
        print('cvv: ' + str(vcvv))
    # AMERICAN EXPRESS
    elif cng == "3":
        print('AMERICAN EXPRESS')
        acn1 = random.randint(000, 999)
        acn2 = random.randint(0000,9999)
        acn3 = random.randint(0000,9999)
        acn4 = random.randint(0000,9999)
        vced1 = random.randint(1, 12)
        expyear = '2025', '2026', '2027', '2028', '2029', '2030'
        vced2 = random.choice(expyear)
        vcvv = random.randint(000, 999)
        print('')
        print('card number: 3' + str(acn1) + '-' + str(acn2) + '-' + str(acn3) + '-' + str(acn4))
        print('exp date: ' + str(vced1) + '/' + str(vced2))
        print('cvv: ' + str(vcvv))
# NMAP LOCAL IP SCAN (in maintenance)
elif usrchoice == '4':
    finalip = ''
    print('enter target local ip: example: 192.168.0.1')
    print('')
    usrlocalip = input()
    print('')
    print('enter target port: example: 24')
    print('')
    usrport = input()
    print('')
    print('does the target ip loos like this: ',usrlocalip + '/' + usrport, '? y/n')
    print('')
    usrnlisfr = input()
    print('')
    if usrnlisfr == 'y':
        finalip = usrlocalip + '/' + usrport
        os.system('nmap -sS ' + finalip)
    elif usrnlisfr == 'n':
        print('relaunch program and insert correct ip')
        input()
# SYSTEMINFORMATION
if usrchoice == '5':
    os.system('fastfetch')
# PKG UPDATER
if usrchoice == '6':
    print('select package manager: apt, dnf, pacman')
    print('')
    usrpkgmchoice = input()
    print('')
    if usrpkgmchoice == 'apt':
        os.system('sudo apt update && upgrade')
    elif usrpkgmchoice == 'dnf':
        os.system('sudo dnf update && upgrade')
    elif usrpkgmchoice == 'pacman':
        os.system('sudo pacman -Syu')
input()
# COPYRIGHT: Hclient, a multi tool python program for general tech purposes.    Copyright (C) 2025  Kevin De Togni, MKlabs
# LICENSE: distribuited on the GNU general public license 3.0v license