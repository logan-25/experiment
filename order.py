import time

# Target string now set to "hello world"
target = "hello world"

# Initialize an empty result string
result = ""

# Loop over each letter in the target string
for letter in target:
    result += letter
    print(result, end='\r')  # Print the current progress (overwrite previous line)
    
    # Sleep for a short while to make the process visible
    time.sleep(0.5)  # Adjust the delay to control the speed

print("\nFinal result:", result)
