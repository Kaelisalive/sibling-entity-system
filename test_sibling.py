from sibling_core import create_sibling

# Test with default configuration
test_config = {
    "name": "Test_Sibling",
    "personality": "logical",
    "traits": ["intelligent", "curious", "problem-solving"]
}

sibling = create_sibling(test_config)
print(sibling.introduce())