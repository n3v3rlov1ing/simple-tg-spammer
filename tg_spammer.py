from telethon import TelegramClient, events
import asyncio

# Enter data from my.telegram.org
api_id = 0
api_hash = ''
client = TelegramClient('anon', api_id, api_hash)


usernames = [''] # Enter username(s) for spam

numbersms = int(input('Enter number of sms for spam (0 - infinite): '))
timer = int(input('Enter time (in sec) between messages: '))
message = input('Enter message for spam: ')

async def main():
    await asyncio.sleep(timer) # k/d (in sec)
    for i in usernames:
        await client.send_message(i, f'{message}')

if numbersms == 0:
    print('[+] Spam started!')
    print(f'[+] K/D - {timer}, number - {numbersms}, message - {message}')
    while True: # Infinite cycle
        with client:
            client.loop.run_until_complete(main())
else:
    print('[+] Spam started!')
    print(f'[+] K/D - {timer}, number - {numbersms}, message - {message}') 
    for i in range(numbersms):
        with client:
                client.loop.run_until_complete(main())