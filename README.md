# Putter

A tiny server for uploading files using HTTP PUT.

## Install

Put this somewhere.

```
virtualenv env
env/bin/pip install -r requirements.txt
```

Configure `putter.cfg`

```
ASSET_ROOT="/var/www/assets/"
SERVER_NAME="localhost:5000"
```

## Test

```
PUTTER_SETTINGS=putter.cfg env/bin/python put.py
```

## Doing it properly

Install to `/opt/gamernetwork/putter/`

```
cp putter.cfg-example /etc/putter.cfg
```

Install under supervisord.

```
apt-get install supervisor
cp supervisor.conf-example /etc/supervisor/conf.d/putter.conf
vi /etc/supervisor/conf.d/putter.conf # at very least make <host> and <port> sensible
mkdir /var/log/gamernetwork/
touch /var/log/gamernetwork/putter.log
chown www-data /var/log/gamernetwork/putter.log
supervisorctl reload
```

Should be running at this point.

