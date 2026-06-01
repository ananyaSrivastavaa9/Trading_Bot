import os
import time
import hmac
import hashlib
from urllib.parse import urlencode

import requests
from dotenv import load_dotenv

from bot.logging_config import get_logger

load_dotenv()
logger = get_logger()

class BinanceClient:
    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")
        self.base_url = os.getenv("BASE_URL", "https://testnet.binancefuture.com")
        self.session = requests.Session()
        self.session.headers.update({"X-MBX-APIKEY": self.api_key})

        if not self.api_key or not self.api_secret:
            raise ValueError("API key or secret missing in .env")

    def _sign_params(self, params: dict) -> dict:
        params["timestamp"] = int(time.time() * 1000)
        query_string = urlencode(params)
        signature = hmac.new(
            self.api_secret.encode(),
            query_string.encode(),
            hashlib.sha256
        ).hexdigest()
        params["signature"] = signature
        return params

    def place_order(self, symbol, side, order_type, quantity, price=None):
        endpoint = "/fapi/v1/order"
        url = self.base_url + endpoint

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
            "recvWindow": 5000,
        }

        if order_type == "LIMIT":
            params["timeInForce"] = "GTC"
            params["price"] = price

        signed_params = self._sign_params(params)

        logger.info(f"REQUEST URL: {url}")
        logger.info(f"REQUEST PARAMS: {signed_params}")

        try:
            response = self.session.post(url, params=signed_params, timeout=10)
            logger.info(f"RESPONSE STATUS: {response.status_code}")
            logger.info(f"RESPONSE TEXT: {response.text}")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"REQUEST ERROR: {str(e)}")
            raise