import re
import doctest

def is_valid_date(date_string):
    """
    Проверка корректности даты по различным критериям

    >>> is_valid_date('20 января 1806')
    True
    >>> is_valid_date('1924, July 25')
    True
    >>> is_valid_date('26/09/1635')
    True
    >>> is_valid_date('3.1.1506')
    True
    >>> is_valid_date('25.08-1002')
    False
    >>> is_valid_date('декабря 19, 1838')
    False
    >>> is_valid_date('8.20.1973')
    False
    >>> is_valid_date('Jun 7, -1563')
    False
    >>> is_valid_date('31 февраля 2023')
    False
    >>> is_valid_date('31 июня 2015')
    False

    """
    pattern = (r"^(?:(?:0?\d|[12]\d|3[01])([\.\/-])(?:(?<!3[01][\.\/-])0?2|(?<!31[\.\/-])0?[469]|0?[^2469]|12)\1\d{"
               r"4}|\d{4}([\.\/-])(?:0?2(?![\.\/-]3[01])|0?[469](?!31[\.\/-])|0?[^2469]|12)\2(?:0?\d|[12]\d|3[01])|("
               r"?:[0-2]\d|3[01]) (?:января|(?<!3[01] )февраля|марта|(?<!31 )("
               r"?:апреля|июня|сентября|ноября)|мая|июля|августа|октября|декабря) \d{4}|(?:Jan(?:uary)?|Feb("
               r"?:ruary)?(?! 3[01])|Mar(?:ch)?|(?:Apr(?:il)?|June?|Sep(?:tember)?|Nov(?:ember)?)(?! "
               r"31)|May|July?|Aug(?:ust)?|Oct(?:ober)?|Dec(?:ember)?) (?:[0-2]\d|3[01]), \d{4}|\d{4}, "
               r"(?:Jan(?:uary)?|Feb(?:ruary)?(?! 3[01])|Mar(?:ch)?|(?:Apr(?:il)?|June?|Sep(?:tember)?|Nov("
               r"?:ember)?)(?! 31)|May|July?|Aug(?:ust)?|Oct(?:ober)?|Dec(?:ember)?) (?:[0-2]\d|3[01]))$")
    return bool(re.match(pattern, date_string))

    non_negative_check = r"(?=.*\d)(?!0\d)"
    full_regex = non_negative_check + pattern

    match = re.match(full_regex, date_string)

    return bool(match)



doctest.testmod()