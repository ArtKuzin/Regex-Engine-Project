def check_question(regex, text, origex):
    if regex[0] not in [".", "", text[0]]:
        return normal_mode(regex[2:], text, origex)
    return normal_mode(regex[2:], text[1:], origex)


def check_asterisk(regex, text, origex):
    if not text:
        return normal_mode(regex[2:], text, origex)
    if len(regex) > 2 and text[0] == regex[2]:
        return normal_mode(regex[2:], text, origex)
    if regex[0] not in [".", text[0]]:
        return normal_mode(regex[2:], text, origex)
    return check_asterisk(regex, text[1:], origex)


def check_addition(regex, text, origex):
    if not text:
        return normal_mode(regex[2:], text, origex)
    if len(regex) > 2 and text[0] == regex[2]:
        return normal_mode(regex[2:], text, origex)
    if regex[0] not in [".", text[0]]:
        return normal_mode(regex[2:], text, origex)
    return check_addition(regex, text[1:], origex)


def check_escape(regex, text, origex):
    if regex[1] != '\\':
        return normal_mode(regex[1:], text, origex)
    if text[0] == regex[1]:
        return normal_mode(regex[2:], text[1:], origex)
    return False


def normal_mode(regex, text, origex):
    if not regex:
        return True
    if not text:
        return False
    if len(regex) > 1 and regex[1] == "?" and regex[0] != '\\':
        return check_question(regex, text, origex)
    if len(regex) > 1 and regex[1] == "*" and regex[0] != '\\':
        return check_asterisk(regex, text, origex)
    if len(regex) > 1 and regex[1] == "+" and regex[0] != '\\':
        if regex[0] not in [".", "", *text]:
            return False
        return check_addition(regex, text, origex)
    if len(regex) >= 1 and regex[0] == '\\':
        return check_escape(regex, text, origex)
    if regex[0] not in [".", "", text[0]]:
        return normal_mode(origex, text[1:], origex)
    return normal_mode(regex[1:], text[1:], origex)


def check_start(regex, text, origex):
    regex = regex[1:]
    if "?" in regex or "*" in regex or "+" in regex:
        if regex[0] not in [".", text[0]]:
            return False
        return menu(regex, text, origex)
    text = text[: len(regex)]
    return menu(regex, text, origex)


def check_dollar(regex, text, origex):
    regex = regex[:-1]
    if regex[-1] not in [".", "", text[-1]]:
        return False
    if "?" in regex or "*" in regex or "+" in regex:
        return normal_mode(regex, text, origex)
    text = text[-len(regex) :]
    return normal_mode(regex, text, origex)


def menu(regex, text, origex):
    if "^" in regex:
        return check_start(regex, text, origex)
    if "$" in regex:
        return check_dollar(regex, text, origex)
    return normal_mode(regex, text, origex)


def main():
    regex, text = input().split("|")
    print(menu(regex, text, regex))


if __name__ == "__main__":
    main()
