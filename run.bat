call ".\venv\Scripts\activate.bat"
@REM set DATABASE_URL=postgres://postgres:postgres@127.0.0.1:5432/vmalldb
uvicorn main:app --reload