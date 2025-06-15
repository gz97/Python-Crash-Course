def dogs_in_daycare_today(weekday, *dogs):
    """"
    Function which gives us a list of all dogs attending daycare
    on a given day.

    Parameters: weekday, names of dogs
    """
    print(f"On {weekday.title()}, we have these dogs in daycare:")
    for dog in dogs:
        print(f"- {dog}")


def dogs_in_daycare_attendance_md(weekday, dog_name, **dog_info):
    print(f"On {weekday.title()}, we have {dog_name} in daycare:")
    dog_info['attendance_day'] = weekday
    dog_info['dog_name'] = dog_name
    return dog_info