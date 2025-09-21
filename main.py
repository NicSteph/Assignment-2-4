# input statements
salary = float(input())
numDependents = float(input())

# calculate taxes here
stateTax = salary * .065
federalTax = salary * .28
dependentDeduction = (salary * .025) * 2
totalWithholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWithholding
# output statements
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
