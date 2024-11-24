from unittest import TestCase
from unittest.mock import MagicMock, patch
from pysrc.data_client import DataClient, Side, Trade


class TestDataClient(TestCase):
    def setUp(self) -> None:
        self.client = DataClient()

    def test_parse_message(self) -> None:
        mock_message = {
            "timestampms": 15151515,
            "tid": 6969696969,
            "price": "420.69",
            "amount": "3.1415",
            "type": "buy",
        }

        expected_trade = Trade(
            timestampms=15151515,
            id=6969696969,
            price=420.69,
            volume=3.1415,
            side=Side.BUY,
        )

        parsed_trade = self.client._parse_message(mock_message)
        self.assertEqual(parsed_trade, expected_trade)

    @patch.object(DataClient, "_query_api")
    def test_get_data(self, mock_query_api: MagicMock) -> None:
        mock_query_api.return_value = None 
        self.client.raw_data = [
            {
                "timestampms": 15151515,
                "tid": 6969696969,
                "price": "420.69",
                "amount": "3.1415",
                "type": "buy",
            }
        ]

        result = self.client.get_data()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["price"], 420.69)
        self.assertEqual(result[0]["side"], Side.BUY)

