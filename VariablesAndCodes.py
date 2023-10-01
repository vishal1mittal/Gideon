from datetime import datetime
hour = datetime.now().hour
if 5 <= hour <= 11:
    partoftheday = "morning"

elif 12 <= hour <= 17:
    partoftheday = "afternoon"

elif 18 <= hour <= 22:
    partoftheday = "evening"

else:
    partoftheday = "night"
user_name = "vishal"
