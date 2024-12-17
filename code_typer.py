import pyautogui
import time
import random
import string

# Generate a random variable name
def random_variable_name(length=5):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# Generate a random number or string literal
def random_literal():
    return str(random.randint(0, 100)) if random.choice([True, False]) else f'"{"".join(random.choices(string.ascii_letters, k=5))}"'

# Generate a random Python statement
def random_statement():
    var1 = random_variable_name()
    var2 = random_variable_name()
    literal = random_literal()
    operator = random.choice(['+', '-', '*', '/', '%', '==', '!=', '<', '>', '<=', '>='])
    
    statements = [
        f'{var1} = {literal}',
        f'{var1} = {var2} {operator} {literal}',
        f'print("{var1}")',
        f'if {var1} {operator} {var2}: print("Condition met")',
        f'for i in range({random.randint(1, 10)}): print(i)',
        f'def {random_variable_name()}(): return {random_literal()}'
    ]
    
    return random.choice(statements)

# Simulate typing random Python code indefinitely
time.sleep(5)  # Gives you 5 seconds to switch to the editor where you want the text to be typed
while True:
    line = random_statement()
    pyautogui.write(line)
    pyautogui.press('enter')
    time.sleep(5)  # Waits for a second before typing the next line