
![IT Polygon Logo](.github/images/logo.png)
# How to start
Install the `make` utility:
```
sudo apt install make
```
Change local.env -> .env

Create application in the Docker:
```
make app
make migrations
make migrate
```

Collect static and create fixtures data
```
make collectstatic
make data
```
# Open Django Backend

Run application: http://127.0.0.1:8000/

# Local development
```
python -m venv venv
source venv/bin/activate
poetry install
make app
```
