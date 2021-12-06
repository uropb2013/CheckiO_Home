def date_time(time: str) -> str:
    # replace this for solution
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    day = time[0:2]
    if int(day) < 10:
        day = time[1:2]
    hours = time[-5:-3]
    hours_ending = "hours"
    if int(hours) < 10:
        hours = time[-4:-3]
        if int(hours) == 1:
            hours_ending = "hour"
    mituts = time[-2:]
    mitutes_ending = "minutes"
    if int(mituts) < 10:
        mituts = time[-1:]
        if int(mituts) == 1:
            mitutes_ending = "minute"
    return day + " " + months[int(time[3:5]) - 1] + " " + time[6:time.find(" ")] + " " + "year"\
           + " " + hours + " " + hours_ending + " " + mituts + " " + mitutes_ending


if __name__ == "__main__":
    print("Example:")
    print(date_time("01.01.2000 00:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert (
        date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
    ), "Millenium"
    assert (
        date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes"
    ), "Victory"
    assert (
        date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes"
    ), "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")