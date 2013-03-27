def checkio(data):
    global balance, withdrawal
    balance, withdrawal = data
    return balance, withdrawal

x = checkio([1,3])
print(x)
