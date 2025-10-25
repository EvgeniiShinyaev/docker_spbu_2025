1) Проверить, что установлен **Docker** и **Docker Compose**  
(проверить: `docker --version` и `docker compose version`).
2) Склонировать репозиторий
3) Запустить систему 
docker compose up -d --build
4) Проверить, что оба контейнера работают
docker compose ps
Ожидаемый результат — контейнеры demo_db и demo_app в статусе Up.

Проверка работы API.
5) Проверить, что сервис отвечает
curl http://localhost:8000/
Ответ: {"status":"ok","message":"API entry point"}
6) Получить список пользователей
curl http://localhost:8000/users
Ответ: [{"id":1,"name":"Alice"},{"id":2,"name":"Bob"},{"id":3,"name":"Charlie"}]
7) Добавить нового пользователя
curl "http://localhost:8000/add?name=Eugene"
8) Снова проверить список
curl http://localhost:8000/users

9) Проверить персистентность данных
docker compose down
docker compose up -d
curl http://localhost:8000/users
Новый пользователь останется в базе данных


