import java.util.Scanner;

public class Account {
    private String number;
    private double balance;
    private String customerName;
    private String CustomerEmail;
    private String customerPhone;

    public Account() {
    }

    public Account(String number, double balance, String customerName, String customerEmail, String customerPhone) {
        this.number = number;
        this.balance = balance;
        this.customerName = customerName;
        CustomerEmail = customerEmail;
        this.customerPhone = customerPhone;
    }

    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }

    public String getCustomerName() {
        return customerName;
    }

    public void setCustomerName(String customerName) {
        this.customerName = customerName;
    }

    public String getCustomerEmail() {
        return CustomerEmail;
    }

    public void setCustomerEmail(String customerEmail) {
        CustomerEmail = customerEmail;
    }

    public String getCustomerPhone() {
        return customerPhone;
    }

    public void setCustomerPhone(String customerPhone) {
        this.customerPhone = customerPhone;
    }

    @Override
    public String toString() {
        return "Account{" +
                "number='" + number + '\'' +
                ", balance=" + balance +
                ", customerName='" + customerName + '\'' +
                ", CustomerEmail='" + CustomerEmail + '\'' +
                ", customerPhone='" + customerPhone + '\'' +
                '}';
    }



    public void depositFunds(double depositAmount){
        balance+=depositAmount;
        System.out.println("Deposit of $"+depositAmount+ "made. New balance: $"+balance);
    }

    public void withdrawFunds(double withdrawAmout){
        if(balance-withdrawAmout < 0)
        {
            System.out.println("insufficient, You are only $"+balance);
        }
        else {
            balance -= withdrawAmout;
            System.out.println("Withdraw $"+balance+" success, your balance is $"+balance);
        }
    }
    public void nhap(){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a numberAccount: ");
        setNumber(sc.next());
        System.out.print("Enter balance default: ");
        setBalance(sc.nextDouble());
        System.out.print("Enter a custommerName: ");
        setCustomerName(sc.next());
        System.out.print("Enter a custommerEmail: ");
        setCustomerEmail(sc.next());
        System.out.print("Enter a custommerPhone: ");
        setCustomerPhone(sc.next());
    }


}
