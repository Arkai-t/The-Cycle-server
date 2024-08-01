# The Cycle servers

This project aims to recreate the backend servers for The Cycle (2018).

## Structure

In this project you have currently two servers :

- [`tcpserver.py`](./tcpserver.py) : Basic TCP server that currently only listen request from the game, I believe this is for the inventory/stats management. The IP of that server can be overwrite with one of these game lauch option `-auth 127.0.0.1 -backend 127.0.0.1`. Listen the port `28194`.
- [`cloudfareserver.py`](./cloudfareserver.py) : Cloudfare authentification server. IP `162.159.134.234` Port `443`. It needs to be overwritted and I think we need to bybass the TLS.

## Project progress

- [x] Listen the game
- [ ] Answer something coherent
- [ ] Play ?

## Usage

I use [Python 3.12](https://www.python.org/downloads/release/python-3124/), but it can be compatible with other version.

```
pip install -r requirements.txt
```

## Run the server

```
python tcpserver.py
```

