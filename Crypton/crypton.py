import sys
import os
import platform
import time


if(platform.system()=='Windows'):
    os.system("color 02")

#CHECKING IF THE USER IS USING PYTHON VERSION 3 OR 2
if (sys.version_info < (3, 0)):
    print('''Please run it in Python 3.x version....
Download it from this link https://www.python.org/downloads/''')
    sys.exit()


#TRY TO IMPORT SELENIUM
try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

except ModuleNotFoundError:
    print('Please install Selenium by using this command "pip install selenium"')
    sys.exit()

#VARIABLES
name = ''
msg = ''
count = 0
cmd = ''
Pic = False
OpenChrome = False

#FUNCTIONS

def Banner():
    if(platform.system()=='Linux'):
        os.system('clear')
    elif(platform.system()=='Windows'):
        os.system('cls')
#Don't be panic..This is just a banner...:P
    print(b"\xff\xfe-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00\n\x00-\x00 \x00 \x00 \x00_\x00_\x00_\x00_\x00_\x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00_\x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00-\x00\n\x00-\x00 \x00 \x00/\x00 \x00_\x00_\x00_\x00_\x00|\x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00|\x00 \x00|\x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00V\x00e\x00r\x00s\x00i\x00o\x00n\x00 \x001\x00.\x000\x00 \x00 \x00-\x00\n\x00-\x00 \x00|\x00 \x00|\x00 \x00 \x00 \x00 \x00 \x00_\x00 \x00_\x00_\x00 \x00_\x00 \x00 \x00 \x00_\x00 \x00_\x00 \x00_\x00_\x00 \x00|\x00 \x00|\x00_\x00 \x00_\x00_\x00_\x00 \x00 \x00_\x00 \x00_\x00_\x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00-\x00\n\x00-\x00 \x00|\x00 \x00|\x00 \x00 \x00 \x00 \x00|\x00 \x00'\x00_\x00_\x00|\x00 \x00|\x00 \x00|\x00 \x00|\x00 \x00'\x00_\x00 \x00\\\x00|\x00 \x00_\x00_\x00/\x00 \x00_\x00 \x00\\\x00|\x00 \x00'\x00_\x00 \x00\\\x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00-\x00\n\x00-\x00 \x00|\x00 \x00|\x00_\x00_\x00_\x00_\x00|\x00 \x00|\x00 \x00 \x00|\x00 \x00|\x00_\x00|\x00 \x00|\x00 \x00|\x00_\x00)\x00 \x00|\x00 \x00|\x00|\x00 \x00(\x00_\x00)\x00 \x00|\x00 \x00|\x00 \x00|\x00 \x00|\x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00-\x00\n\x00-\x00 \x00 \x00\\\x00_\x00_\x00_\x00_\x00_\x00|\x00_\x00|\x00 \x00 \x00 \x00\\\x00_\x00_\x00,\x00 \x00|\x00 \x00.\x00_\x00_\x00/\x00 \x00\\\x00_\x00_\x00\\\x00_\x00_\x00_\x00/\x00|\x00_\x00|\x00 \x00|\x00_\x00|\x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00-\x00\n\x00-\x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00_\x00_\x00/\x00 \x00|\x00 \x00|\x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00-\x00\n\x00-\x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00|\x00_\x00_\x00_\x00/\x00|\x00_\x00|\x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00A\x00u\x00t\x00h\x00o\x00r\x00:\x00 \x00Z\x00a\x00f\x00e\x00e\x00r\x00 \x00 \x00 \x00 \x00 \x00 \x00-\x00\n\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00".decode('utf-16'))

def GetInfo():
    global name
    global msg
    global Pic
    global count
    global user
    name = input('Target Name: ')
    if name == "":
        Banner()
        GetCommands()
    if Pic != True:
        msg = input('Message: ')
    count = input('Number of Count: ')
    while not count.isdigit():
        print('Error: Count should be number.....')
        count = input('Number of Count: ')
    count = int(count)


