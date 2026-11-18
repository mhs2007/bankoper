def bankoper(initialBal, deposit, withdraw):
    totalBal = initialBal + deposit
    updatedBal = totalBal - withdraw

    return totalBal, updatedBal

if __name__ == "__main__":
    initialBal = int(input("Enter Amount as initail Balance:"))
    deposit = int(input("Enter amount to Deposit: "))
    withdraw = int(input("Enter withdrawal amount: "))

    totalBal , updatedBal = bankoper(initialBal, deposit, withdraw)

    print("Total Balance : ", totalBal)
    print("Updated Balance: ")