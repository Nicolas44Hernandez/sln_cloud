# SLN Web server
Smart Local Networks web server 

# OS installation

You can use the [Raspberry Pi Imager](https://www.raspberrypi.com/software/) to flash the last 64-bit Bullseye ligth version (no desktop)

# Initial setup

Use raspi-config to configure the RPI

```bash
sudo raspi-config
```
- Configure the SSH interface

## Update OS

```bash
sudo apt update
sudo apt upgrade
```

## Install and configure git

```bash
sudo apt install git
git config --global user.name "<USER>"
git config --global user.email <EMAIL>
```

## Clone repository
```bash
git clone git@github.com:Nicolas44Hernandez/sln_cloud.git
```

# Projet Setup 

## Install docker
Follow the [docker RPI installation tutorial](https://www.raspberrypi-france.fr/installer-docker-sur-raspberry-pi/)

## Install nginx
Follow the [NGINX RPI installation tutorial](https://www.themoderncoder.com/install-nginx-on-raspberry-pi/)

Copy nginx config 
```bash
cd ressources
```

```bash
sudo cp nginx.conf  /etc/nginx/sites-available/sln
sudo ln -s /etc/nginx/sites-available/eip /etc/nginx/sites-enabled/sln
```   

To test nginx config:
```bash
sudo nginx -t
``` 
Restart nginx service
```bash
sudo service nginx restart
``` 

# Download mongo for RPI docker image
You can follow the [following link](https://github.com/themattman/mongodb-raspberrypi-docker)

1. Download the tarball:

```bash
wget https://github.com/themattman/mongodb-raspberrypi-docker/releases/download/r7.0.4-mongodb-raspberrypi-docker-unofficial/mongodb.ce.pi4.r7.0.4-mongodb-raspberrypi-docker-unofficial.tar.gz
``` 

2. Load the release
```bash
$ docker load --input mongodb.ce.pi4.r7.0.4-mongodb-raspberrypi-docker-unofficial.tar.gz
```
```
Loaded image: mongodb-raspberrypi4-unofficial-r7.0.4:latest
``` 

3. Verify the Docker image has been loaded
```bash
$ docker images
```
```
REPOSITORY                                TAG       IMAGE ID       CREATED       SIZE
mongodb-raspberrypi4-unofficial-r7.0.4    latest    c04f966fe9e2   5 days ago    468MB
```

# Launch platform

1. Run platform ressources docker compose
```bash
docker compose -f docker-compose-ressources.yml up -d
```
2. Run application docker compose
```bash
docker compose -f docker-compose-application.yml up -d
```

3. Create and seed database
```bash
docker exec -it sln-backend sh -c "python db_manage.py create"
```

To Delete database
```bash
docker exec -it sln-backend sh -c "python db_manage.py delete"
```

# Access webserver 
The web server can be accessed from:
```http://<rpi_ip_address:80>```


# Rebuild docker images
If you want to install a new version is necessary to rebuild the docker images 

Delete current images
```bash
docker image rm sln-backend sln-web-server mongo mongo-express
```

Rebuild images and run service
```bash
docker compose -f docker-compose-ressources.yml up -d
docker compose -f docker-compose-applications.yml up -d
```
