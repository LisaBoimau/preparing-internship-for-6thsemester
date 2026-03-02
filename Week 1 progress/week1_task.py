brand_name= 'LG'
initial_stock=20
items_sold=int(input('how many items sold: '))
if items_sold>initial_stock:
    print(f"Error: Cannot sell {items_sold} items. Only {initial_stock} in stock.")
else:
    current_stock=initial_stock-items_sold
    
    if current_stock<5:
        print(f"Status: CRITICAL. Please restock {brand_name} immediately!")
    else:    
        print(f'Status: Safe. {brand_name} stock is sufficient.')
        
    print(f"Remaining stock for {brand_name}: {current_stock} units.")