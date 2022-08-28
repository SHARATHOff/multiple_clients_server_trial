#smsnumb = input("Input the number of the target: ")
#message = input("Please input the message: ")
import requests
resp = requests.post('https://textbelt.com/text', {
            'phone': '7373854499',
            'message': 'hello rudnesh iam sharath if we recived this message send me a whatsapp message ',
            'key': 'textbelt',})
print(resp.json())