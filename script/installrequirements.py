import os
print('select distro: 1 = debain/ubuntu based , 2 = fedora based, 3 = arch based')
print('')
ud = input()
print('')
print('this software will install the Hclient requirements: nmap, neofetch, fastfetch, macchina, hyfetch')
print('')
urc = input('install? y/n: ')
print('')
if urc == 'y':
    if ud == '1':
        os.system('sudo apt install nmap neofetch fastfetch macchina hyfetch -y')
    elif ud == '2':
        os.system('sudo dnf install nmap neofetch fastfetch macchina hyfetch -y')
    elif ud == '3':
        os.system('sudo pacman -S nmap fastfetch macchina hyfetch -y && yay -S neofetch -y')
elif urc == 'n':
    print('installation aborted, press ENTER to exit')
    input()