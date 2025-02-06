# Запуск

```bash
docker build -t hello_v1.1 . сборка образа 

docker run -d -p 5051:8000 hello_v1.1 запуск контейнера 

http://localhost:5051/api/up/ обращение к серверу 

GET http://localhost:8000/api/up/ API запрос
Accept: application/json


