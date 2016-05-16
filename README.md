# Putter

A tiny server for uploading files using HTTP PUT.

## Install

Put this somewhere.

```
virtualenv env
env/bin/pip install -r requirements.txt
```

Configure `setings.cfg`

```
ASSET_ROOT="/var/www/assets/"
SERVER_NAME="localhost:5000"
```

## Run

```
PUTTER_SETTINGS=settings.cfg env/bin/python put.py
```

## Harden

You probably want to run it with supervisord
