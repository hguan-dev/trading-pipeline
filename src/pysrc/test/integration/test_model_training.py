import pytest
import time
from pysrc.data_client import DataClient, Side
from pysrc.lasso_model import LassoModel


@pytest.mark.integration
def test_model_training_inference() -> None:
    """
    Integration test for DataClient fetching data and feeding it into LassoModel.
    """

    client = DataClient()
    model = LassoModel()

    for i in range(10):
        test_data = client.get_data()
        assert isinstance(test_data, list), "DataClient should return a list"
        assert len(test_data) > 0, "No trade data received from API"

        parsed_data = [
            (trade["price"], trade["volume"], trade["side"] == Side.BUY)
            for trade in test_data
        ]
        model.add_tick(parsed_data)

        assert (
            model.predict() is None
        ), "Model should return None before training data accumulates"
        time.sleep(0.25)

    for i in range(10):
        test_data = client.get_data()
        assert isinstance(test_data, list), "DataClient should return a list"
        assert len(test_data) > 0, "No trade data received from API"

        parsed_data = [
            (trade["price"], trade["volume"], trade["side"] == Side.BUY)
            for trade in test_data
        ]
        model.add_tick(parsed_data)

        # Expect predictions after training
        prediction = model.predict()
        assert (
            prediction is not None
        ), "Model should return a valid prediction after training"
        time.sleep(0.25)

