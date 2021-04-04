from collections import OrderedDict

def GrossSalaryCalculator(BasicSalary):
    Tax = 0.2 * BasicSalary

    def inner(Bonus):
        return Bonus + Tax + BasicSalary

    return inner


# I kind of simplified the steps here, so it's not an exact replica of the original solution
Segments = ['a', 'b', 'c']
Calculators = [GrossSalaryCalculator(1000), GrossSalaryCalculator(2000), GrossSalaryCalculator(3000)]
GrossSalaryCalculators = OrderedDict(zip(Segments,Calculators))
# print(GrossSalaryCalculators)

print(GrossSalaryCalculators['a'](80))
print(GrossSalaryCalculators['b'](90))
print(GrossSalaryCalculators['c'](100))