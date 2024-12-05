
class ReasoningSystem:
    def generate_name(self):
        import random
        return "Sibling_" + str(random.randint(1000, 9999))

    def initialize_personality(self, personality_traits):
        return {
            "traits": personality_traits,
            "adaptive": True
        }
