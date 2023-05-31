import requests

API_ENDPOINT = 'https://api.funtranslations.com/translate/morse.json'

text = input("Enter the sentence you'd like to translate: ")
params = {'text': text}
response = requests.get(url=API_ENDPOINT, params=params)
morse_code = response.json()['contents']['translated']
print(f"The morse code is: {morse_code}")
