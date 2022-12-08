def normal_mode(regex, text, origex):
    if not regex:
        return True
    if not text:
        return False
    if regex[0] not in [".", "", text[0]]:
        return normal_mode(origex, text[1:], origex)
    return normal_mode(regex[1:], text[1:], origex)


def beginning_mode(regex, text, origex):
    regex = regex[1:]
    text = text[: len(regex)]
    return menu(regex, text, origex)


def dollar_mode(regex, text, origex):
    regex = regex[:-1]
    text = text[-len(regex) :]
    return normal_mode(regex, text, origex)


def menu(regex, text, origex):
    if "^" in regex:
        return beginning_mode(regex, text, origex)
    if "$" in regex:
        return dollar_mode(regex, text, origex)
    return normal_mode(regex, text, origex)


def main():
    regex, text = input().split("|")
    print(menu(regex, text, regex))


if __name__ == "__main__":
    main()
