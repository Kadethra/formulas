def get_number(var: str):
    while True:
        inp = input(f"Please put in {var}: ")

        sign = 1
        interim = inp
        if inp.startswith("-"):
            sign = -1
            interim = inp[1:]

        if not interim.replace(".", "", 1).isdecimal():
            print("Invalid Input")
            continue

        num = float(interim) * sign
        return num