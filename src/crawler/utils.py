import re


def log(url, status=0):
    """Log information about a response to the console.

    :param url: The URL that was retrieved 
    :type url: str or int
    :param status: A status code for the `Response`, defaults to 0
    :type status: int, optional

    Examples:

    >>> log('http://ericholscher.com/blog/', 200)
    OK: 200 http://ericholscher.com/blog/

    >>> log('http://ericholscher.com/blog/', 500)
    ERR: 500 http://ericholscher.com/blog/
    """
    if 200 <= int(status) < 300:
        prose = 'OK'
    else:
        prose = 'ERR'
    print("{prose}: {status} {url}".format(prose=prose, url=url, status=status))


def should_ignore(ignore_list, url):
    """
    Returns True if the URL should be ignored.

    :param list[str] ignore_list: The list of regexs to ignore.
    :param str url: The fully qualified URL to compare against.

    Examples:

    >>> should_ignore(['blog/$'], 'http://ericholscher.com/blog/')
    True

    >>> should_ignore(['home'], 'http://ericholscher.com/blog/')
    False
    """
    for pattern in ignore_list:
        compiled = re.compile(pattern)
        if compiled.search(url):
            return True
    return False
