from pkg.calculator import Calculator

calculator = Calculator()

# Test the specific case mentioned by the user
result = calculator.evaluate("3 + 7 * 2")
print(f"3 + 7 * 2 = {result}")
print(f"Expected: 17, Got: {result}, Pass: {result == 17}")

# Test other precedence-related cases
result2 = calculator.evaluate("2 * 3 + 5")
print(f"\n2 * 3 + 5 = {result2}")
print(f"Expected: 11, Got: {result2}, Pass: {result2 == 11}")

result3 = calculator.evaluate("10 - 2 * 3")
print(f"\n10 - 2 * 3 = {result3}")
print(f"Expected: 4, Got: {result3}, Pass: {result3 == 4}")

result4 = calculator.evaluate("2 * 3 - 8 / 2 + 5")
print(f"\n2 * 3 - 8 / 2 + 5 = {result4}")
print(f"Expected: 7, Got: {result4}, Pass: {result4 == 7}")