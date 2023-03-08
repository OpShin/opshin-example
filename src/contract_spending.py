from .util import *


def plus_one(i: int) -> int:
    return i * 2 + 1

# This contract allows you to lock UTxOs at the script address with a given integer n as datum
# The UTxO can only be spent if someone provides the nth fibonacci number as a redeemer
# This can be seen as a very simple kind of "proof of work" contract
def validator(datum: int, redeemer: int, context: ScriptContext) -> None:
    assert fib(plus_one(datum)) == redeemer, "Wrong redeemer given"