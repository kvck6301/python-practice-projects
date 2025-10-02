# input for total rent
# input for number of persons
# input for total groceries
# input for electricity bill
#input for unit charge

#output 
# how much amount should be on one person

total_rent = int(input("Enter the total rent = "))
no_of_persons= int(input("Enter the number of persons = "))
total_groceries= int(input("total amount for groceries = "))
electricity_bill = float(input("total electricity bill = "))
unit_charge = float(input("unit chanrge =  "))
electricity_for_person =electricity_bill *unit_charge

rent_per_person = (total_rent+total_groceries+electricity_for_person)/no_of_persons
print(rent_per_person)

