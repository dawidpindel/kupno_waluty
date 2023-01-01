import requests

body = requests.get('http://api.nbp.pl/api/exchangerates/tables/A/ ')
response = body.json()
currency = input('Jaką walute chcesz wymienić [USD/EUR/CHF]:')
quantity = int(input('Ile waluty chcesz wymienić:'))

for rate in response[0]['rates']:
    if currency == rate['code']:
        result = quantity * float(rate['mid'])
        print(f'W rezultacie otrzymasz {result}.')
        break
