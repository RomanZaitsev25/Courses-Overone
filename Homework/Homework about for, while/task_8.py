# Любая ссылка в интернете начинается с "http://www" вводится строка,
# если она начинается с "http://www", то вывести доменную зону пример:
# http://www.paypal.com доменная зона .com,
# иначе вывести "некорректная ссылка"

text = input('Enter the string:')
if text.startswith('http://www') and text.endswith('com'):
    print(True)
else:
    print('Не коректная ссылка')
