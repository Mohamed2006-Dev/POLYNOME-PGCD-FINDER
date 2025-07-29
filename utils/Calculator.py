"""
Calculator module.

This module provides the performe_calculation function, which performs polynomial division
and GCD calculation using sympy. It returns the quotient, remainder, and GCD as sympy Poly objects.
"""

import sympy as sp

def perform_calculation(p1: sp.Poly, p2: sp.Poly):
    """
    Perform polynomial division and GCD calculation.

    Args:
        p1 (sp.Poly): First polynomial (dividend).
        p2 (sp.Poly): Second polynomial (divisor).

    Returns:
        tuple: (Quotient, Remainder, GCD) as sympy Poly objects, or (None, None, None) on error.
    """
    try:
        Q, R = p1.div(p2)
        pgcd = p1.gcd(p2)
        return Q, R, pgcd
    except Exception as e:
        print(f"[ERROR] performe_calculation failed for polynomials {p1} and {p2}: {e}")
        return None, None, None