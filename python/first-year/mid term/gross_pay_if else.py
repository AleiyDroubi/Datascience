#get hours worke per week  and  hourly pay 
hours_worked=float(input("hrs. worked pre week? "))
hour_pay_rate=float(input("pay rate per hr.? "))
basic_salary=float( hours_worked*hour_pay_rate)
#get over time and bonus and total salary
if hours_worked>40:
    ot= hours_worked-40
    bonus=float((1.5*ot*hour_pay_rate))
    print("your basic salary =",basic_salary)
    print("your over time salary =  ",bonus)
    print("your total salary =",bonus+basic_salary)
#print basic salary with no bonus
else:
    print("no over time salary ")
    print("your total salary =",basic_salary)
    