#1st Question

sales = {
  "cost_value": 31.87,
  "sell_value": 45.00,
  "inventory": 1000
}  

print("Your profit is: ", round(sales["inventory"] * (sales["sell_value"]-sales["cost_value"])))

#2st Question

Amount = float(input("Please Enter The Amount : "))

print("$%.2f" % Amount)