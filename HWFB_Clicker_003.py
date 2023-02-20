######################
# HW BOT by eMintis #
######################
# pip install pyautogui
# pip install Pillow
# pip install keyboard
# pip install opencv-python

#Import things
import pyautogui
pyautogui.PAUSE = 1  # pause
pyautogui.FAILSAFE = True # Move to top-left to exit

import time
import keyboard
import random

#pyautogui.position()   #cursor position
#pyautogui.alert('This is the message to display.') #msg OK
#print ("3 sec delay")
#time.sleep(3)

#Screen resolution and size:
swidth, sheight = pyautogui.size()
srv = 1 #set multiplier for 2560x1440
srh = 1 #set multiplier for 2560x1440
vrand = random.randint(1,10) # random width modifier
hrand = random.randint(1,5) # random height modifier

if (swidth == 3840) and (sheight == 2160):
    srv = 1.5
    srh = 1.5
elif (swidth == 2560) and (sheight == 1440):
    srv = 1
    srh = 1
#elif (swidth == 1920) and (sheight == 1200):
#    srv = 0.75
#    srh = 0.83333
elif (swidth == 1920) and (sheight == 1080):
    srv = 0.75
    srh = 0.75
#elif (swidth == 1680) and (sheight == 1050):
#    srv = 0.65625
#   srh = 0.72916
elif (swidth == 1600) and (sheight == 900):
    srv = 0.625
    srh = 0.625
#elif (swidth == 1440) and (sheight == 900):
#    srv = 0.5625
#    srh = 0.625
elif (swidth == 1366) and (sheight == 768):
    srv = 0.53359
    srh = 0.53333
#elif (swidth == 1280) and (sheight == 800):
#    srv = 0.5
#    srh = 0.55555
else:
    print('!!! Unsuported resolution: only #1 clicker will work!!! \n')
    pyautogui.alert('!!! Unsuported resolution: only #1 clicker will work!!!') #msg not OK
###

