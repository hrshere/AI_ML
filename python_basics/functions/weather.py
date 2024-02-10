'''prepared for weather?'''

def main():
    have_umbrella = False
    rain_level = 1
    have_hood = False
    is_workday = False
    actual = prepared_for_weather(have_umbrella,have_hood,rain_level,is_workday)
    print(actual)

def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    return have_umbrella or ((rain_level < 5) and have_hood) or (not (rain_level > 0) and is_workday)

if __name__ == "__main__":
    main()