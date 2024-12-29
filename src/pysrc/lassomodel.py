from typing import List, Tuple, Any
from pysrc.data_client import DataClient, Side 
from pysrc import intern  # type: ignore
from sklearn.linear_model import Lasso # type: ignore 

class FeatureTrainer:
    def __init__(self, alpha: float = 0.1, train_length: int = 10):
        self.data_client = DataClient()
        self.alpha = alpha
        self.train_length = train_length
        self.features_computers: List[Any] = [
            intern.NTradesFeature(),
            intern.PercentBuyFeature(),
            intern.PercentSellFeature(),
            intern.FiveTickVolumeFeature()
        ]  
        self.X: List[List[float]] = [] 
        self.Y: List[float] = []
        self.model = Lasso(alpha=self.alpha)

    def fetch_and_transform_data(self) -> List[Tuple[float, float, bool]]:
        """
        Fetch trade data from the data client and transform it to the required format.
        """
        raw_trades = self.data_client.get_data()

        transformed_trades = [
            (trade["price"], trade["volume"], trade["side"] == Side.BUY)
            for trade in raw_trades
        ]

        return transformed_trades

    def compute_features(self, trades: List[Tuple[float, float, bool]]) -> List[float]:
        features = []
        for feature_computer in self.features_computers:
            features.append(feature_computer.compute_feature(trades))  # Compute each feature

        return features 

    def compute_target(self, trades: List[Tuple[float, float, bool]]) -> float:
        if len(trades) < 2:
            return 0.0 

        current_price = trades[-1][0]
        future_price = trades[-2][0]
        return (current_price - future_price) / future_price

    def add_data(self, features: List[float], target: float) -> None:
        self.X.append(features)
        self.Y.append(target)
        
        # Keep only the latest `train_length` data points
        if len(self.X) > self.train_length:
            self.X.pop(0)
            self.Y.pop(0)

    def train(self) -> None:
        """
        Train the Lasso model using the accumulated data.
        """
        if len(self.X) < self.train_length:
            raise ValueError("Not enough data to train. Need at least 10 pairs.")
        self.model.fit(self.X, self.Y)

    def predict(self, features: List[float]) -> float:
        if len(self.X) < self.train_length:
            raise ValueError("Not enough data to make a prediction. Need at least 10 pairs.")
        return self.model.predict([features])[0]

    def process_and_predict(self) -> None:
        trades = self.fetch_and_transform_data()
        features = self.compute_features(trades)
        target = self.compute_target(trades)
        self.add_data(features, target)

        if len(self.X) >= self.train_length:
            self.train()
            prediction = self.predict(features)
            print(f"Prediction: {prediction}")

