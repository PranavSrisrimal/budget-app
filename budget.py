class Category:
 
 #Initialising object with default/passed attributes
 def __init__(self, Category=""):
   self.ledger = []
   self.Category = Category
   self.total = 0.0

#Deposit
 def deposit(self, amount, description=""):
   
   self.ledger.append({"amount":amount, "description": description})
   self.total += amount

#Withdraw
 def withdraw(self, amount, description=""):
   
   if self.check_funds(amount):
      self.ledger.append({"amount":-amount,"description": description})
      self.total -= amount

      return True
   else : 
      return False   

#Balance
 def get_balance(self):
   return self.total

#Transfer   
 def transfer(self,amount,destination):
   
   if self.check_funds(amount) :
      _transfer_from = "Transfer from " + self.Category 
      destination.deposit(amount, _transfer_from)
      
      _transfer_to = "Transfer to " + destination.Category
      self.withdraw(amount, _transfer_to)
      

      return True

   else    :      
      return False

#Check funds
 def check_funds(self, amount):
   if self.get_balance() >= amount :
     return True
   else :
     return False

#Print the object 
 def __str__(self):
   top = ""
   top += self.Category.center(30,"*")
   middle=""
   middle += '\n'
  #Printing amount and description according to the format specified 
   for i in self.ledger:
       middle += '{:<23}'.format(i["description"][:23]) #First 23 char left aligned
       middle += '{:>7.2f}'.format(i["amount"])
       middle += '\n'
   bottom=""
   bottom += "Total: " + str(self.get_balance())    
    
   return (top + middle + bottom.rstrip())     
   
def create_spend_chart(category_list):
    title="Percentage spent by category\n"
    barchart=""
    withdraw_total = 0
    withdraw_percent = []
    
    #Calculating wtihdraw amount and percentage of each category 
    for i in category_list:
      k=0
      for j in i.ledger:
        if j["amount"]<0:
             withdraw_total += j["amount"]
             k += j["amount"]
        else :
           continue    
      
      withdraw_percent.append(f'{k:.2f}')  
    
    bar_percent=[int((((float(m) / withdraw_total) * 10) // 1) * 10) for m in withdraw_percent]

    #Printing the barchart     
    for p in range(100,-1,-10):
      barchart += str(p).rjust(3) + "|"
      
      for a in bar_percent:
       if a >= p:
         barchart += ' o '
       else :
        barchart += "   "
    
      barchart += " \n" 

      bottomline =""     
      bottomline += "    " + "-" * (3*len(category_list) + 1) + "\n"
    
    #Printing the description under the 'o' chart    
    _category = [y.Category for y in category_list]
    max_len = max(map(lambda length: len(length), _category))
    cat_description = list(map(lambda z: z.ljust(max_len), _category))

    for j in zip(*cat_description):
        bottomline += "    " + "".join(map(lambda p: p.center(3), j)) + " \n"    
           
    return(title + barchart + bottomline).rstrip("\n")