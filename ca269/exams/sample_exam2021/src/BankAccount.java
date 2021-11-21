public class BankAccount {
    private double balance;

    public BankAccount()  // default constructor
    {
        balance = 0;
    }

    public BankAccount(int bal)  // set balance constructor
    {
        this.balance = bal;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }

    @Override
    public String toString() {
        return "The balance is "+this.getBalance()+'.';
    }
}
