def between_markers(text: str, begin: str, end: str) -> str:
    # your code here
    if begin in text:
        start = text.find(begin) + len(begin)
    else:
        start = None
    if end in text:
        end = text.find(end)
    else:
        end = None
    return text[start:end]


if __name__ == '__main__':
    print('Example:')
    print(between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>"))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
