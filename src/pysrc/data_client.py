import requests
from typing import Any, TypedDict
from enum import Enum

class Side(Enum):
    BUY = 0
    SELL = 1

class Trade(TypedDict):
    timestampms: int
    id: int
    price: float
    volume: float
    side: Side


class DataClient:
    def __init__(self) -> None:
        self.raw_data: list[dict[str, Any]] = []
        self.parsed_data: list[Trade] = []

    def _query_api(self) -> None:
        base_url = "https://api.gemini.com/v1"
        response = requests.get(base_url + "/trades/btcusd")
        self.raw_data = response.json()

    def _parse_message(self, message: dict[str, Any]) -> Trade:
        # data 'validation'
        if "timestampms" not in message:
            raise ValueError("Missing required field: 'timestampms'")
        if "tid" not in message:
            raise ValueError("Missing required field: 'tid'")
        if "price" not in message:
            raise ValueError("Missing required field: 'price'")
        if "amount" not in message:
            raise ValueError("Missing required field: 'amount'")
        if "type" not in message:
            raise ValueError("Missing required field: 'type'")

        return Trade(
            timestampms=message["timestampms"],
            id=message["tid"],
            price=float(message["price"]),
            volume=float(message["amount"]),
            side=Side.BUY if message["type"] == "buy" else Side.SELL
        )

    def get_data(self) -> list[Trade]:
        self._query_api()
        self.parsed_data = [self._parse_message(msg) for msg in self.raw_data]
        return self.parsed_data
