
from eopsin.prelude import *

@dataclass()
class ContractParam(PlutusData):
    address_to_receive_payment: PubKeyHash
    lovelace_per_token: int
    accepted_token_name_mint: TokenName

LOVELACE = Token(b"", b"")

def validator(contract_param: ContractParam, redeemer: None, ctx: ScriptContext) -> None:
    info = ctx.tx_info
    lovelace_paid = all_tokens_locked_at_address(info.outputs, Address(PubKeyCredential(contract_param.address_to_receive_payment), NoStakingCredential()), LOVELACE)
    minted_token = info.mint.values()[1]
    min_one_correct_token_minted = minted_token.get(contract_param.accepted_token_name_mint, 0) >= 1
    check_minted_type_and_amount = minted_token.get(contract_param.accepted_token_name_mint, 0) * contract_param.lovelace_per_token <= lovelace_paid
    assert min_one_correct_token_minted, "At least one token with the correct name must be minted"
    assert check_minted_type_and_amount, "Payment too low to mint requested number of tokens"
