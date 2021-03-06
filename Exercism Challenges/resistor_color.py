def color_code(color):
    if color == "black":
        return 0
    else:
        if color == "white":
            return 9
        else:
            if color == "orange":
                return 3
            else:
                if color == "brown":
                    return 1
                else:
                    if color == "red":
                        return 2
                    else:
                        if color == "yellow":
                            return 4
                        else:
                            if color == "green":
                                return 5
                            else:
                                if color == "blue":
                                    return 6
                                else:
                                    if color == "violet":
                                        return 7
                                    else:
                                        return 8


def colors():
    return [
            "black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white"
        ]


def color_codes(input_colors):
    result = []
    print(result)
    for x in input_colors:
        converted = color_code(x)
        result.append(converted)
        print(result)
    return result

