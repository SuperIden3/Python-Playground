import sys
import os

from pygments import highlight
from pygments.formatters import Terminal256Formatter
from pygments.lexers import PythonLexer

from pprint import pformat
import sqlite3

def pretty(val):
    """Prettify a value."""
    return highlight(pformat(val).rstrip('\n'), PythonLexer(), Terminal256Formatter())

def printf(*args):
    """Basically `print(..., end=\"\")`"""
    print(*args, end="")

def eprint(*args):
    """Print to stderr."""
    print(*args, file=sys.stderr)

class uint8:
    def __init__(self, value = 0):
        if not (0 <= value and value <= 255):
            raise ValueError(f"uint8 must be 0 to 255 inclusive, not {value}")
        if not isinstance(value, int):
            raise ValueError(f"value must be type of int, not {value}")
        self._value = value;
    def __int__(self):
        return self._value
    def __str__(self):
        return str(self._value)
    def __repr__(self):
        return f"uint8({self._value})"
    def __eq__(self, other):
        if isinstance(other, uint8):
            return self._value == other._value
        return False
    def __hash__(self):
        return hash(self._value)
    def __add__(self, other):
        if isintance(other, uint8):
            return uint8(self._value + other._value)
        elif isinstance(other, int):
            return uint8(self._value + other)
        else:
            return NotImplemented
    def __sub__(self, other):
        if isintance(other, uint8):
            return uint8(self._value - other._value)
        elif isinstance(other, int):
            return uint8(self._value - other)
        else:
            return NotImplemented
    def __mul__(self, other):
        if isintance(other, uint8):
            return uint8(self._value * other._value)
        elif isinstance(other, int):
            return uint8(self._value * other)
        else:
            return NotImplemented
    def __div__(self, other):
        if isintance(other, uint8):
            return uint8(self._value / other._value)
        elif isinstance(other, int):
            return uint8(self._value / other)
        else:
            return NotImplemented
    def __lt__(self, other):
        if isinstance(other, uint8):
            return self._value < other._value
        return False
    def __gt__(self, other):
        if isinstance(other, uint8):
            return self._value > other._value
        return False

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by `db_file`.
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        eprint(e)
    return conn

