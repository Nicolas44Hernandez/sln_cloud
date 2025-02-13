# backend

## Launch in dev post
* Install venv manager
```sh
apt install python3.10-venv
```

* Create and activate venv

```sh
python3 -m venv venv
source venv/bin/activate
```

* Install requirements
```sh
pip install -r requirements.txt
```

* Run app
```sh
export FLASK_APP="server/app:create_app()"
export FLASK_ENV="PRODUCTION"
flask run --host '0.0.0.0'
```

## Dockerize  application

```sh
cd backend
docker build -t sln-backend .
```
