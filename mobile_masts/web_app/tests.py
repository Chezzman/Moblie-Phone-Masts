from django.test import Client
c = Client()
response = c.post('/login/', {'username': 'john', 'password': 'smith'})
response.status_code

response = c.get('/customer/details/')
response.content
