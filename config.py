TOKEN = '5160849707:AAF1jh1GvbNlYJS8YTIEwEvKHqNJdsrYLMk'
URL_APP = 'https://nemesiscosmopolisbot.herokuapp.com/'

with open('badwords.txt', 'r', encoding='utf-8') as file:
    LIST_BAD_WORDS = [i[:-1] for i in file.readlines()]
