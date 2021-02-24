# Caleb Manor

# PROGRAM TWO - comp3100p2.py
# Put your name in a comment at the top, do this for all programs submitted to Easel
# Create a string variable called PYTHON and loop through each character
# If the ascii value of the character is even then write "EVEN"
# If odd, then output "ODD"
# The output should look like this:
# P is ascii 80 - EVEN
# Y is ascii 89 - ODD
# and so forth

PYTHON = "PYTHON"

max_value = 6
for i in range(max_value):
    if (ord(PYTHON[i]) % 2) == 0:
        print(f"{PYTHON[i]} is ascii {ord(PYTHON[i])} - EVEN")
    else:
        print(f"{PYTHON[i]} is ascii {ord(PYTHON[i])} - ODD")