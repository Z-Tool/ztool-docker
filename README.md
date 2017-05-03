# ztool-docker

## System architecture diagram

All services are on a vultr vps server. I use one docker container for each service. And about reference code(python code and frontend code), I use git submodule to connect them.

![diagram](readme_files/diagram.png)

## Docker-compose

### Services

* mongodb
* uwsgi + flask
* nginx

### repositories

#### depends on

* [ztool-backhend-mongo](https://github.com/Z-Tool/ztool-backhend-mongo)
* [ztool-frontend](https://github.com/Z-Tool/ztool-frontend)

## Data Backup

All data is uploaded to [Dropbox](https://www.dropbox.com) and I use [dropbox_uploader.sh](https://github.com/andreafabrizi/Dropbox-Uploader) and crontab to upload every night.
