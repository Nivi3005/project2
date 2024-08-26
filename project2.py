import re

# Read the story from the file
with open("story.txt", "r") as file:
    story = file.read()

# Define a pattern to match placeholders
pattern = re.compile(r'<(.*?)>')

# Find all unique placeholders
placeholders = set(match.group(0) for match in pattern.finditer(story))

# Dictionary to store user inputs
user_inputs = {}

# Prompt user for input for each placeholder
for placeholder in placeholders:
    user_input = input(f"Enter a word for {placeholder}: ")
    user_inputs[placeholder] = user_input or placeholder  # Use the placeholder if the input is empty

# Replace placeholders in the story with user inputs
for placeholder, replacement in user_inputs.items():
    story = story.replace(placeholder, replacement)

# Print the updated story
print(story)
