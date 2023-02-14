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

#pyautogui.position()   #cursor position
#pyautogui.alert('This is the message to display.') #msg OK
#print ("3 sec delay")
#time.sleep(3)

#Screen resolution and size:
sweight, sheight = pyautogui.size()
srv = 1 #set multiplier for 2560x1440
srh = 1 #set multiplier for 2560x1440

if (sweight == 3840) and (sheight == 2160):
    srv = 1.5
    srh = 1.5
elif (sweight == 2560) and (sheight == 1440):
    srv = 1
    srh = 1
elif (sweight == 1920) and (sheight == 1080):
    srv = 0.75
    srh = 0.75
elif (sweight == 1680) and (sheight == 1050):
    srv = 0.65625
    srh = 0.72916
elif (sweight == 1600) and (sheight == 900):
    srv = 0.625
    srh = 0.625
elif (sweight == 1440) and (sheight == 900):
    srv = 0.5625
    srh = 0.625
elif (sweight == 1366) and (sheight == 768):
    srv = 0.53359
    srh = 0.53333
elif (sweight == 1280) and (sheight == 800):
    srv = 0.5
    srh = 0.55555
else:
    print('!!! Unsuported resolution: only #1 clicker will work!!! \n')
###

print('\n ###################################################################')
print(' ######------- HW Bot v001 - Screen res:' , sweight,'x', sheight, '-------########')
print(' * To Stop move mouse Top Left Corner \n')
print(' * Close pop-ups, open Game in Fullscreen mode \n')

