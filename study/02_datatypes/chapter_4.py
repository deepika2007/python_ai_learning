is_boiling = True
stri_count = 5
total_action = is_boiling + stri_count #upcasting 
print(f"Total action (True as 1): {total_action}")

milk_present = False
tea_present = True
beverage_ready = milk_present or tea_present
print(f"Beverage ready: {beverage_ready} {bool(-1)}")