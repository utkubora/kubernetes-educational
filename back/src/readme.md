source venv/bin/activate

pip install -r src/requirements.txt

uvicorn main:app --reload

docker build -t simple-fastapi-app .

docker run -p 8000:8000 simple-fastapi-app