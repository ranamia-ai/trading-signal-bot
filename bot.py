def generate_signal(ema9, ema21, rsi, price):
    if ema9 > ema21 and rsi >= 50:
        return "CALL"

    if ema9 < ema21 and rsi <= 50:
        return "PUT"

    return "NO SIGNAL"


print("Trading Signal Bot")
print("-------------------")

# Example data
price = 100
ema9 = 101
ema21 = 99
rsi = 56

signal = generate_signal(ema9, ema21, rsi, price)

print("Price:", price)
print("EMA 9:", ema9)
print("EMA 21:", ema21)
print("RSI:", rsi)
print("Signal:", signal)