print('\n ###################################################################')
print(' ######------- HW Clicker v003 - Screen res:' , swidth,'x', sheight, '-------########')
print(' * To Stop move mouse Top Left Corner \n')
print(' * Close pop-ups, open Game in Fullscreen mode \n', vrand, "--", hrand)
pyautogui.alert('!!! Unsuported resolution: only #1 clicker will work!!!') #msg not OK
menu_options = {
    1: 'AutoClicker',
    2: 'Gifts -',
    3: 'Heroic Chest -',
    4: 'Outland -',
    5: 'AirShip -',
    6: 'Grand arena -',
    7: 'Tower -',
    8: 'Arena -',
    9: '-Asgard - ???',
    10: '-Sanctuary - ???',
    11: '-Titan Valley - ???',
    0: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
     print (key, '--', menu_options[key] )

def option1():
     print('> AutoClicker')
     
     coords = ''
     clix = ''
     print (" 1. Enter how many clicks \n 2. Point mouse were to click and press Enter")
     clix = int(input('How many: '))
     
     print ("2 sec delay... you can move mouse too.. \n")

     keyboard.send("windows+down")
     time.sleep(2)

     coords = pyautogui.position()
     pyautogui.click(coords[0], coords[1], clicks=clix, interval=0.1, button='left') # Do clicking


def option2():
     print('Friend gifts') # all gifts
     
     keyboard.send("windows+down")
     time.sleep(2)

     pyautogui.click(1785*srv, 1269*srh, clicks=1, interval=1, button='left') # Open Gifts
     pyautogui.click(1275*srv, 789*srh, clicks=1, interval=1, button='left') # Send Gifts
     # Auto Close and back to menu  


def option3():
     print('Openening Heroic Chest')

     keyboard.send("windows+down")
     time.sleep(2)

     pyautogui.click(687*srv, 1000*srh, clicks=1, interval=1, button='left') # Open Chest
     pyautogui.click(1635*srv, 1148*srh, clicks=1, interval=1, button='left') # Send Gifts
     pyautogui.click(1271*srv, 1250*srh, clicks=1, interval=1, button='left') # OK
     pyautogui.click(1907*srv, 220*srh, clicks=1, interval=1, button='left') # Close
     pyautogui.click(2333*srv, 247*srh, clicks=1, interval=1, button='left') # Close Exit


def option4():
     print('Outland reward')

     keyboard.send("windows+down")
     time.sleep(2)     
     
     pyautogui.click(1002*srv, 101*srh, clicks=1, interval=1, button='left') # Open

     pyautogui.click(569*srv, 776*srh, clicks=1, interval=1, button='left') # Open 1 chest Claim reward
     pyautogui.click(1280*srv, 900*srh, clicks=1, interval=1, button='left') # Open chests
     pyautogui.click(1271*srv, 953*srh, clicks=1, interval=1, button='left') # Open get reward
     pyautogui.click(2318*srv, 174*srh, clicks=1, interval=1, button='left') # Close 1 chest

     pyautogui.click(2198*srv, 1178*srh, clicks=1, interval=1, button='left') # Open 2 Chest menu Next boss

     pyautogui.click(569*srv, 776*srh, clicks=1, interval=1, button='left') # Open 2 chest Claim reward
     pyautogui.click(1280*srv, 900*srh, clicks=1, interval=1, button='left') # Open chests
     pyautogui.click(1271*srv, 953*srh, clicks=1, interval=1, button='left') # Open get reward
     pyautogui.click(2318*srv, 174*srh, clicks=1, interval=1, button='left') # Close 2 chest

     pyautogui.click(2198*srv, 1178*srh, clicks=1, interval=1, button='left') # Open 3 Chest menu Next boss

     pyautogui.click(569*srv, 776*srh, clicks=1, interval=1, button='left') # Open 2 chest Claim reward
     pyautogui.click(1280*srv, 900*srh, clicks=1, interval=1, button='left') # Open chests
     pyautogui.click(1271*srv, 953*srh, clicks=1, interval=1, button='left') # Open get reward
     pyautogui.click(2318*srv, 174*srh, clicks=1, interval=1, button='left') # Close 2 chest

     pyautogui.click(2337*srv, 86*srh, clicks=1, interval=1, button='left') # Close Exit Outland
        
def option5():
     print('Airship open')

     keyboard.send("windows+down")
     time.sleep(2)     

     pyautogui.click(1346*srv, 206*srh, clicks=1, interval=1, button='left') # Open Airship
     pyautogui.click(1284*srv, 387*srh, clicks=1, interval=1, button='left') # Open Gift
     pyautogui.click(1276*srv, 917*srh, clicks=1, interval=1, button='left') # Collect
     pyautogui.click(2259*srv, 147*srh, clicks=1, interval=1, button='left') # Close

     pyautogui.click(1276*srv, 1034*srh, clicks=1, interval=1, button='left') # Open Expedition

def option6():
     print('Grand Arena')

     keyboard.send("windows+down")
     time.sleep(2)     

     pyautogui.click(1756*srv, 380*srh, clicks=1, interval=1, button='left') # Open Grand Arena
     pyautogui.click(536*srv, 817*srh, clicks=1, interval=1, button='left') # Claim
     pyautogui.click(2248*srv, 205*srh, clicks=1, interval=1, button='left') # Close
     
def option7():
     print('Tower run')
     keyboard.send("windows+down")
     time.sleep(2) 

     pyautogui.click(2063*srv, 311*srh, clicks=1, interval=1, button='left') # Open tower

     pyautogui.click(1219*srv, 720*srh, clicks=1, interval=1, button='left') # Instant Clear

     pyautogui.click(870*srv, 1022*srh, clicks=1, interval=1, button='left') # Choose Left Chests

     pyautogui.click(1706*srv, 790*srh, clicks=1, interval=1, button='left') # Choose 4th
     pyautogui.click(1916*srv, 925*srh, clicks=1, interval=1, button='left') # 3rd box
     #pyautogui.click(1290*srv, 925*srh, clicks=1, interval=1, button='left') # 2nd box
     #pyautogui.click(675*srv, 925*srh, clicks=1, interval=1, button='left') # 1st box
     pyautogui.click(2038*srv, 1229*srh, clicks=1, interval=1, button='left') # Proceed

     pyautogui.click(1706*srv, 790*srh, clicks=1, interval=1, button='left') # Choose 8th
     pyautogui.click(1916*srv, 925*srh, clicks=1, interval=1, button='left') # 3rd box
     pyautogui.click(2038*srv, 1229*srh, clicks=1, interval=1, button='left') # Proceed

     pyautogui.click(1706*srv, 790*srh, clicks=1, interval=1, button='left') # Choose 10th
     pyautogui.click(1916*srv, 925*srh, clicks=1, interval=1, button='left') # 3rd box
     pyautogui.click(2038*srv, 1229*srh, clicks=1, interval=1, button='left') # Proceed

     pyautogui.click(1706*srv, 790*srh, clicks=1, interval=1, button='left') # Choose 14th
     pyautogui.click(1916*srv, 925*srh, clicks=1, interval=1, button='left') # 3rd box
     pyautogui.click(2038*srv, 1229*srh, clicks=1, interval=1, button='left') # Proceed

     pyautogui.click(1706*srv, 790*srh, clicks=1, interval=1, button='left') # Choose 16th
     pyautogui.click(1916*srv, 925*srh, clicks=1, interval=1, button='left') # 3rd box
     pyautogui.click(2038*srv, 1229*srh, clicks=1, interval=1, button='left') # Proceed

     pyautogui.click(1706*srv, 790*srh, clicks=1, interval=1, button='left') # Choose 20th
     pyautogui.click(1916*srv, 925*srh, clicks=1, interval=1, button='left') # 3rd box
     pyautogui.click(2038*srv, 1229*srh, clicks=1, interval=1, button='left') # Proceed

     pyautogui.click(1706*srv, 790*srh, clicks=1, interval=1, button='left') # Choose 22th
     pyautogui.click(1916*srv, 925*srh, clicks=1, interval=1, button='left') # 3rd box
     pyautogui.click(2038*srv, 1229*srh, clicks=1, interval=1, button='left') # Proceed

     pyautogui.click(1706*srv, 790*srh, clicks=1, interval=1, button='left') # Choose 26th
     pyautogui.click(1916*srv, 925*srh, clicks=1, interval=1, button='left') # 3rd box
     pyautogui.click(2038*srv, 1229*srh, clicks=1, interval=1, button='left') # Proceed

     pyautogui.click(1706*srv, 790*srh, clicks=1, interval=1, button='left') # Choose 28th
     pyautogui.click(1916*srv, 925*srh, clicks=1, interval=1, button='left') # 3rd box
     pyautogui.click(2038*srv, 1229*srh, clicks=1, interval=1, button='left') # Proceed

     pyautogui.click(1706*srv, 790*srh, clicks=1, interval=1, button='left') # Choose 32th
     pyautogui.click(1916*srv, 925*srh, clicks=1, interval=1, button='left') # 3rd box
     pyautogui.click(2038*srv, 1229*srh, clicks=1, interval=1, button='left') # Proceed

     pyautogui.click(920*srv, 731*srh, clicks=1, interval=1, button='left') # Choose 35th Left
     pyautogui.click(1916*srv, 925*srh, clicks=1, interval=1, button='left') # 3rd box
     pyautogui.click(2038*srv, 1229*srh, clicks=1, interval=1, button='left') # Proceed

     pyautogui.click(920*srv, 731*srh, clicks=1, interval=1, button='left') # Choose 39th Left
     pyautogui.click(1916*srv, 925*srh, clicks=1, interval=1, button='left') # 3rd box
     pyautogui.click(2038*srv, 1229*srh, clicks=1, interval=1, button='left') # Proceed

     pyautogui.click(1706*srv, 790*srh, clicks=1, interval=1, button='left') # Choose 42th
     pyautogui.click(1916*srv, 925*srh, clicks=1, interval=1, button='left') # 3rd box
     pyautogui.click(2038*srv, 1229*srh, clicks=1, interval=1, button='left') # Proceed

     pyautogui.click(1706*srv, 790*srh, clicks=1, interval=1, button='left') # Choose 46th
     pyautogui.click(1916*srv, 925*srh, clicks=1, interval=1, button='left') # 3rd box
     pyautogui.click(2038*srv, 1229*srh, clicks=1, interval=1, button='left') # Proceed

     pyautogui.click(1973*srv, 699*srh, clicks=1, interval=1, button='left') # Choose 50th Final
     pyautogui.click(1916*srv, 925*srh, clicks=1, interval=1, button='left') # 3rd box
     pyautogui.click(2309*srv, 208*srh, clicks=1, interval=1, button='left') # Close

     pyautogui.click(268*srv, 112*srh, clicks=1, interval=1, button='left') # Scul
     pyautogui.click(1263*srv, 945*srh, clicks=1, interval=1, button='left') # Exchange points

     pyautogui.click(418*srv, 1311*srh, clicks=1, interval=1, button='left') # Tower points
     pyautogui.click(1238*srv, 1239*srh, clicks=1, interval=1, button='left') # Collect all
     pyautogui.click(1812*srv, 188*srh, clicks=1, interval=1, button='left') # Close

     pyautogui.click(2300*srv, 83*srh, clicks=1, interval=1, button='left') # Close Tower

def option8():
     print('Arena fight')
     keyboard.send("windows+down")
     time.sleep(2) 

     pyautogui.click(1509*srv, 662*srh, clicks=1, interval=1, button='left') # Open
    #pyautogui.click(595*srv, 851*srh, clicks=1, interval=1, button='left') # Attack 1 position (team should be selected)
     pyautogui.click(1054*srv, 848*srh, clicks=1, interval=1, button='left') # Attack 2 position (team should be selected)
    #pyautogui.click(1510*srv, 854*srh, clicks=1, interval=1, button='left') # Attack 3 position (team should be selected)
     pyautogui.click(2098*srv, 1296*srh, clicks=1, interval=1, button='left') # To battle
     print ("3 sec delay")
     time.sleep(3)
     pyautogui.click(2302*srv, 97*srh, clicks=1, interval=1, button='left') # Pause
     pyautogui.click(1276*srv, 856*srh, clicks=1, interval=1, button='left') # Skip battle
     pyautogui.click(2208*srv, 171*srh, clicks=1, interval=1, button='left') # Close

def option9():
     print('Asgard collect seed')

     keyboard.send("windows+down")
     time.sleep(2)      

     pyautogui.click(583*srv, 1040*srh, clicks=1, interval=1, button='left') # Open
     pyautogui.click(1225*srv, 1042*srh, clicks=1, interval=1, button='left') # Astral Seer
     pyautogui.click(1117*srv, 1248*srh, clicks=1, interval=2, button='left') # Open Get
     print ("3 sec delay")
     time.sleep(3)
     pyautogui.click(2318*srv, 86*srh, clicks=2, interval=2, button='left') # Close
     #pyautogui.click(1670*srv, 230srh, clicks=1, interval=2, button='left') # Close
     #pyautogui.click(1670*srv, 230srh, clicks=1, interval=1, button='left') # Close


def option10():
     print('Sanctuary buy 2')

     keyboard.send("windows+down")
     time.sleep(2)      

     pyautogui.click(1503*srv, 368*srh, clicks=1, interval=1, button='left') # Open
     pyautogui.click(707*srv, 747*srh, clicks=1, interval=1, button='left') # Merchant
     pyautogui.click(1055*srv, 637*srh, clicks=1, interval=1, button='left') # Buy 1
     pyautogui.click(1670*srv, 637*srh, clicks=1, interval=1, button='left') # Buy 2
     pyautogui.click(1932*srv, 248*srh, clicks=1, interval=1, button='left') # Close
     pyautogui.click(2316*srv, 85*srh, clicks=1, interval=1, button='left') # Close

def option11():
     print('Titan valley')

     keyboard.send("windows+down")
     time.sleep(2)      

     pyautogui.click(890*srv, 555*srh, clicks=1, interval=1, button='left') # Open
     pyautogui.click(600*srv, 550*srh, clicks=1, interval=1, button='left') # Open Tournament of ..

     pyautogui.click(1585*srv, 1108*srh, clicks=1, interval=1, button='left') # Raid 1
     pyautogui.click(1281*srv, 1097*srh, clicks=1, interval=1, button='left') # Raid
     pyautogui.click(1283*srv, 1175*srh, clicks=2, interval=1, button='left') # Show all / OK
     pyautogui.click(1260*srv, 950*srh, clicks=1, interval=1, button='left') # Claim reward

     pyautogui.click(1585*srv, 1108*srh, clicks=1, interval=1, button='left') # Raid 2
     pyautogui.click(1281*srv, 1097*srh, clicks=1, interval=1, button='left') # Raid
     pyautogui.click(1283*srv, 1175*srh, clicks=2, interval=1, button='left') # Show all / OK
     pyautogui.click(1260*srv, 950*srh, clicks=1, interval=1, button='left') # Claim reward

     pyautogui.click(1585*srv, 1108*srh, clicks=1, interval=1, button='left') # Raid 3
     pyautogui.click(1281*srv, 1097*srh, clicks=1, interval=1, button='left') # Raid
     pyautogui.click(1283*srv, 1175*srh, clicks=2, interval=1, button='left') # Show all / OK
     pyautogui.click(1260*srv, 950*srh, clicks=1, interval=1, button='left') # Claim reward

     pyautogui.click(1585*srv, 1108*srh, clicks=1, interval=1, button='left') # Raid 4
     pyautogui.click(1281*srv, 1097*srh, clicks=1, interval=1, button='left') # Raid
     pyautogui.click(1283*srv, 1175*srh, clicks=2, interval=1, button='left') # Show all / OK
     pyautogui.click(1260*srv, 950*srh, clicks=1, interval=1, button='left') # Claim reward

     pyautogui.click(1585*srv, 1108*srh, clicks=1, interval=1, button='left') # Raid 5
     pyautogui.click(1281*srv, 1097*srh, clicks=1, interval=1, button='left') # Raid
     pyautogui.click(1283*srv, 1175*srh, clicks=2, interval=1, button='left') # Show all / OK
     pyautogui.click(1260*srv, 950*srh, clicks=1, interval=1, button='left') # Claim reward

     pyautogui.click(1585*srv, 1108*srh, clicks=1, interval=1, button='left') # Raid 6
     pyautogui.click(1281*srv, 1097*srh, clicks=1, interval=1, button='left') # Raid
     pyautogui.click(1283*srv, 1175*srh, clicks=2, interval=1, button='left') # Show all / OK
     pyautogui.click(1260*srv, 950*srh, clicks=1, interval=1, button='left') # Claim reward     

     pyautogui.click(1585*srv, 1108*srh, clicks=1, interval=1, button='left') # Raid 7
     pyautogui.click(1281*srv, 1097*srh, clicks=1, interval=1, button='left') # Raid
     pyautogui.click(1283*srv, 1175*srh, clicks=2, interval=1, button='left') # Show all / OK
     pyautogui.click(1260*srv, 950*srh, clicks=1, interval=1, button='left') # Claim reward

     pyautogui.click(2232*srv, 1003*srh, clicks=1, interval=1, button='left') # Reward box open
     pyautogui.click(1261*srv, 1149*srh, clicks=1, interval=1, button='left') # Reward box claim
     pyautogui.click(1284*srv, 1130*srh, clicks=1, interval=1, button='left') # Reward box ok

     pyautogui.click(1670*srv, 230*srh, clicks=1, interval=1, button='left') # Close


if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            option5()
        elif option == 6:
            option6()
        elif option == 7:
            option7()
        elif option == 8:
            option8()
        elif option == 9:
            option9()
        elif option == 10:
            option10()
        elif option == 11:
            option11()                
        elif option == 0:
            print('Bye bye')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 11.')
