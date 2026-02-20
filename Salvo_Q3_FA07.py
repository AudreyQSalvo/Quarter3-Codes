items = ["Orange", "Leek", "Spam", "Tissue roll"]

prices = [

  [122, 100, 127 ],

  [152, 120, 133],
  
  [208, 180, 235],

  [284, 335, 128]
  
]

for i in range(len(items)):
    p_total = sum(prices[i])
    p_avg = round(p_total / len(prices[i]), 1)
    p_min = min(prices[i])
    p_max = max(prices[i])
    print(f"{items[i]:<12}- Total Price: ₱{p_total} | Average: ₱{p_avg} | Min: ₱{p_min} | Max: ₱{p_max}")