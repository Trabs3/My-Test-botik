# import requests
# import time


# api_url: str = 'https://api.telegram.org/bot'
# api_dogs_url: str = 'https://random.dog/woof.json'
# bot_token: str = '5958065563:AAEA6zVKsPLoOE4ETy9UBH0ZpTYeNyKQ570'
# error_text: str = 'Yikes!'
# max_counter: int = 10

# offset: int = -2
# counter: int = 0
# cat_response: requests.Response
# cat_link: str
# chat_id: int

# while counter < max_counter:
#     print('attempt=', counter)

#     updates = requests.get(
#         f"{api_url}{bot_token}/getUpdates?offset={offset+1}").json()

#     if updates['result']:
#         for result in updates['result']:
#             offset = result['update_id']
#             chat_id = result['message']['from']['id']
#             cat_response = requests.get(api_dogs_url)
#             if cat_response.status_code == 200:
#                 cat_link = cat_response.json()['url']
#                 requests.get(
#                     f"{api_url}{bot_token}/sendPhoto?chat_id={chat_id}&photo={cat_link}")
#             else:
#                 requests.get(
#                     f"{api_url}{bot_token}/sendMessage?chat_id={chat_id}&text={error_text}")

#     time.sleep(1)
#     counter += 1

import requests
import time


api_url: str = 'https://api.telegram.org/bot'
api_fox_url: str = 'https://randomfox.ca/floof/'
bot_token: str = '5958065563:AAEA6zVKsPLoOE4ETy9UBH0ZpTYeNyKQ570'
offset: int = 2
updates: dict
chat_id: int
timeout: int = 100
text: str


def do_something() -> None:
    print("There was Update")


while True:
    start_time = time.time()
    updates = requests.get(
        f"{api_url}{bot_token}/getUpdates?offset={offset+1}&timeout={timeout}").json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            text = result['message']['text']
            chat_id = result['message']['from']['id']
            do_something()
        requests.get(
            f"{api_url}{bot_token}/sendMessage?chat_id={chat_id}&text={text}")

    time.sleep(3)
    end_time = time.time()
    print(f"Time between inquiries: {end_time - start_time}")
