# App where:
#  IN money amount
#  IN currency
#  OUT money amount
print(" Welcome to USD, EUR, and MDL converter!")
in_currency  = input("Enter currency that you want to sell: ")    # str < "USD", "EUR", "MDL"

data_USD_to_EUR_rate = 0.8
data_USD_to_MDL_rate = 17.66
data_EUR_to_USD_rate = 1.25
data_EUR_to_MDL_rate = 19.88
data_MDL_to_USD_rate = 0.06
data_MDL_to_EUR_rate = 0.05

# LOGIC
if in_currency == "USD":
    out_currency = input("Enter currency that you want to buy: ")
    if out_currency == "EUR":
       in_money     = int(input("Enter money: "))
       out_money = in_money * data_USD_to_EUR_rate
       print("Amount of money in EUR that client will receive after the exchange: ", out_money)
    else:
        if out_currency == "MDL":
           in_money     = int(input("Enter money: "))
           out_money = in_money * data_USD_to_MDL_rate
           print("Amount of money in MDL that client will receive after the exchange: ", out_money)
        else:
           print(" This currency cannot be bought ")
elif in_currency == "EUR":
       out_currency = input("Enter currency that you want to buy: ")
       if out_currency == "USD":
          in_money     = int(input("Enter money: "))
          out_money = in_money * data_EUR_to_USD_rate
          print("Amount of money in USD that client will receive after the exchange: ", out_money)
       else: 
          if out_currency == "MDL":
             in_money     = int(input("Enter money: "))
             out_money = in_money * data_EUR_to_MDL_rate
             print("Amount of money in MDL that client will receive after the exchange: ", out_money)
          else:
             print(" This currency cannot be bought ")
elif in_currency == "MDL":
     out_currency = input("Enter currency that you want to buy: ")
     if out_currency == "USD":
       in_money     = int(input("Enter money: "))
       out_money = in_money * data_MDL_to_USD_rate
       print("Amount of money in USD that client will receive after the exchange: ", out_money)
     else:
        if out_currency == "EUR":
           in_money     = int(input("Enter money: "))
           out_money = in_money * data_MDL_to_EUR_rate
           print("Amount of money in EUR that client will receiva after the exchange: ", out_money)
        else:
           print(" This currency cannot be bought ")
else:
    print(" This currency cannot be sold ")