#Jangan Di ubah ubah  cuk kodennya nanti erorr
#Impor
from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon.errors import SessionPasswordNeededError
from bs4 import BeautifulSoup
from time import sleep
import requests, json, re, sys, os
import colorama
from colorama import Fore, Back, Style

#warna
colorama.init(autoreset=True)
hijau = Style.RESET_ALL+Style.BRIGHT+Fore.GREEN
hijau2 = Style.NORMAL+Fore.GREEN
putih = Style.RESET_ALL
abu = Style.DIM+Fore.WHITE
ungu = Style.RESET_ALL+Style.BRIGHT+Fore.YELLOW
ungu2 = Style.NORMAL+Fore.MAGENTA
yellow = Style.RESET_ALL+Style.BRIGHT+Fore.YELLOW
yellow2 = Style.NORMAL+Fore.YELLOW
red = Style.RESET_ALL+Style.BRIGHT+Fore.RED
red2 = Style.NORMAL+Fore.RED

####Banner Start#####
# Colors
R='\033[31m'
G='\033[32m'
Y='\033[33m'
B='\033[34m'
W='\033[37m'
print(Y + '''
____                   ____         _
|  _ \  ___   __ _  ___| __ )  ___ | |_
| | | |/ _ \ / _` |/ _ \  _ \ / _ \| __|
| |_| | (_) | (_| |  __/ |_) | (_) | |_
|____/ \___/ \__, |\___|____/ \___/ \__|
             |___/
''')
print(G + "Modded by Hidden Anonymous" + R + "\n{ Crack the system }" + W + "\n")
#####BannerEnd#####

#Sistem_Script
if not os.path.exists('session'):
    os.makedirs('session')

api_id = '3558617'
api_hash = 'ccb2e543a3c261d1eca6d4446f097901'
phone_number = input("Enter your phone: ")

client = TelegramClient('session/'+phone_number,api_id,api_hash)
client.connect()
if not client.is_user_authorized():
    try:
        client.send_code_request(phone_number)
        me = client.sign_in(phone_number,input('{}Enter your code: {}>>{} '.format(hijau,abu,putih)))
    except SessionPasswordNeededError:
        password = input('{}Masukan Password 2fa Anda {}>>{} '.format(hijau,abu,putih))
        me = client.start(phone_number,password)

channel_username = '@Dogecoin_Click_bot'

c = requests.session()

ua = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}

channel_entity = client.get_entity(channel_username)
try:
    for ulang in range(999999999):
        sys.stdout.write('\r                                                        \r')
        sys.stdout.write('\r{}Trying to get URL'.format(yellow2))
        client.send_message(entity=channel_entity,message='🖥 Visit sites')
        sleep(3)
        message_history = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
        channel_id = message_history.messages[0].id
        if message_history.messages[0].message.find('Sorry, there are no new ads available.') != -1:
            sys.stdout.write('\r                                                     \r')
            sys.stdout.write('\r{}The ad has ended, please try again later\n'.format(red2))
            break
        url = message_history.messages[0].reply_markup.rows[0].buttons[0].url
        sys.stdout.write('\r                                                     \r')
        sys.stdout.write('\r{}Visit To URL {}'.format(yellow2,putih)+url)

        r = c.get(url,headers=ua)
        soup = BeautifulSoup(r.text,"html.parser")

        if soup.find('div',class_='g-recaptcha') is None and soup.find('div',id='headbar') is None:
            sleep(2)
            message_history = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
            message = message_history.messages[0].message
            sys.stdout.write('\r                                                     \r')
            sys.stdout.write('\r'+yellow+message)
            if message_history.messages[0].message.find('Please stay on') != -1 or message_history.messages[0].message.find('You must stay') != -1:
                timer = re.findall(r'([\d.]*\d+)',message)
                sleep(int(timer[0]))
                sleep(3)
                message_history = client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0,add_offset=0, hash=0))
                sys.stdout.write('\r                                                     \r')
                sys.stdout.write('\r{}'.format(hijau)+message_history.messages[0].message+'\n')

        elif soup.find('div',id='headbar') is not None:
            for data in soup.find_all('div',class_='container-fluid'):
                code = data.get('data-code')
                timer = data.get('data-timer')
                token = data.get('data-token')
                sleep(int(timer))
                r = c.post('https://dogeclick.com/reward',data={'code': code, 'token': token},headers=ua)
                jsn = json.loads(r.text)
                sys.stdout.write('\r                                                     \r')
                sys.stdout.write(hijau+"\rYou earned "+jsn['reward']+" Doge for visiting sites\n")
        else:
            sys.stdout.write('\r                                                     \r')
            sys.stdout.write(red+'\rCaptcha detected')
            sleep(2)
            client(GetBotCallbackAnswerRequest(channel_username,channel_id,data=message_history.messages[0].reply_markup.rows[1].buttons[1].data))
            sys.stdout.write('\r                                                     \r')
            print (red+'\rSkip Captcha successfully\n')

except:
    print(red+"Error detected")
    sys.exit()