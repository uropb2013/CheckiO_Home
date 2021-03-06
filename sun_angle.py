def sun_angle(time: str):
    if int(time[0:2]) < 6 or int(time[0:2]) > 18 or (int(time[0:2]) == 18 and int(time[3:5]) > 0):
        return "I don't see the sun!"
    return ((int(time[0:2]) - 6) * 60 + int(time[3:5])) / 4


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")