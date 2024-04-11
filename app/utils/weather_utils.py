def determine_safety_alert(temperature, precipitation, wind_speed):
    if 50 <= temperature <= 86 and precipitation < 0.2 and wind_speed < 22.4:
        return 'green'
    else:
        return 'red'