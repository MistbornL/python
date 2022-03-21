def converter(option, target):
    current = option[0]
    temp = option[1]

    if current == "fahrenheit" and target == "celcius":
        return round((temp - 32) * 5 / 9, 1)
    elif current == "farenheit" and target == "kelvin":
        return round((temp - 32) * 5 / 9 + 273.15, 1)
    elif current == "celcius" and target == "farenheit":
        return round((temp * 9 / 5) + 32, 1)
    elif current == "celcius" and target == "kelvin":
        return round(temp + 273.15, 1)
    elif current == "kelvin" and target == "celcius":
        return round(temp - 273.5, 1)
    elif current == "kelvin" and target == "farenheit":
        return round((temp - 273.15) * 9 / 5 + 32, 1, 1)


while True:
    try:
        current = input("Enter current temperature type: ")
        temp  = int(input("Enter temperature: "))
        target = input("Enter target to convert: ")

        if current or temp or target != "fahrenheit" or "celcius" or "kelvin":
            print("Enter valid temperature type!!")
            continue
    except ValueError:
        print("invalid input")
        continue

print(converter([current, temp], target))