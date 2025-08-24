# Define the coffee menu

coffee_menu= {
    'Espresso': 70,
    'Americano': 90,
    'Latte': 100, 
    'Cappuccino': 140,
    'Mocha': 178,
} 

# Welcome the Customer

print("welcome to AJ Coffee")
print("Espresso: Rs 70\nAmericano: Rs 90\nLatte: Rs 100\nCappuccino: Rs140\nMocha: Rs 178")

order_total=0  
#order will add on with total price

service_1= input("Enter the name of your coffee you want to order = ")
if service_1 in coffee_menu:
    order_total+=coffee_menu[service_1]
    print(f"your service {service_1} has been to your order")

else:
    print(f"ordered service {service_1} is not available in are cart yet !!")

another_order =input("Do you want to add another coffee? (Yes/No)")
if another_order=="Yes": 
    service_2=input("Enter the name of another coffee= ")
    if service_2 in coffee_menu:
            order_total += coffee_menu[service_2]
            print(f"service{service_2} has been added to order")
    else:
         print(f"Ordered Service {service_2} is not available !!")

print(f"The total amount of Service is to pay is {order_total}")