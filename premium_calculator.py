class DynamicPremiumEngine:
    def __init__(self, base_cost=5000):
        self.base_cost = base_cost

    def compute_adjusted_premium(self, risk_index, market_factor):
        risk_weight = 1 + (risk_index / 100)
        premium = self.base_cost * risk_weight * market_factor
        return round(premium, 2)
