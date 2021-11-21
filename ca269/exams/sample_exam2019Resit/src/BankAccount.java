public class BankAccount {
    private double balance;

    // default constructor
    public BankAccount()
    {
        this.balance = 0;
    }

    public BankAccount(double balance)
    {
        this.balance = balance;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }

    @Override
    public String toString() {
        return "Bank balance is: " + balance;
    }
}
