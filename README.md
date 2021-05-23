# TradeHubAPIWithdraw
Simple Python Script, using tradehub-python, to withdraw from Tradehub.

Python 3.8+ required. (***BSC CHAIN ISNT SUPPORTED ATM, ONLY NEO AND ETH CHAINS)

Instructions
1)Install Tradehub-python library "pip install tradehub" (https://github.com/Mai-Te-Pora/tradehub-python)
2)Open TradeHubAPIWithdraw.py
3)Change # PARAMETERS settings
4)Run the script


# PARAMETERS
# ------------------------------------------------------------------------------
myMnemonic = 'program cram lunch mail clump kebab paela switcheo make people rich now' #Tradehub mnemonic (example here: 12 word TradeHub mnemonic)
depositAddress = '0x1577af8a039414df5ade74453fac4a0a06d1e6ef' #Wallet Address you want to send tokens (example here: ERC-20/BEP-20 address)
tokenDenom = 'busd1' #Quantity to withdraw (example here: 'busd1' = BUSD (BEP-20) on tokenlist.txt)
quantityWithdraw = '8.0' #Quantity to withdraw (example here: '8.0' = 8$)
blockchainType = 'BUSD' #Blockchain ttype (example here: '8.0' = 8$)

tokenlist.txt = https://switcheo.org/tokens?net=main
