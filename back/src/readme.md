source venv/bin/activate

pip install -r src/requirements.txt

uvicorn main:app --reload

docker build -t simple-fastapi-app .

docker run -p 8000:8000 simple-fastapi-app

# Source - https://stackoverflow.com/a/72928176
# Posted by Thomas Anderson
# Retrieved 2026-04-19, License - CC BY-SA 4.0

docker save my/local-image:v1.2.3 | sudo k3s ctr images import -
docker save fastapi-backend:latest | sudo k3s ctr images import -

--------------------------

docker build -t fastapi-backend:latest .

docker save fastapi-backend:latest -o fastapi-backend.tar

sudo k3s ctr images import fastapi-backend.tar

sudo k3s ctr images list | grep fastapi


--clear commands

sudo k3s crictl images

sudo k3s crictl rmi --prune

sudo k3s crictl ps -a

sudo k3s crictl rm $(sudo k3s crictl ps -a -q)

sudo du -h /var/log/containers | sort -h | tail -20
sudo journalctl --vacuum-size=500M

-- node status
kubectl describe node | grep -A5 "Conditions"
kubectl get pods -A -o wide

--ubuntu clear

sudo apt clean
sudo apt autoclean
sudo apt autoremove --purge

rm -rf ~/.cache/*
rm -rf ~/.cache/thumbnails/*

------------------------------