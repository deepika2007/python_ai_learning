is_boiling = True
stri_count = 5
total_action = is_boiling + stri_count #upcasting 
print(f"Total action (True as 1): {total_action}")

milk_present = False
tea_present = True
beverage_ready = milk_present or tea_present
print(f"Beverage ready: {beverage_ready} {bool(-1)}")


water_not = True
tea_added = False

can_serve = water_not and tea_added
can_serve_not = water_not or tea_added
print(f"Can serve tea? {can_serve}, {can_serve_not}")