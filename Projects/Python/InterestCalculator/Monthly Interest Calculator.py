# -*- coding: utf-8 -*-
#PS2 

#Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

#tips:
# For each month, calculate satements on the monthly payment and remaining balnce and print
#do not print out mor ethan two decimal places (use the round() function!)
#Finally, print out the total amount paid that year 

#This is going to be a loop over 12 cycles that will need to print over each cycle

#use these three variables

#balance-total outstanding balance, annualInterestRate-annual interest rate as decimal, monthlyPaymentRate- minimum monthly payment rate as decimal

#Break this down into steps...

#For each month:
#Compute the monthly payment, based on the previous month’s balance.
#Update the outstanding balance by removing the payment, then charging interest on the result.
#Output the month, the minimum monthly payment and the remaining balance.
#Keep track of the total amount of paid over all the past months so far.
#Print out the result statement with the total amount paid and the remaining balance.
def interest_calculator():
	'''
This application takes a balance of nums, and an annual interest rate and monthly payment rate of floats and caclulates the minimum monthly payment, remaining blanace, and total paid over a year
	'''
balance= 12000 #The first three variables are filled in by the grader... but you can add numbers to check
annualInterestRate = .06
monthlyPaymentRate = .05
monthlyInterestRate = (annualInterestRate)/12.0 #definitional
monthlyPayment = balance * monthlyPaymentRate #basic math, your minimum payment each month will be your balance times your mandatory monthly payment rate
month = 0 # updates with loop
totalPaid = 0 #keeps track of amount paid
for month in range(1,13): #moves through 12 steps, one for each month
    
    monthlyPayment = monthlyPaymentRate * balance #each month you pay this amount
    balance =  (balance-monthlyPayment)*(1+monthlyInterestRate) #you need to update your balance each month!, subtract your payment and multiply this new balance by your interest rate
    totalPaid= monthlyPayment+totalPaid #keep track of your total payments by adding your monthly payment to this amount each time the loop goes by
    
    print "Month: "+ str(month) #the loop should print each month that goes by
    print 'Minimum monthly payment: ' + str(round(monthlyPayment,2)) #the loop should print a rounded value for how much you payed each month
    print 'Remaining Balance: ' +str(round(balance,2)) #the loop should display your current balance
print 'Total paid: ' + str(round(totalPaid,2)) #after the loop finishes, display the sum of the monthly payments
print 'Remaining Balance: ' +str(round(balance,2)) #after the loop finishes, display the current balance after a year of loans