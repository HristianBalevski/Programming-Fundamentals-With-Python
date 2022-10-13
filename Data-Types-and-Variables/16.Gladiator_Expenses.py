#As a gladiator, Peter needs to repair his broken equipment when he loses a fight. His equipment consists of a helmet, a sword, a shield, and an armor. 
#You will receive Peter's lost fights count.
#Every second lost game, his helmet is broken.
#Every third lost game, his sword is broken.
#When both his sword and helmet are broken in the same lost fight, his shield also breaks.
#Every second time his shield brakes, his armor also needs to be repaired.
#You will receive the price of each item in his equipment. Calculate his expenses for the year for renewing his equipment. 

lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_expenses = 0

for fight in range(1, lost_fights_count + 1):

    if fight % 2 == 0:
        total_expenses += helmet_price
    if fight % 3 == 0:
        total_expenses += sword_price
    if fight % 6 == 0:
        total_expenses += shield_price
    if fight % 12 == 0:
        total_expenses += armor_price
print(f"Gladiator expenses: {total_expenses:.2f} aureus")