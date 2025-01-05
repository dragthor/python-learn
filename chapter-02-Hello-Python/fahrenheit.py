def celsius_to_fahrenheit(celsius: float) -> float:
    return (9/5) * celsius + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5/9

print(celsius_to_fahrenheit(0)) # freezing point of water, 32.0

print(celsius_to_fahrenheit(100)) # boiling point of water, 212.0

print(fahrenheit_to_celsius(32)) # freezing point of water, 0.0

print(fahrenheit_to_celsius(212)) # boiling point of water, 100.0
