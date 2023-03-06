from eopsin.prelude import *

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# This contract allows you to lock UTxOs at the script address with a given integer n as datum
# The UTxO can only be spent if someone provides the nth fibonacci number as a redeemer
# This can be seen as a very simple kind of "proof of work" contract
def validator(datum: int, redeemer: int, context: ScriptContext) -> None:
    assert fib(datum) == redeemer, "Wrong redeemer given"