class InsuranceRiskEvaluator:
    def __init__(self, age, health_score, driving_score):
        self.age = age
        self.health_score = health_score
        self.driving_score = driving_score

    def calculate_risk_index(self):
        # Balanced risk score using domain-specific weights
        health_risk = (100 - self.health_score) * 0.45
        driving_risk = (100 - self.driving_score) * 0.35
        age_risk = (self.age / 120) * 20  # Scaled based on human lifespan

        total_risk = health_risk + driving_risk + age_risk
        return round(min(total_risk, 100), 2)
