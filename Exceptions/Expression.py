"""
Expression.py

This module defines the ExpressionError exception, used for signaling invalid polynomial expressions
in the PGCD Finder application.
"""

class ExpressionError(Exception):
    """
    Exception raised for errors in polynomial expressions.

    Args:
        message (str): Description of the error.
    """
    def __init__(self, message: str):
        super().__init__(message)