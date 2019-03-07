# ccxt-websockets

Just the transpiled files from [CCXT lfern/websockets-multiple fork](https://github.com/lfern/ccxt/tree/feature/websockets-multiple), to speed up installation.

For a practical example on how to use this in a python project, check [ccxt-websockets-db-updater](https://github.com/firepol/ccxt-websockets-db-updater)

Check also the main thread about websockets in the official CCXT project:  
[Streaming (WS, Websocket support): Orderbooks, Trades, Balances...](https://github.com/ccxt/ccxt/issues/56)

## Usage

To use this already transpiled lfern websockets powered branch of CCXT in your project, add in your project `requirements.txt` this line:

```
git+git://github.com/firepol/ccxt-websockets#egg=ccxt&subdirectory=python
```

Then run:

```
pip install -r requirements.txt
```
