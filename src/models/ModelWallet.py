from .database import run_query
from .entities.Wallet import Wallet


class ModelWallet:
    @classmethod
    def update_balance(
        cls, user_wallet: Wallet, transaction_amount, transaction_type
    ) -> None:
        if transaction_type == "Income":
            user_wallet.balance += transaction_amount
        else:
            user_wallet.balance -= transaction_amount

        update_balance_query = """
            UPDATE wallets SET balance = %s WHERE user_id = %s;
        """
        run_query(update_balance_query, (user_wallet.balance, user_wallet.user_id))
