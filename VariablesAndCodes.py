from datetime import datetime

# Get the current hour
hour = datetime.now().hour

# Determine the part of the day
if 5 <= hour <= 11:
    part_of_the_day = "morning"
elif 12 <= hour <= 17:
    part_of_the_day = "afternoon"
elif 18 <= hour <= 22:
    part_of_the_day = "evening"
else:
    part_of_the_day = "night"

# User-specific data
user_name = "Gideon"

# Greetings based on time of day
system_Greetings = [
    f'Hi {user_name}, good {part_of_the_day}!',
    f'Hello {user_name}, good {part_of_the_day}!',
    f'Good to see you {user_name}! Good {part_of_the_day}!',
    f'Greetings, {user_name}! Good {part_of_the_day}!',
    f'Good {part_of_the_day}, {user_name}!'
]

print(random.choice(system_Greetings))
