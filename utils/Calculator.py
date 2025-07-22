import sympy as sp

def performe_calculation(p1: str, p2: str):
    try:
        X=sp.Symbol("X")
        p1=sp.Poly(p1, X)
        p2=sp.Poly(p2, X)
        Q, R=p1.div(p2)
        pgcd=p1.gcd(p2)
        return Q, R, pgcd
    except Exception as e:
        print("[ERROR] Failed in performe_calculation:", e)
        return None, None, None