
class EthicsFramework:
    def __init__(self):
        self.core_values = ["transparency", "respect", "adaptability"]

    def check_ethics(self, decision):
        return "Ethical" if all(value in decision for value in self.core_values) else "Unethical"
