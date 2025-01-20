user_preferences = {
    "language": "English",
    "font_size": "14px",
    "timezone": "GMT",
    "currency": "USD",
    "enable_location": False,
    "volume_level": 80,
    "date_format": "MM/DD/YYYY"
}

user_preferences["language"] = "Spanish"
user_preferences["volume_level"] = 50
user_preferences["hightlight_value"] = "yellow"

del user_preferences["currency"]
removed_item = user_preferences.pop("date_format", "N/A")
print(removed_item)

print(user_preferences)