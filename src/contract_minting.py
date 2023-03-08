from src.util import *

# Minting UTxOs do not have a datum, they are invoked only with a redeemer
# You can mint this token if you provide the 10th fibonacci number as a redeemer!
def validator(redeemer: int, context: ScriptContext) -> None:
    assert fib(10) == redeemer, "Wrong redeemer given"