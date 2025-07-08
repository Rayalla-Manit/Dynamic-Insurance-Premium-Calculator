import random

class MarketFluctuationModel:
    def __init__(self):
        self.trend_score = self._simulate_market_conditions()

    def _simulate_market_conditions(self):
        # Simulating volatility in insurance sector pricing
        return round(random.uniform(0.88, 1.18), 2)

    def get_market_factor(self):
        return self.trend_score
