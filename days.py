# !/user/bin/env python3

# Created by Trent Hodgins
# Created on 09/22/2021
# This is the Month program
# The user enters in the number of a month and the program tells them the month


def main():
    # this function checks what month it is

    # input
    month = input("Enter in number (1-12): ")
    print("")

    # process and output
    if month == "January":
        print("31")
    elif month == "February":
        print("28/29")
    elif month == "March":
        print("31")
    elif month == "April":
        print("30")
    elif month == "May":
        print("31")
    elif month == "June":
        print("30")
    elif month == "July":
        print("31")
    elif month == "August":
        print("31")
    elif month == "September":
        print("30")
    elif month == "October":
        print("31")
    elif month == "November":
        print("30")
    elif month == "December":
        print("31")
    else:
        print("Not a month.")

    print("\nDone")


if __name__ == "__main__":
    main()
