import re


def Symbol_match(password):
    return bool(re.search(r'^[a-zA-Z0-9^$%@#&*]+$', password))


def Password_length(password):
    return len(password) >= 8


def Low_case_register(password):
    count = sum(1 for i in password if i.islower())
    return count >= 2


def Digit(password):
    return bool(re.search(r'\d', password))


def Special_characters(password):
    count = sum(1 for char in password if char in r"^$%@#&*")
    return count >= 3


def Invalid_symbol(password):
    return not bool(re.search(r"[,\.!\?]", password))


def correct_password(password):
    """
    Проверка корректности пароля по различным критериям

    >>> correct_password('rtG&3FG#Tr^e')
    True
    >>> correct_password('a^A1@*@1Aa')
    True
    >>> correct_password('oF^a1D@y5%e6')
    True
    >>> correct_password('enroi#$*rkdeR#$*092uwedchf34tguv394h')
    True
    >>> correct_password('пароль')
    False
    >>> correct_password('password')
    False

    """
    return (Invalid_symbol(password) and Special_characters(password) and Digit(password)
            and Low_case_register(password) and Password_length(password) and Symbol_match(password))


import doctest

doctest.testmod()
