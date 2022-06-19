from dataclasses import dataclass
from enum import Enum


class CurrencyChoice(Enum):
    EURO = '€ Euro'
    POUND = '£ Pound Sterling'
    DOLLAR = '$ US Dollar'


class CurrencyType(Enum):
    EURO = '€'
    POUND = '£'
    DOLLAR = '$'


@dataclass
class AuthData:
    LOGIN = 'user'
    PASSWORD = 'bitnami'


@dataclass
class User:
    first_name = 'Nikolay'
    last_name = 'Domochevsky'
    email = 'someemal@gmail.com'
    telephone = '89774547718'
    password = 'mynewpassword'
