# read the total amount,tenure,intrest rate and print the following calculation
# monthly emi
# total interest payable
# total payment

total_amount=float(input("enter the amount:"))
intrest_rate=float(input("enter the intrest:"))/(12*100)
tenure=int(input("enter the number of months:"))
emi=total_amount*intrest_rate*((1+intrest_rate)**tenure)/((1+intrest_rate)**tenure-1)
total_payable=emi*tenure
print(f"monthly emi:{emi}")
print(f"total payable amount={total_payable}")
total_intrest_payable=total_payable-total_amount
print(f"total intrest payable is:{total_intrest_payable}")

