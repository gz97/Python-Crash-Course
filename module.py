def dogs_in_daycare_today(weekday, *dogs):
    print(f"On {weekday.title()}, we have these dogs in daycare:")
    for dog in dogs:
        print(f"- {dog}")