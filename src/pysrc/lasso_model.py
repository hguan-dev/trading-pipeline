from sklearn.linear_model import Lasso  # type: ignore
from pysrc import intern  # type: ignore
from typing import Any, Optional


class LassoModel:
    def __init__(self) -> None:
        self.reg = Lasso()
        self.X: list[list[Any]] = []
        self.Y: list[list[float]] = []
        self.curr_tick_features: Optional[list[Any]] = None
        self.curr_tick_midprice: Optional[float] = None
        self.ntf = intern.NTradesFeature()
        self.ptf = intern.PercentBuyFeature()
        self.psf = intern.PercentSellFeature()
        self.vf = intern.FiveTickVolumeFeature()

    def add_tick(self, tick: list[tuple[float, float, bool]]) -> None:
        if self.curr_tick_features is not None:
            self.X.append(self.curr_tick_features)

        features = []
        features.append(self.ntf.compute_feature(tick))
        features.append(self.ptf.compute_feature(tick))
        features.append(self.psf.compute_feature(tick))
        features.append(self.vf.compute_feature(tick))

        self.curr_tick_features = features

        midprice: float = 0
        total_volume: float = 0
        for t in tick:
            midprice += t[0] * t[1]
            total_volume += t[1]
        midprice /= total_volume

        if self.curr_tick_midprice is not None:
            self.Y.append([midprice - self.curr_tick_midprice])

        self.curr_tick_midprice = midprice

        if len(self.X) > 10:
            self.X.pop(0)
            self.Y.pop(0)

    def predict(self) -> Any:
        if len(self.X) < 10:
            return None

        self.reg.fit(self.X, self.Y)

        return self.reg.predict([self.curr_tick_features])
