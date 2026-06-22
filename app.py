import datetime

class OrvantaTradingEngine:
    def __init__(self):
        self.MAX_LOTS = 9
        print("[INIT] Orvanta Trading Engine Online.")

    def check_market_time(self):
        # Strict SEBI compliance: 09:16 to 15:15
        now = datetime.datetime.now().time()
        if datetime.time(9, 16) <= now <= datetime.time(15, 15):
            return "TRADING_ACTIVE"
        return "MARKET_CLOSED"

    def process_order(self, strategy_id, lots):
        # Validate Lot Limit
        if lots > self.MAX_LOTS:
            return f"REJECTED: {lots} lots exceeds limit of {self.MAX_LOTS}."
        
        # Validate Market Window
        if self.check_market_time() != "TRADING_ACTIVE":
            return "REJECTED: Outside active trading window (09:16 - 15:15)."
            
        return f"SUCCESS: Strategy {strategy_id} executed with {lots} lots."

# Global Trigger
if __name__ == "__main__":
    engine = OrvantaTradingEngine()
    # Test simulation
    print(f"Engine Status: {engine.process_order('ST-01', 5)}")
