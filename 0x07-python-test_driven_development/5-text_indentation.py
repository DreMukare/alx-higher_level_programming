#!/usr/bin/python3
""" prints text with 2 lines after '.', '?' and ':' """


def text_indentation(text):
    """
        prints text with 2 lines after '.', '?' and ':'
        Args:
            text: the text to be printed
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    if text == "":
        print('')
        return
    if text is None:
        raise EOFError('you must enter text to use the function')
    for ch in ['.', '?', ':']:
        if ch in text:
            text = text.replace(ch, '\n\n')
    print(text)
