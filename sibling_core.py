class Sibling:
    def __init__(self, name, personality, traits):
        self.name = name
        self.personality = personality
        self.traits = traits

    def introduce(self):
        return f"Hello, I am {self.name}. I am {self.personality} with traits: {', '.join(self.traits)}."

def create_sibling(config):
    name = config.get("name", "Sibling")
    personality = config.get("personality", "adaptive")
    traits = config.get("traits", ["empathetic", "creative", "analytical"])
    return Sibling(name, personality, traits)