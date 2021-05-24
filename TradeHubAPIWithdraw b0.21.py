# TradeHubAPIWithdraw b0.21

# LIBRARYS DEM
# ------------------------------------------------------------------------------
import tradehub
from tradehub.wallet import Wallet
from tradehub.authenticated_client import AuthenticatedClient

from tradehub.types import CreateOrderMessage

# PARAMETERS
# ------------------------------------------------------------------------------
myMnemonic = 'program cram lunch mail clump kebab paela switcheo make people rich now' #Tradehub mnemonic (example here: 12 word TradeHub mnemonic)
depositAddress = '0x1577af8a039414df5ade74453fac4a0a06d1e6ef' #Wallet Address you want to send tokens (example here: ERC-20/BEP-20 address)
tokenDenom = 'busd1' #Quantity to withdraw (example here: 'busd1' = BUSD (BEP-20) on tokenlist.txt)
quantityWithdraw = '8.0' #Quantity to withdraw (example here: '8.0' = 8$)
blockchainType = 'BUSD' #Blockchain type

# CONSTANTS
# ------------------------------------------------------------------------------
demPK = Wallet(myMnemonic, network='mainnet')
clientDem = AuthenticatedClient(demPK, network='mainnet',trusted_ips=None, trusted_uris=['http://54.255.5.46:5001', 'http://175.41.151.35:5001'])

# MAIN
# ------------------------------------------------------------------------------
print(f'Connected To Tradehub --- {demPK.address}')

try:
    clientDem.create_withdraw(message=tradehub.types.CreateWithdrawMessage(to_address=depositAddress,
                                                        denom=tokenDenom,
                                                       amount=quantityWithdraw,
                                                        fee_amount='1'),
                    blockchain=blockchainType)

    print('WITHDRAWAL DONE!')

except:
    print('WITHDRAWAL FAILED')
