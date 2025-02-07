import time
import pandas as pd
from tqdm import tqdm
from pysrc.data_client import DataClient, Side
from pysrc.lasso_model import LassoModel

client = DataClient()
model = LassoModel()

time_sleep_sec = 10


def fetch_and_process_data() -> None:
    while True:
        test_data = client.get_data()
        parsed_data = [
            (trade["price"], trade["volume"], trade["side"] == Side.BUY)
            for trade in test_data
        ]

        if parsed_data:
            model.add_tick(parsed_data)
            break

        time.sleep(time_sleep_sec)


for _ in tqdm(range(11)):
    fetch_and_process_data()

num_predictions = 10
for _ in tqdm(range(num_predictions)):
    model.predict()
    fetch_and_process_data()

targets = pd.read_csv("src/pysrc/targets.csv")
predictions = pd.read_csv("src/pysrc/predictions.csv")

data = pd.concat([targets, predictions], axis=1)
correlation = data["target"].corr(data["prediction"])

print(f"Correlation: {correlation:.5f}")
