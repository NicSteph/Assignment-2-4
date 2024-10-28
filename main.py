salary = 1250
num_dependents = 3
state_tax = salary * 0.065
federal_tax = salary * 0.28
dependent_deduction = salary * 0.025 * num_dependents
total_withholding = state_tax + federal_tax + dependent_deduction
takehomepay = salary - total_withholding
print(f"state_tax: ${state_tax:.2f}")
print(f"federal_tax: ${federal_tax:.2f}")
print(f"dependent_deduction: ${dependent_deduction:.2f}")
print(f"salary: ${salary:.2f}")
print(f"takehomepay: ${takehomepay:.2f}")
