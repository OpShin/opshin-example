from eopsin.prelude import *

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# Minting UTxOs do not have a datum, they are invoked only with a redeemer
# You can mint this token if you provide the 10th fibonacci number as a redeemer!
def validator(redeemer: int, context: ScriptContext) -> None:
    assert fib(10) == redeemer, "Wrong redeemer given"