# Локальный запуск проекта
```bash
gunicorn --reload -w 4 -b 0.0.0.0:8000 src.app:app
```

# Запуск проекта в Docker
```bash
docker compose up --build
```