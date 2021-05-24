# TradeHubAPIWithdraw<br>
Simple Python Script, using tradehub-python, to withdraw from Tradehub.<br>

Python 3.8+ required. (***BSC CHAIN ISNT SUPPORTED ATM, ONLY NEO AND ETH CHAINS)<br>

Instructions<br>
1)Install Tradehub-python library "pip install tradehub" (https://github.com/Mai-Te-Pora/tradehub-python)<br>
2)Open TradeHubAPIWithdraw.py<br>
3)Change # PARAMETERS settings<br>
4)Run the script<br>


# PARAMETERS<br>
myMnemonic = 'program cram lunch mail clump kebab paela switcheo make people rich now' #Tradehub mnemonic (example here: 12 word TradeHub mnemonic)<br>
depositAddress = '0x1577af8a039414df5ade74453fac4a0a06d1e6ef' #Wallet Address you want to send tokens (example here: ERC-20/BEP-20 address)<br>
tokenDenom = 'busd1' #Quantity to withdraw (example here: 'busd1' = BUSD (BEP-20) on tokenlist.txt)<br>
quantityWithdraw = '8.0' #Quantity to withdraw (example here: '8.0' = 8$)<br>
blockchainType = 'BUSD' #Blockchain ttype (example here: BUSD (BEP-20) on tokenlist.tx)<br>
<br>
tokenlist.txt = https://switcheo.org/tokens?net=main<br>
