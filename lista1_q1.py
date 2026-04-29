'''1) Ler uma temperatura em graus Celsius
e apresentá-la convertida em graus Fahrenheit.
A fórmula de conversão é F = (9 * C + 160) / 5,
sendo F a temperatura em Fahrenheit e C a
temperatura em Celsius.'''

celsius = float(input("Temp. Celsius: "))
fahrenheit = (9 * celsius + 160) / 5
print(f"Temp: {fahrenheit}°F")

