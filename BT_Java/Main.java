import java.util.*;

class  Car{
    //data
    private String make;
    private String model;
    private String color;
    private int door;

    public String getMake() {
        return make;
    }

    public void setMake(String make) {
        this.make = make;
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public int getDoor() {
        return door;
    }

    public void setDoor(int door) {
        this.door = door;
    }

    //method
    void showCar(){
        System.out.format("\nMake %s, Model %s, Color %s, Door %d",make,model,color,door);
    }
}
class PhanSo{
    private int tuSo;
    private int mauSo;

    public PhanSo() {
    }

    public PhanSo(int tuSo, int mauSo) {
        this.tuSo = tuSo;
        this.mauSo = mauSo;
    }

    void showPS(){
        System.out.format("\n%d/%d",tuSo,mauSo);
    }

    public int getTuSo() {
        return tuSo;
    }

    public void setTuSo(int tuSo) {
        this.tuSo = tuSo;
    }

    public int getMauSo() {
        return mauSo;
    }

    public void setMauSo(int mauSo) {
        this.mauSo = mauSo;
    }

}


class NhanVien{
    private String name;
    private int age;
    private boolean gender;
    private double salary;

    public NhanVien() {
    }

    public NhanVien(String name, int age, boolean gender, double salary) {
        this.name = name;
        this.age = age;
        this.gender = gender;
        this.salary = salary;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public boolean isGender() {
        return gender;
    }

    public void setGender(boolean gender) {
        this.gender = gender;
    }

    public double getSalary() {
        return salary;
    }

    public void setSalary(double salary) {
        this.salary = salary;
    }

    void nhapNV() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Nhap ten: ");
        setName(sc.next());
        System.out.print("Nhap tuoi: ");
        setAge(sc.nextInt());
        System.out.print("Nhap gioi tinh: ");
        setGender(sc.nextBoolean());
        System.out.print("Nhap luong: ");
        setSalary(sc.nextDouble());
    }

    @Override
    public String toString() {
        return "NhanVien{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", gender=" + gender +
                ", salary=" + salary +
                '}';
    }
}




public class Main {


    public static void menu(){
        List<Account> listAc= new ArrayList<Account>();
        int choose;
        do{
            System.out.println();
            System.out.println("Bank System");
            System.out.println("[1]. Add Acounts");
            System.out.println("[2]. Show Acounts");
            System.out.println("[3]. DepositFunds");
            System.out.println("[4]. WithdrawFunds");
            System.out.println("[0]. exit");

            System.out.print("Please choose an option: ");
            Scanner sc = new Scanner(System.in);
            choose = sc.nextInt();

            switch (choose){
                case 1:
                    System.out.println("How many accounts you want to create: ");
                    int n = sc.nextInt();

                    for (int i = 0; i<n;i++)
                    {
                        System.out.println("Create acction:");
                        Account ac = new Account();
                        ac.nhap();
                        listAc.add(ac);
                    }

                    break;
                case 2:
                    System.out.println("List Account");
                    for (Account ac : listAc)
                    {
                        System.out.println("Account Info:");
                        System.out.println(ac.toString());
                    }

                    break;
                case 3:
                    System.out.println("Chooe an account: ");
                    int c = sc.nextInt();
                    System.out.println("Enter money: ");
                    double money = sc.nextDouble();
                    listAc.get(c).depositFunds(money);

                    break;
                case 4:
                    System.out.println("Chooe an account: ");
                    int c1 = sc.nextInt();
                    System.out.println("Enter money: ");
                    double money1 = sc.nextDouble();
                    listAc.get(c1).withdrawFunds(money1);

                    break;
                case 0:
                    break;
            }


        }while (choose != 0);


    }
    public static void main(String[] args) {
//        Car car = new Car();
//        car.make="abc";
//        car.model="ford";
//        car.color="blue";
//        car.door=4;
//        car.showCar();


//        PhanSo ps = new PhanSo();
//        Scanner sc = new Scanner(System.in);
//        System.out.print("Nhap tu so: ");
//        ps.setTuSo(sc.nextInt());
//        System.out.print("Nhap mau so: ");
//        ps.setMauSo(sc.nextInt());
//        ps.showPS();

//        Tao ds nhan vien co fullname,age,gender,salary

//
//        List<NhanVien> listNV = new ArrayList<NhanVien>();
//        Scanner sc = new Scanner(System.in);
//        System.out.print("Nhap so luong nhan vien: ");
//        int n = sc.nextInt();
//        for (int i = 0;i<n;i++){
//            System.out.println("Nhap nhan vien thu "+i);
//            NhanVien nv = new NhanVien();
//            nv.nhapNV();
//            listNV.add(nv);
//        }
//        System.out.println("Danh sach NV: ");
//        for (NhanVien nv : listNV) {
//            System.out.println(nv.toString());
//        }

    menu();

    }
}