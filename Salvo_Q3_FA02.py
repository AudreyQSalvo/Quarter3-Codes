#Data
items = ["Orange", "Leek", "Spam", "Tissue roll"]

prices = [

  [122, 100, 127 ],

  [152, 120, 133],
  
  [208, 180, 235],

  [284, 335, 128]
  
]

total_prices = []

for i in range(0, 3):
    store_prices = [row[i] for row in prices]
    total_prices.append(sum(store_prices))
    
#Display the total amount of money that would be spent buying the items from each store individually
print(f"The total amount of money I would spend is ₱{total_prices[0]} if I would buy from SM Markets, ₱{total_prices[1]} if I would buy from Landers, and ₱{total_prices[2]} if I would buy from Shopee.")
    
#Display the store that you would spend the least amount of money buying the items from
if min(total_prices) == total_prices[0]:
    print(f"The store where I will spend the least amount of money buying from is: SM Markets")
elif min(total_prices) == total_prices[1]:
    print(f"The store where I will spend the least amount of money buying from is: Landers")
else:
    print(f"The store where I will spend the least amount of money buying from is: Shopee")