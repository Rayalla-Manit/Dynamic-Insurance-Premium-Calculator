class QuoteBuilder:
    def __init__(self, premium_value, risk_score, market_factor):
        self.premium = premium_value
        self.risk = risk_score
        self.market = market_factor

    def compose_summary(self):
        return f"""
        ───────────────────────────────
             Final Insurance Quote
        ───────────────────────────────
        ➤ Calculated Risk Index  : {self.risk}/100
        ➤ Market Trend Modifier  : {self.market}
        ➤ Total Estimated Premium: ₹{self.premium}
        ───────────────────────────────

        💡 Details:
        - Your individual risk profile is based on health, age, and driving safety.
        - Market trends are dynamically factored using a real-time pricing simulation.
        - The final quote reflects fair, risk-sensitive pricing tailored to you.
        """
