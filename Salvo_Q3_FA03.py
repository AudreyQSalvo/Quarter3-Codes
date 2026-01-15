#Data
items = ["Orange", "Leek", "Spam", "Tissue roll"]

prices = [

  [122, 100, 127 ],

  [152, 120, 133],
  
  [208, 180, 235],

  [284, 335, 128]
  
]

total_prices = []
average_prices = []
min_value = []
max_value = []

#Calculate the total for each row
for i in range(0, 4):
    total_prices.append(sum(prices[i]))
    
#Calculate the average for each row
for j in range(0,4):
    average = round(total_prices[j]/3)
    average_prices.append(average)
    
#Calculate the minimum value
for l in range(0,4):
    min_value.append(min(prices[l]))
    
#Calculate the maximum value
for k in range(0,4):
    max_value.append(max(prices[k]))

#Display the data
for m in range(0, 4):
    print(f"{items[m]} - Total Price: ₱{total_prices[m]} | Average: ₱{average_prices[m]} | Min: ₱{min_value[m]} | Max: ₱{max_value[m]}")