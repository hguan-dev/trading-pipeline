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

    @patch("pysrc.data_client.requests.get")
    def test_get_data(self, mock_get: MagicMock) -> None:
        mock_api_response = [
            {
                "timestampms": 15151515,
                "tid": 6969696969,
                "price": "420.69",
                "amount": "3.1415",
                "type": "buy",
            }
        ]

        mock_get.return_value.json.return_value = mock_api_response

        result = self.client.get_data()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["price"], 420.69)
        self.assertEqual(result[0]["side"], Side.BUY)
