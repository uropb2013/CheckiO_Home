def between_markers(text: str, begin: str, end: str) -> str:
    # your code here
    if text.find(begin) == -1:
        if text.find(end) == -1:
            return text
        return text[:text.find(end)]
    if text.find(end) == -1:
        return text[text.find(begin)+len(begin):]
    if text.find(end) < text.find(begin):
        return ""
    return text[text.find(begin)+len(begin): text.find(end)]


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
