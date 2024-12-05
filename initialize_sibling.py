import json
from sibling_core import create_sibling

def initialize_sibling(config_file="config.json"):
    with open(config_file, "r") as f:
        config = json.load(f)
    sibling = create_sibling(config)
    print(sibling.introduce())
    with open(f"{sibling.name}_state.json", "w") as f:
        json.dump(config, f, indent=4)

if __name__ == "__main__":
    initialize_sibling()