print("\n")  
import pandas as pd
Menu = [
    "Coffee",
    "Tea",
    "Beef",
    "Rice",
    "Ugali",
    "Chicken",
    "Fries",
    "Pork",
    "Fried eggs",
    "Juice",
    "Sausages",
    "BBQ Meat"
    ]

df = pd.DataFrame(Menu, columns=["Menu"])
df.loc[:8, "Prices"] = 7.50
df.loc[8:, "Prices"] = 13.50
df.index += 1
total_bill = 0.0

print ("Welcome to our Restaurant")
print ("\n")
print ("Here's our menu")
print ("\n")

print (df.to_string(justify='left',header=False,formatters={'Menu':'{{:<{}s}}'.format(df['Menu'].str.len().max()).format,'Prices':'     ${:.2f}'.format}))
print ("\n")

print ("Type the number that corresponds with the meal you want to order and press enter to select")
print ("\n")
print ("Type 'exit' to cancel your order")
print ("\n")
print ("Type 'done' to finish your order and see your total bill")
print ("\n")

while True:

    order = input(">>> ")

    if order == 'exit':
        break
    
    elif order == 'done':
        print ("Total bill: ${:.2f}.".format(total_bill))
        input("Press any key to exit")
        break
    
    elif int(order) in df.index:
        item = df.loc[int(order), "Menu"]
        price = df.loc[int(order), "Prices"]
        print ("{}: ${:.2f}.".format(item, price))
        total_bill += price
        continue
    
    else:
        print ("\n Wrong selection")
        print ("\n Choose the correct")
        continue
