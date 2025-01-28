import os
import pprint
import json
from py_clob_client.constants import POLYGON
from py_clob_client.client import ClobClient
from py_clob_client.clob_types import OrderArgs
from py_clob_client.order_builder.constants import BUY

host = "https://clob.polymarket.com"
key = os.getenv("POLYMARKET_PK")
chain_id = POLYGON

# Create CLOB client and get/set API credentials
client = ClobClient(host, key=key, chain_id=chain_id)
client.set_api_creds(client.create_or_derive_api_creds())

resp = client.get_markets()

while resp.get('next_cursor'):
    for m in resp['data']: 
        if not m['closed'] and m['active']:
            for t in m.get("tokens"):
                tId = t.get('token_id')
                if tId:
                    print(f'"{tId}",')

    resp = client.get_markets(next_cursor=resp['next_cursor'])