import string
import random
import time

# Target string now set to "hello world"
target = "loganathan"

# List of all lowercase letters, including space
letters = string.ascii_lowercase + " "  # Only lowercase letters and space

# Initialize an empty result string
result = ""

# Loop over each letter in the target string
for letter in target:
    while True:
        # Pick a random letter from the list of letters
        guess = random.choice(letters)
        print(result + guess, end='\r')  # Print the current progress + guessed letter (overwrite previous line)
        
        # If the guessed letter matches the current letter in the target string, add it to result
        if guess == letter:
            result += guess
            break
        
        # Sleep for a short while to make the guessing process visible
        time.sleep(0.1)

print("\nFinal result:", result)