def OpenWebDriver():
    global driver
    global OpenChrome
    if OpenChrome != True:
        options = webdriver.ChromeOptions();
        options.add_argument('--log-level 3')
        if(platform.system()=='Linux'):
            driver = webdriver.Chrome(os.path.abspath("Linux/chromedriver"),service_log_path='NUL')
        elif(platform.system()=='Windows'):
            driver = webdriver.Chrome(os.path.abspath("Windows/chromedriver.exe"),service_log_path='NUL')
        else:
            print("The is an error while opening webdriver.")
            sys.exit()
        driver.get('https://web.whatsapp.com/')

    OpenChrome = True

def SendMessage():
    global name
    global msg
    global count
    global driver
    global user
    try:
        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    except:
        print('Error: Unable to find target name.Make sure that the upper or lower casing is correct.')
        GetInfo()
        SendMessage()
    user.click()
    # msg_box = driver.find_element_by_class_name('_2S1VP')
    msg_box = driver.find_element_by_css_selector('footer div:nth-child(2n) div:nth-child(1n) div:nth-child(2n)')

    for i in range(count):
        msg_box.send_keys(msg)
        msg_box.send_keys(Keys.ENTER)
        # button = driver.find_element_by_class_name('_35EW6')
        # button.click()
    Banner()
    print('[*] Task has Completed! {} may be angry on you :P'.format(name))


def help():
    print('Commands           Detail')
    print('-------------------------------------------------------------')
    print('wdm                wdm(Whatsapp Dos with Message) is use to -\n                   send spacied number of messages          -')
    print('wdp                wdp(Whatsapp Dos with Picture) is use to -\n                   send spacied number of pics              -')
    print('exit               To exit the program                      -')
    print('about              See the version no. and author\'s detail  -')
    print('-------------------------------------------------------------')

def about():
    Banner()
    print('Names               Work                   Contact')
    print('------------------------------------------------------------------------------------------------')
    print('Zafeer              Developer+Idea         Facebook: https://www.facebook.com/We.Are.Watching.U')
    print('                                           Github: https://github.com/iivexii')
    print('Vaibhava Mishra     Suggestions+Testing    Facebook: https://m.facebook.com/vaibhava.mishra.7965')
    print('                                           Github: https://github.com/Vaibhava7965')
    print('Ameer Hamza         Suggestions            Facebook: https://www.facebook.com/ahn9100')
    print('                                           Github: https://github.com/ameerhmzx')
def SendPic():
        global name
        global count
        global driver
        global user
        global Pic
        for i in range(count):
                time.sleep(.30)
                try:
                    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
                except:
                    print('Error: Unable to find target name.Make sure that the upper or lower casing is correct.')
                    GetInfo()
                    SendPic()
                user.click()
                imgClip = driver.find_element_by_xpath('//div[@title="Attach"]')
                imgClip.click()
                time.sleep(1)
                img = driver.find_element_by_xpath('//ul[@class="_2imug"]/li[@class="_3L0q3 _167q _1Fc0v"]//input[@type="file"]')
                img.send_keys(os.getcwd() + "/Pic.jpg")    
                time.sleep(1)
                btn = driver.find_element_by_xpath('//div[@class="_3hV1n yavlE"]')
                btn.click()
def GetCommands():
    global driver
    global Pic
    cmd = input('root@Anonymous#:~ ').upper()
    while cmd == "":
        cmd = input('root@Anonymous#:~ ').upper()
    if cmd == 'WDM':
        Pic = False
        OpenWebDriver()
        Banner()
        while True:
            GetInfo()
            SendMessage()
    elif cmd == 'WDP':
        Pic = True
        OpenWebDriver()
        Banner()
        while True:
            GetInfo()
            SendPic()
    elif cmd == 'EXIT':
        Banner()
        print('See you soon..Bye!')
        sys.exit()
        driver.close()
    elif cmd == 'HELP':
        help()
        GetCommands()
    elif cmd == 'ABOUT':
        about()
        GetCommands()
    else:
        print('Error: Invalid Command')
        help()
        GetCommands()
Banner()
help()
GetCommands()
