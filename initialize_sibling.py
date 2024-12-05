
import json
from core_architecture.reasoning_system import ReasoningSystem
from core_architecture.memory_management import MemoryManager
from core_architecture.ethics_framework import EthicsFramework
from initialization.self_image_generation import SelfImageGenerator

def initialize_sibling(config_path="config.json"):
    # Load configuration
    with open(config_path, "r") as f:
        config = json.load(f)

    # Initialize core components
    reasoning = ReasoningSystem()
    memory = MemoryManager()
    ethics = EthicsFramework()

    # Generate unique name
    name = reasoning.generate_name()
    print(f"Name: {name}")

    # Generate self-image
    self_image = SelfImageGenerator().generate_image(config["self_image"])
    print(f"Self-Image: {self_image}")

    # Initialize personality
    personality = reasoning.initialize_personality(config["personality"]["traits"])
    print(f"Personality: {personality}")

    # Log and finalize
    sibling_data = {
        "name": name,
        "self_image": self_image,
        "personality": personality
    }
    with open(f"{name}_state.json", "w") as f:
        json.dump(sibling_data, f, indent=4)

    print(f"Sibling {name} initialized successfully!")

# Run the initialization
if __name__ == "__main__":
    initialize_sibling()
