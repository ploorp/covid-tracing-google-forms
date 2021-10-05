import sys
import requests
from os import system
from time import sleep

def main():
    while True:
        autofill()
        input('Press [Enter] to restart ')
        clear()

def autofill():
    
    # user info
    first_name = 'Finn'
    last_name = 'Witherup'
    role = 'Student'
    
    while True:
        print('[<day-letter>,<number-of-submissions>,<initial-period>]\n')
        print('Press [Enter] for prompts')
        q1 = input('\n:')
        clear()
        if not q1 == '':
            usr_input = q1.split(',')
        else:
            print('Is today an A or B day? (a/b)')
            q2 = input(':')
            clear()
            if not q2 == 'a' or 'b':
                clear()
                print('--- Error: ' + str(q2) + ' is invalid. ---')
                break
            else:
                print('How many submissions do you want to make? (1-8)')
                q3 = input(':')
                clear()
                if q3 == '1':
                    form_count = 1
                    print('What is the start period? (0-9)')
                    q4 = input(':')
                    clear()
                elif q3 == '8':
                    form_count = 8
                else:
                    clear()
                    print('--- Error: ' + str(q3) + ' is invalid. ---')
                    break
        
        form_url = 'https://docs.google.com/forms/d/1FAIpQLSfAa0T4ToAh5L0g7v60nG_K0bs8xxFV5iMnsmLXBn3skJLZeA/viewform'
        submit_url = form_url.replace('/viewform', '/formResponse')

        # parsing complex input
        if not q1 == '':
            try:
                q2 = usr_input[0]
                q3 = int(usr_input[1])
                q4 = int(usr_input[2])
                if q2.isalpha == True:
                    clear()
                if q3 == '1'or'2'or'3'or'4'or'5'or'6'or'7'or'8'or'9':
                    clear()
                else:
                    clear()
                    print('--- Error: Input is invalid. ---')
                    break
            except:
                clear()
                print('--- Error: Input is invalid. ---')
                break
        if not q4 == '0'or'1'or'2'or'3'or'4'or'5'or'6'or'7'or'8'or'9':
            clear()
            print('--- Error: Input is invalid. ---')
            break

        # inputs
        day_letter = q2
        form_count = int(q3)
        period = q4

        # form entries to submit
        values1 = {
            'entry.969137177': first_name,
            'entry.822148254': last_name,
            'entry.1793748464': '',
            'entry.1336888971': role,
        }
        values3 = {
            'dlut': '1632943105299',
            'hud': 'true',
            'entry.817783632_sentinel': '',
            'fvv': '1',
            'draftResponse': '[null,null,,,&quot;-1199553024199346589&quot;]',
            'pageHistory': '0',
            'fbzx': '-1199553024199346589'
        }

        # schedule
        schedule = {
            #'0': [''],
            '1': [['E31','E31']],
            '2': [['E31','C105+-+Bliss+Gym']],
            '3': [['E1','E1']],
            '4': [['CAFETERIA','CAFETERIA']],
            '5': [['K105','K105']],
            '6': [['G208','G208']],
            '7': [['G111','G111']],
            '8': [['G115','G115']],
            #'9': ['']
        }

        day_letter_binary = 0
        if day_letter == 'b':
            day_letter_binary = 1

        user_agent = {'Referer': form_url,'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}
        form_values = []

        for x in range(form_count):
            for i in schedule[str(period)]:
                final_period = str(period)
                if form_count > 1:
                    period += 1
                form_period = 'Period+' + final_period
                location = i[day_letter_binary]
                values2 = {
                'entry.1082503223': location,
                'entry.817783632': form_period,
                }
                form_values.append(values1)
                form_values.append(values2)
                form_values.append(values3)
                print('\nSubmitting form...\n')
                try:
                    #r = requests.post(submit_url, data=form_values, headers=user_agent)
                    sleep(5)
                    clear()
                    print(str(x + 1) + ' forms Submitted.\n')
                    form_values = []
                    print('Day letter: ' + day_letter + ' - Period: ' + final_period + ' - Location: ' + location + '\n')
                except:
                    clear()
                    print('--- Error: Submission failed. ---')
                finally:
                    break
        break

def clear():
    print('----')
    #system('clear')

main()