menu_options = {
    1: 'AutoClicker +',
    2: 'Gifts',
    3: 'Heroic Chest',
    4: 'Outland',
    5: 'AirShip',
    6: 'Grand arena',
    7: 'Tower +',
    8: 'Arena',
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
     print('> Friend gifts, Heroic Chest, Outland, Airship, Grand Arena') # all gifts
     
     pyautogui.click(1785, 1269, clicks=1, interval=1, button='left') # Open Gifts
     pyautogui.click(1275, 789, clicks=1, interval=1, button='left') # Send Gifts
     # Auto Close and back to menu  


def option3():
     print('Openening Heroic Chest')

     pyautogui.click(354, 995, clicks=1, interval=1, button='left') # Open Chest
     pyautogui.click(1635, 1148, clicks=1, interval=1, button='left') # Send Gifts
     pyautogui.click(1271, 1250, clicks=1, interval=1, button='left') # OK
     pyautogui.click(1907, 220, clicks=1, interval=1, button='left') # Close
     pyautogui.click(2333, 247, clicks=1, interval=1, button='left') # Close Exit


def option4():
     print('Outland reward')
     
     pyautogui.click(1002, 198, clicks=1, interval=1, button='left') # Open

     pyautogui.click(569, 776, clicks=1, interval=1, button='left') # Open 1 chest Claim reward
     pyautogui.click(1280, 900, clicks=1, interval=1, button='left') # Open chests
     pyautogui.click(1271, 953, clicks=1, interval=1, button='left') # Open get reward
     pyautogui.click(2318, 174, clicks=1, interval=1, button='left') # Close 1 chest

     pyautogui.click(2198, 1178, clicks=1, interval=1, button='left') # Open 2 Chest menu Next boss

     pyautogui.click(569, 776, clicks=1, interval=1, button='left') # Open 2 chest Claim reward
     pyautogui.click(1280, 900, clicks=1, interval=1, button='left') # Open chests
     pyautogui.click(1271, 953, clicks=1, interval=1, button='left') # Open get reward
     pyautogui.click(2318, 174, clicks=1, interval=1, button='left') # Close 2 chest

     pyautogui.click(2198, 1178, clicks=1, interval=1, button='left') # Open 3 Chest menu Next boss

     pyautogui.click(569, 776, clicks=1, interval=1, button='left') # Open 2 chest Claim reward
     pyautogui.click(1280, 900, clicks=1, interval=1, button='left') # Open chests
     pyautogui.click(1271, 953, clicks=1, interval=1, button='left') # Open get reward
     pyautogui.click(2318, 174, clicks=1, interval=1, button='left') # Close 2 chest

     pyautogui.click(2337, 86, clicks=1, interval=1, button='left') # Close Exit Outland
        
def option5():
     print('Airship open')

     pyautogui.click(1346, 313, clicks=1, interval=1, button='left') # Open Airship
     pyautogui.click(1284, 387, clicks=1, interval=1, button='left') # Open Gift
     pyautogui.click(1276, 917, clicks=1, interval=1, button='left') # Collect
     pyautogui.click(2259, 147, clicks=1, interval=1, button='left') # Close

     pyautogui.click(1276, 1034, clicks=1, interval=1, button='left') # Open Expedition

def option6():
     print('Grand Arena')

     pyautogui.click(1756, 407, clicks=1, interval=1, button='left') # Open Grand Arena
     pyautogui.click(536, 817, clicks=1, interval=1, button='left') # Claim
     pyautogui.click(2248, 205, clicks=1, interval=1, button='left') # Close
     
def option7():
     print('Tower run')
     pyautogui.click(2063, 263, clicks=1, interval=1, button='left') # Open tower

     pyautogui.click(1219, 720, clicks=1, interval=1, button='left') # Instant Clear

     pyautogui.click(870, 1022, clicks=1, interval=1, button='left') # Choose Left Chests

     pyautogui.click(1706, 790, clicks=1, interval=1, button='left') # Choose 4th
     pyautogui.click(1916, 925, clicks=1, interval=1, button='left') # 3rd box
     #pyautogui.click(1290, 925, clicks=1, interval=1, button='left') # 2nd box
     #pyautogui.click(675, 925, clicks=1, interval=1, button='left') # 1st box
     pyautogui.click(2038, 1229, clicks=1, interval=1, button='left') # Proceed

     pyautogui.click(1706, 790, clicks=1, interval=1, button='left') # Choose 8th
     pyautogui.click(1916, 925, clicks=1, interval=1, button='left') # 3rd box
     pyautogui.click(2038, 1229, clicks=1, interval=1, button='left') # Proceed

     pyautogui.click(1706, 790, clicks=1, interval=1, button='left') # Choose 10th
     pyautogui.click(1916, 925, clicks=1, interval=1, button='left') # 3rd box
     pyautogui.click(2038, 1229, clicks=1, interval=1, button='left') # Proceed

     pyautogui.click(1706, 790, clicks=1, interval=1, button='left') # Choose 14th
     pyautogui.click(1916, 925, clicks=1, interval=1, button='left') # 3rd box
     pyautogui.click(2038, 1229, clicks=1, interval=1, button='left') # Proceed

     pyautogui.click(1706, 790, clicks=1, interval=1, button='left') # Choose 16th
     pyautogui.click(1916, 925, clicks=1, interval=1, button='left') # 3rd box
     pyautogui.click(2038, 1229, clicks=1, interval=1, button='left') # Proceed

     pyautogui.click(1706, 790, clicks=1, interval=1, button='left') # Choose 20th
     pyautogui.click(1916, 925, clicks=1, interval=1, button='left') # 3rd box
     pyautogui.click(2038, 1229, clicks=1, interval=1, button='left') # Proceed

     pyautogui.click(1706, 790, clicks=1, interval=1, button='left') # Choose 22th
     pyautogui.click(1916, 925, clicks=1, interval=1, button='left') # 3rd box
     pyautogui.click(2038, 1229, clicks=1, interval=1, button='left') # Proceed

     pyautogui.click(1706, 790, clicks=1, interval=1, button='left') # Choose 26th
     pyautogui.click(1916, 925, clicks=1, interval=1, button='left') # 3rd box
     pyautogui.click(2038, 1229, clicks=1, interval=1, button='left') # Proceed

     pyautogui.click(1706, 790, clicks=1, interval=1, button='left') # Choose 28th
     pyautogui.click(1916, 925, clicks=1, interval=1, button='left') # 3rd box
     pyautogui.click(2038, 1229, clicks=1, interval=1, button='left') # Proceed

     pyautogui.click(1706, 790, clicks=1, interval=1, button='left') # Choose 32th
     pyautogui.click(1916, 925, clicks=1, interval=1, button='left') # 3rd box
     pyautogui.click(2038, 1229, clicks=1, interval=1, button='left') # Proceed

     pyautogui.click(920, 731, clicks=1, interval=1, button='left') # Choose 35th Left
     pyautogui.click(1916, 925, clicks=1, interval=1, button='left') # 3rd box
     pyautogui.click(2038, 1229, clicks=1, interval=1, button='left') # Proceed

     pyautogui.click(920, 731, clicks=1, interval=1, button='left') # Choose 39th Left
     pyautogui.click(1916, 925, clicks=1, interval=1, button='left') # 3rd box
     pyautogui.click(2038, 1229, clicks=1, interval=1, button='left') # Proceed

     pyautogui.click(1706, 790, clicks=1, interval=1, button='left') # Choose 42th
     pyautogui.click(1916, 925, clicks=1, interval=1, button='left') # 3rd box
     pyautogui.click(2038, 1229, clicks=1, interval=1, button='left') # Proceed

     pyautogui.click(1706, 790, clicks=1, interval=1, button='left') # Choose 46th
     pyautogui.click(1916, 925, clicks=1, interval=1, button='left') # 3rd box
     pyautogui.click(2038, 1229, clicks=1, interval=1, button='left') # Proceed

     pyautogui.click(1973, 699, clicks=1, interval=1, button='left') # Choose 50th Final
     pyautogui.click(1916, 925, clicks=1, interval=1, button='left') # 3rd box
     pyautogui.click(2309, 208, clicks=1, interval=1, button='left') # Close

     pyautogui.click(268, 112, clicks=1, interval=1, button='left') # Scul
     pyautogui.click(1263, 945, clicks=1, interval=1, button='left') # Exchange points

     pyautogui.click(418, 1311, clicks=1, interval=1, button='left') # Tower points
     pyautogui.click(1238, 1239, clicks=1, interval=1, button='left') # Collect all
     pyautogui.click(1812, 188, clicks=1, interval=1, button='left') # Close

     pyautogui.click(2300, 83, clicks=1, interval=1, button='left') # Close Tower

def option8():
     print('Arena fight')

     pyautogui.click(1509, 662, clicks=1, interval=1, button='left') # Open
    #pyautogui.click(595, 851, clicks=1, interval=1, button='left') # Attack 1 position (team should be selected)
     pyautogui.click(1054, 848, clicks=1, interval=1, button='left') # Attack 2 position (team should be selected)
    #pyautogui.click(1510, 854, clicks=1, interval=1, button='left') # Attack 3 position (team should be selected)
     pyautogui.click(2098, 1296, clicks=1, interval=1, button='left') # To battle
     print ("3 sec delay")
     time.sleep(3)
     pyautogui.click(2302, 97, clicks=1, interval=1, button='left') # Pause
     pyautogui.click(1276, 856, clicks=1, interval=1, button='left') # Skip battle
     pyautogui.click(2208, 171, clicks=1, interval=1, button='left') # Close

def option9():
     print('Asgard collect seed')

     pyautogui.click(583, 1040, clicks=1, interval=1, button='left') # Open
     pyautogui.click(1225, 1042, clicks=1, interval=1, button='left') # Astral Seer
     pyautogui.click(1117, 1248, clicks=1, interval=2, button='left') # Open Get
     print ("3 sec delay")
     time.sleep(3)
     pyautogui.click(2318, 86, clicks=2, interval=2, button='left') # Close
     #pyautogui.click(1670, 230, clicks=1, interval=2, button='left') # Close
     #pyautogui.click(1670, 230, clicks=1, interval=1, button='left') # Close


def option10():
     print('Sanctuary buy 2')


     pyautogui.click(1503, 368, clicks=1, interval=1, button='left') # Open
     pyautogui.click(777, 597, clicks=1, interval=1, button='left') # Merchant
     pyautogui.click(984, 528, clicks=1, interval=1, button='left') # Buy 1
     pyautogui.click(1313, 527, clicks=1, interval=1, button='left') # Buy 2
     pyautogui.click(1457, 317, clicks=1, interval=1, button='left') # Close
     pyautogui.click(1670, 230, clicks=1, interval=1, button='left') # Close

def option11():
     print('Titan valley')

     pyautogui.click(880, 491, clicks=1, interval=1, button='left') # Open
     pyautogui.click(726, 488, clicks=1, interval=1, button='left') # Open Tournament of ..

     pyautogui.click(1264, 798, clicks=1, interval=1, button='left') # Raid 1
     pyautogui.click(1099, 797, clicks=1, interval=1, button='left') # Raid
     pyautogui.click(1093, 849, clicks=2, interval=1, button='left') # Show all / OK
     pyautogui.click(1099, 708, clicks=1, interval=1, button='left') # Claim reward

     pyautogui.click(1264, 798, clicks=1, interval=1, button='left') # Raid 2
     pyautogui.click(1099, 797, clicks=1, interval=1, button='left') # Raid
     pyautogui.click(1093, 849, clicks=2, interval=1, button='left') # Show all / OK
     pyautogui.click(1099, 708, clicks=1, interval=1, button='left') # Claim reward

     pyautogui.click(1264, 798, clicks=1, interval=1, button='left') # Raid 3
     pyautogui.click(1099, 797, clicks=1, interval=1, button='left') # Raid
     pyautogui.click(1093, 849, clicks=2, interval=1, button='left') # Show all / OK
     pyautogui.click(1099, 708, clicks=1, interval=1, button='left') # Claim reward

     pyautogui.click(1264, 798, clicks=1, interval=1, button='left') # Raid 4
     pyautogui.click(1099, 797, clicks=1, interval=1, button='left') # Raid
     pyautogui.click(1093, 849, clicks=2, interval=1, button='left') # Show all / OK
     pyautogui.click(1099, 708, clicks=1, interval=1, button='left') # Claim reward

     pyautogui.click(1264, 798, clicks=1, interval=1, button='left') # Raid 5
     pyautogui.click(1099, 797, clicks=1, interval=1, button='left') # Raid
     pyautogui.click(1093, 849, clicks=2, interval=1, button='left') # Show all / OK
     pyautogui.click(1099, 708, clicks=1, interval=1, button='left') # Claim reward 

     pyautogui.click(1264, 798, clicks=1, interval=1, button='left') # Raid 6
     pyautogui.click(1099, 797, clicks=1, interval=1, button='left') # Raid
     pyautogui.click(1093, 849, clicks=2, interval=1, button='left') # Show all / OK
     pyautogui.click(1099, 708, clicks=1, interval=1, button='left') # Claim reward         

     #pyautogui.click(1264, 798, clicks=1, interval=1, button='left') # Raid 7
     #pyautogui.click(1099, 797, clicks=1, interval=1, button='left') # Raid
     #pyautogui.click(1093, 849, clicks=2, interval=1, button='left') # Show all / OK
     #pyautogui.click(1099, 708, clicks=1, interval=1, button='left') # Claim reward

     pyautogui.click(1670, 230, clicks=1, interval=1, button='left') # Close


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
