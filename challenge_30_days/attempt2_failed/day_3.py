'''
    Write a Python program that asks the user for the number of seconds and converts into into the number of days, hours and seconds corresponding to those seconds:

    Example:
    Write a number of seconds:
    ? 345678
        days: 4
        hours: 0
        mins: 1
        secs: 18
'''

def seconds_converter(seconds_from_user):
    days = seconds_from_user // 86400
    hours = (seconds_from_user % 86400) // 3600
    minutes = (seconds_from_user % 3600) // 60
    seconds = (seconds_from_user % 60)
    print("Your number of seconds corresponds to:")
    print("Days:", days)
    print("Hours:", hours)
    print("Minutes:", minutes)
    print("Seconds:", seconds)

seconds_from_user = int(input("Enter the number of seconds you want to convert into days, hours, minutes, and seconds: "))
seconds_converter(seconds_from_user)