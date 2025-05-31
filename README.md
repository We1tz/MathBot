# AI Calculator

Небольшое веб-приложение для решения математических задач с помощью OpenRouter (MistralAI) + Prompt Engineering. 

## 🚀 Возможности

- Решение математических задач с пошаговым объяснением.
- Поддержка LaTeX для красивого отображения формул.
- Простой и современный дизайн.
- Быстрый старт на Flask.

---

## 🔧 Установка и запуск

1️⃣ Клонируйте репозиторий:
```bash
git clone https://github.com/We1tz/MathBot.git
cd MathBot
```

2️⃣ Создайте виртуальное окружение:
```bash
python3 -m venv .venv
source .venv/bin/activate  # для macOS/Linux
.venv\Scripts\activate     # для Windows
```

3️⃣ Установите зависимости:
```bash
pip install -r requirements.txt
```

4️⃣ Создайте файл `.env` в корне проекта:
```
OPENROUTER_TOKEN=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXX
```
👉 Замените `sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXX` на свой токен OpenRouter.

5️⃣ Запустите приложение:
```bash
python app.py
```

6️⃣ Перейдите в браузере на:
```
http://127.0.0.1:5000/
```

---

## 📚 Зависимости

Ниже приведён список библиотек, используемых проектом:
```
anyio==4.9.0
blinker==1.9.0
certifi==2025.4.26
click==8.2.1
dotenv==0.9.9
Flask==3.1.1
h11==0.16.0
httpcore==1.0.9
httpx==0.28.1
idna==3.10
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.2
python-dotenv==1.1.0
sniffio==1.3.1
typing_extensions==4.13.2
Werkzeug==3.1.3
```

👉 Чтобы обновить список зависимостей:
```bash
pip freeze > requirements.txt
```

---

## 📌 Примечания

- Для работы требуется актуальный токен OpenRouter.
- Если вы вносите изменения в зависимости, не забудьте обновить `requirements.txt`.
- Проект рассчитан на Python 3.8+.

---

## 💻 Авторы

👤 [We1tz](https://github.com/We1tz)

---

