source venv/bin/activate

pip install -r src/requirements.txt

uvicorn main:app --reload

docker build -t simple-fastapi-app .

docker run -p 8000:8000 simple-fastapi-app

# Source - https://stackoverflow.com/a/72928176
# Posted by Thomas Anderson
# Retrieved 2026-04-19, License - CC BY-SA 4.0

docker save my/local-image:v1.2.3 | sudo k3s ctr images import -

