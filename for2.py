# A program to show a nested for loop.
outer_loop_total = 0
inner_loop_total = 0
countries = ["America", "England", "India", "China"]
capitals = ["Washington", "London", "New Delhi", "Beijing"]
for country_to_check in countries:
  outer_loop_total += 1
  for city_to_check in capitals:
    inner_loop_total += 1
    if country_to_check == "China" and city_to_check == "Beijing":
      print(outer_loop_total + inner_loop_total)
