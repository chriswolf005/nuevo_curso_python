import reports

#Genera reporte de ventas y gastos usando a funcion del modulo

sales_report=reports.generate_sales_report("October", 10000)

expense_report=reports.generate_expense_report("October", 5000)

print(sales_report)
print(expense_report)