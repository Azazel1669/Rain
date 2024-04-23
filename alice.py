from requests import get, post

print(get('http://localhost:8080/api/fan').json())

id = 1
print(get(f'http://localhost:8080/api/fan/{id}').json())

print(post('http://localhost:8080/api/fan', json={}).json())

print(post('http://localhost:8080/api/fan',
           json={'title': 'Заголовок'}).json())

print(post('http://localhost:8080/api/fan',
           json={'title': 'Header',
                 'content': 'News text',
                 'user_id': 1,
                 'is_private': False}).json())