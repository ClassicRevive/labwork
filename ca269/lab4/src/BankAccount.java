public class BankAccount {
    double balance;

    public BankAccount(double b)
    {
        balance = b;
    }
    public BankAccount()  // default constructor
    {
        balance = 100;
    }
    public void withdraw(double amount)
    {
        this.balance -= amount;
    }
    public void deposit(double amount)
    {
        this.balance += amount;
    }
    public double getBalance()
    {
        return this.balance;
    }
    public void setBalance(double amount)
    {
        this.balance = amount;
    }

    public String toString() {
        return "The balance is "+getBalance();
    }
}
