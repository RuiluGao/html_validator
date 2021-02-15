#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking
    whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    # HINT:
    # use the _extract_tags function below to generate a list of html tags
    # without any extra text;
    # then process these html tags using the balanced parentheses algorithm
    # from the class/book
    # the main difference between your code and the code
    # from class will be that you will have to keep
    # track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags

    stack = []
    extracted = _extract_tags(html)
    if html == "":
        return True
    if len(extracted) == 1 or len(extracted) == 0:
        return False
    for symbol in extracted:
        if not symbol[1] == "/":
            stack.append(symbol)
        else:
            if len(stack) == 0:
                return False
            current_tag = stack[-1]
            if not current_tag[1] == "/":
                if symbol == ("</" + current_tag[1:]):
                    stack.pop()
    return len(stack) == 0


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions
    that are not meant to be used directly by the user
    are prefixed with an underscore.

    This function returns a list of all the html tags
    contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''

    tag_list = []
    tag = ""
    for symbol in html:
        if symbol == "<":
            tag += symbol
        else:
            if symbol == ">":
                tag += symbol
                tag_list.append(tag)
                tag = ""
            else:
                if not len(tag) == 0:
                    tag += symbol
    return tag_list
