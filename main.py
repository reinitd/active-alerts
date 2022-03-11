import os
import json
from colorama import init, Style, Fore, Back
from urllib.request import urlopen

'''
SCRAPPED
'''


os.system('cls|clear')

init(autoreset=True)

apistatusUrl = "https://api.weather.gov/"
statusRespone = urlopen(apistatusUrl)
statusData = json.load(statusRespone)

status = statusData['status']
print(f'''
{Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}] Only grabs the first alert found, if no alert found then throws error.{Fore.RESET}
{Style.BRIGHT}API STATUS: {Style.RESET_ALL}{Fore.BLUE}{status}
      ''')
state = input(f'{Style.DIM}State Initials:{Style.RESET_ALL} ').upper()

apiUrl = "https://api.weather.gov/alerts/active?area=" + state
respone = urlopen(apiUrl)
data = json.load(respone)
print(state)



'''
Dictionary type beat
'''
TITLE = data['title']
UPDATED = data['updated']
AREA = data['features'][0]['properties']['areaDesc']
EVENT = data['features'][0]['properties']['event']
SEVERITY = data['features'][0]['properties']['severity']
CERTAINTY = data['features'][0]['properties']['certainty']
URGENCY = data['features'][0]['properties']['urgency']
RESP = data['features'][0]['properties']['response']
TYPE = data['features'][0]['properties']['@type']
CAT = data['features'][0]['properties']['category']
HEADLINE = data['features'][0]['properties']['headline']
DESC = data['features'][0]['properties']['description']
INSTRUCTION = data['features'][0]['properties']['instruction']

SENT = data['features'][0]['properties']['sent']
EFFECT = data['features'][0]['properties']['effective']
ONSET = data['features'][0]['properties']['onset']
EXPIRES = data['features'][0]['properties']['expires']
ENDS = data['features'][0]['properties']['ends']
SSTATUS = data['features'][0]['properties']['status']

SENDER = data['features'][0]['properties']['sender']
SENDERNAME = data['features'][0]['properties']['senderName']

######

os.system('cls|clear')

print(f'''
      
{Style.BRIGHT}API Status:{Style.RESET_ALL} {Fore.BLUE}{status}{Style.RESET_ALL}
{Style.DIM}{Fore.GREEN}{apiUrl}{Style.RESET_ALL}
  
{Style.BRIGHT}{Fore.BLUE}{TITLE}{Style.RESET_ALL}
{Style.BRIGHT}Updated:{Style.RESET_ALL} {Style.DIM}{UPDATED}{Style.RESET_ALL}
  
{Style.BRIGHT}{Fore.BLUE}Areas affected with {EVENT}:{Style.RESET_ALL}
{AREA}

      
{Style.BRIGHT}{Fore.BLUE}{HEADLINE}{Style.RESET_ALL}

{Style.BRIGHT}{Fore.BLUE}Basic information:{Style.RESET_ALL}
{Fore.MAGENTA}[{Fore.MAGENTA}{Style.DIM}!{Style.RESET_ALL}{Fore.MAGENTA}] Type...........:{Style.RESET_ALL} {TYPE}
{Fore.MAGENTA}[{Fore.MAGENTA}{Style.DIM}!{Style.RESET_ALL}{Fore.MAGENTA}] Category.......:{Style.RESET_ALL} {CAT}
{Fore.MAGENTA}[{Fore.MAGENTA}{Style.DIM}!{Style.RESET_ALL}{Fore.MAGENTA}] Certainty......:{Style.RESET_ALL} {CERTAINTY}
{Fore.MAGENTA}[{Fore.MAGENTA}{Style.DIM}!{Style.RESET_ALL}{Fore.MAGENTA}] Severity.......:{Style.RESET_ALL} {SEVERITY}
{Fore.MAGENTA}[{Fore.MAGENTA}{Style.DIM}!{Style.RESET_ALL}{Fore.MAGENTA}] Urgency........:{Style.RESET_ALL} {URGENCY}
{Fore.MAGENTA}[{Fore.MAGENTA}{Style.DIM}!{Style.RESET_ALL}{Fore.MAGENTA}] Response.......:{Style.RESET_ALL} {RESP}
{Fore.MAGENTA}[{Fore.MAGENTA}{Style.DIM}!{Style.RESET_ALL}{Fore.MAGENTA}] Instruction(s).:{Style.RESET_ALL} {INSTRUCTION}

{Style.BRIGHT}{Fore.BLUE}Time information:{Style.RESET_ALL}
{Fore.MAGENTA}[{Fore.MAGENTA}{Style.DIM}!{Style.RESET_ALL}{Fore.MAGENTA}] Sent...........:{Style.RESET_ALL} {SENT}
{Fore.MAGENTA}[{Fore.MAGENTA}{Style.DIM}!{Style.RESET_ALL}{Fore.MAGENTA}] Effective......:{Style.RESET_ALL} {EFFECT}
{Fore.MAGENTA}[{Fore.MAGENTA}{Style.DIM}!{Style.RESET_ALL}{Fore.MAGENTA}] Onset..........:{Style.RESET_ALL} {ONSET}
{Fore.MAGENTA}[{Fore.MAGENTA}{Style.DIM}!{Style.RESET_ALL}{Fore.MAGENTA}] Expires........:{Style.RESET_ALL} {EXPIRES}
{Fore.MAGENTA}[{Fore.MAGENTA}{Style.DIM}!{Style.RESET_ALL}{Fore.MAGENTA}] Ends...........:{Style.RESET_ALL} {ENDS}
{Fore.MAGENTA}[{Fore.MAGENTA}{Style.DIM}!{Style.RESET_ALL}{Fore.MAGENTA}] Alert Status...:{Style.RESET_ALL} {SSTATUS}

{Style.BRIGHT}{Fore.BLUE}Sender information:{Style.RESET_ALL}
{Fore.MAGENTA}[{Fore.MAGENTA}{Style.DIM}!{Style.RESET_ALL}{Fore.MAGENTA}] Sender.........:{Style.RESET_ALL} {SENDER}
{Fore.MAGENTA}[{Fore.MAGENTA}{Style.DIM}!{Style.RESET_ALL}{Fore.MAGENTA}] Sender Name....:{Style.RESET_ALL} {SENDERNAME}

      
{Style.BRIGHT}{Fore.BLUE}NWS Description:{Style.RESET_ALL}
{DESC}
  ''')


