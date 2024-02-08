payRate = float(input('Pago por Hora: '))
hourRate = float(input('Horas trabajadas: '))

overtimeHours = 0

if (hourRate > 40):
    overtimeHours = hourRate - 40
    totalPay = (40 * payRate) + (overtimeHours * (payRate * 2))
else:
    totalPay = hourRate * payRate

print(f'El sueldo a pagar es {totalPay}')