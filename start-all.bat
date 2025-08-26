@echo off
REM Запуск виртуального окружения и backend Django
cd backend
call ..\venv\Scripts\activate.bat
start cmd /k "python manage.py runserver"
cd ..
REM Запуск фронтенда (Vite dev server)
cd frontend
start cmd /k "npm run dev"
cd ..
REM Открыть сайт в браузере (можно изменить порт, если нужно)
start http://localhost:5173
