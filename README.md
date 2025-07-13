# 🚀 0gl04q - Backend Developer Landing Page

<img width="1511" height="859" alt="Снимок экрана 2025-07-13 в 17 48 36" src="https://github.com/user-attachments/assets/9cecb568-764d-49c5-b4fb-90fcf7c292a5" />

Персональный лендинг backend разработчика с современным дизайном и функциональностью отправки сообщений через Telegram.

## 📋 Описание

Это веб-приложение представляет собой персональный лендинг для backend разработчика с именем 0gl04q. Сайт включает в себя:

- **Персональную информацию** о разработчике
- **Портфолио проектов** с описанием технологий
- **Технологический стек** с визуальными индикаторами уровня владения
- **Контактную форму** с отправкой сообщений в Telegram
- **Адаптивный дизайн** для всех устройств
- **Анимации и интерактивные элементы**

Ссылка на лендинг - https://0gl04q.ru

## 🛠️ Технологии

### Backend
- **Python 3.12** - основной язык программирования
- **Flask** - веб-фреймворк
- **Pydantic** - валидация данных
- **Telegram Bot API** - отправка сообщений
- **Gunicorn** - WSGI сервер для продакшена

### Frontend
- **HTML5** - структура страницы
- **CSS3** - стилизация с анимациями
- **JavaScript** - интерактивность
- **Responsive Design** - адаптивность

### DevOps
- **Docker** - контейнеризация
- **Docker Compose** - оркестрация контейнеров
- **Amvera** - конфигурация для деплоя

## 🚀 Быстрый старт

### Предварительные требования

- Python 3.12+
- Docker и Docker Compose (опционально)
- Telegram Bot Token

### Установка и запуск

#### Локальная разработка

1. **Клонируйте репозиторий:**
```bash
git clone <repository-url>
cd blog
```

2. **Создайте виртуальное окружение:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows
```

3. **Установите зависимости:**
```bash
pip install -r requirements.txt
```

4. **Настройте переменные окружения:**
Создайте файл `.env` в корневой директории:
```env
TG_BOT_TOKEN=your_telegram_bot_token
TG_CHAT_ID=your_telegram_chat_id
```

5. **Запустите приложение:**
```bash
gunicorn --reload -w 4 -b 0.0.0.0:5000 src.app:app
```

Приложение будет доступно по адресу: http://0.0.0.0:5000

#### Запуск через Docker

1. **Создайте файл `.env`:**
```env
TG_BOT_TOKEN=your_telegram_bot_token
TG_CHAT_ID=your_telegram_chat_id
```

2. **Запустите через Docker Compose:**
```bash
docker compose up --build
```

Приложение будет доступно по адресу: http://localhost:8000

## 📁 Структура проекта

```
blog/
├── src/
│   ├── app.py          # Основное Flask приложение
│   ├── config.py       # Конфигурация и настройки
│   └── message.py      # Логика работы с сообщениями
├── static/
│   ├── style.css       # Стили приложения
│   └── script.js       # JavaScript функциональность
├── templates/
│   └── index.html      # Главная страница
├── Dockerfile          # Конфигурация Docker
├── docker-compose.yml  # Docker Compose конфигурация
├── amvera.yml         # Конфигурация для Amvera
├── requirements.txt    # Python зависимости
└── README.md          # Документация
```

## 🔧 Конфигурация

### Переменные окружения

| Переменная | Описание | Обязательная |
|------------|----------|--------------|
| `TG_BOT_TOKEN` | Токен Telegram бота | Да |
| `TG_CHAT_ID` | ID чата для отправки сообщений | Да |

## 🚀 Деплой

### Amvera

Проект готов к деплою на Amvera. Конфигурация находится в файле `amvera.yml`.

### Другие платформы

Проект можно развернуть на любой платформе, поддерживающей Docker:
