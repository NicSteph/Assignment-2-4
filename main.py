# input statements
salary = float(input(1250))
numDependents = float(input(2))

# calculate taxes here
stateTax = salary * .065
federalTax = salary * .28
dependentDeduction = (salary * .025) * 2
totalWithholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWithholding
# output statements
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
