source venv/bin/activate

pip install -r src/requirements.txt

uvicorn main:app --reload

