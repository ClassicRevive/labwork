public class TestBankAccount
{
    public static void main(String [] args)
    {
        BankAccount account1 = new BankAccount(); // This uses the default constructor.
        BankAccount account2 = new BankAccount(900); // This uses one argument constructor.
        account2.deposit(100);
        System.out.println("Account 1 has " + account1.balance);
        System.out.println("Account 2 has " + account2.balance);
        System.out.println(account2);
    }
}