def capitalizeFirstLetter(description):
    if len(description) > 0:
        weatherDescription = description[0].upper() + description[1:]
        return weatherDescription
    else:
        return description 