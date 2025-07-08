from risk_profiler import InsuranceRiskEvaluator
from market_analyzer import MarketFluctuationModel
from premium_calculator import DynamicPremiumEngine
from quote_generator import QuoteBuilder

def run_premium_tool():
    print("🔷 Dynamic Insurance Premium Quote Generator 🔷\n")
    try:
        age = int(input("Enter your age: "))
        health_rating = float(input("Rate your overall health (0 to 100): "))
        driving_history = float(input("Rate your driving behavior (0 to 100): "))
    except ValueError:
        print("🚫 Invalid input. Please enter numerical values only.")
        return

    risk_evaluator = InsuranceRiskEvaluator(age, health_rating, driving_history)
    risk_index = risk_evaluator.calculate_risk_index()

    market_model = MarketFluctuationModel()
    trend_factor = market_model.get_market_factor()

    premium_engine = DynamicPremiumEngine()
    estimated_premium = premium_engine.compute_adjusted_premium(risk_index, trend_factor)

    quote = QuoteBuilder(estimated_premium, risk_index, trend_factor)
    print(quote.compose_summary())

if __name__ == "__main__":
    run_premium_tool()
