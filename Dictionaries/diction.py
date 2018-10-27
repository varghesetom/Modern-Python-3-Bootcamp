#Totaling Donations


donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0,
lisa=50.25, harrison=10.0)

total = sum(donations.values())
print(total)

# Initial Game State
game_properties = ["current_score", "high_score", "number_of_lives",
"items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills",
"enemy_kill_streaks", "minutes_played", "notications", "achievements"]

answer = dict.fromkeys(game_properties, 0)

### print(answer.items())

# Dictionary Methods

inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}

stock_list = inventory.copy()

stock_list["cookie"] = 18

stock_list.pop("cake")
