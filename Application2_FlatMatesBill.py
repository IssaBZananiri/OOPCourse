'''
Getting the Bill Split - 
Author: Issa B. Zananiri 12/11/2023
OOP Course

1. Find the two flatmates.
2. Find their stay in the flat.
3. Calculate how much they need to pay by the bill

Classes Needed:
1. Flatmate: Attributes - name, days_in_house
             Methods - pays(bill, period)
             
2. Bill: Attributes - amount, period
         
3. PdfReport:
            Attributes: filename
            Methods: generatepdf(flatmate1, flatmate2, bill).
'''
from fpdf import FPDF


class Flatmate:
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house
    
    def bill_by_person(self, specific_bill):
        return (self.days_in_house/specific_bill.period) * specific_bill.amount 

class Bill:
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

class BillReport(Bill):

    def get_to_pdf(specificbill, mate1, mate2):
        pass
        
        


flatmate1 = Flatmate(input("Please Enter the name of Flatmate 1:"), float(input("Please Enter the Number of Days he/She Spent: ")))
flatmate2 = Flatmate(input("Please Enter the name of Flatmate 2:"), float(input("Please Enter the Number of Days he/She Spent: ")))

bill1 = BillReport(150, 30, filename="Report")
print("{} has to pay {} for the Stay".format(flatmate1.name, flatmate1.bill_by_person(bill1)))



