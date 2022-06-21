from cProfile import label
from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('Lab1.2\data_analysis_lab.xlsx')

def getvalue(x):
    return x.value

years = list(map(getvalue, wb['Data']['A'][1:]))
action = list(map(getvalue, wb['Data']['D'][1:]))
temperature = list(map(getvalue, wb['Data']['C'][1:]))

pyplot.plot(years, action, label='Action')
pyplot.plot(years, temperature, label='Temp')
pyplot.show()