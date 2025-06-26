import java.util.Scanner;
import java.util.ArrayList;
public class DanhSachTaiKhoan {
    static ArrayList<TaiKhoan> danhSach= new ArrayList<>();
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int luaChon;
        do{
            hienMenu();
            luaChon = scanner.nextInt();

            switch (luaChon){
                case 1 -> themTaiKhoan();
                case 2 -> napTien();
                case 3 -> rutTien();
                case 4 -> hienThiTatCa();
                case 0 -> System.out.println("thoat chuong trinh");
                default -> System.out.println("lua khong dung ");
            }
        } while (luaChon !=0);

    }
    public static void hienMenu() {
        System.out.println("Customer");
        System.out.println("1. tao tai khoan");
        System.out.println("2. nap tien");
        System.out.println("3. rut tien");
        System.out.println("4. thong tin tai khoan");
        System.out.println("0. thoat");
        System.out.println("chon chuc nang:");
    }
    public static void themTaiKhoan() {
        scanner.nextLine();
        System.out.print("Nhập tên: ");
        String ten = scanner.nextLine();
        System.out.print("Nhập số điện thoại: ");
        String sdt = scanner.nextLine();
        System.out.print("Nhập số tài khoản: ");
        String stk = scanner.nextLine();

        TaiKhoan tk = new TaiKhoan(ten, sdt, stk);
        danhSach.add(tk);
        System.out.println("Đã thêm tài khoản.");
    }

    public static void napTien() {
        scanner.nextLine();
        System.out.print("Nhập số tài khoản muốn nạp: ");
        String stk = scanner.nextLine();
        System.out.print("Nhập số tiền: ");
        double soTien = scanner.nextDouble();

        TaiKhoan tk = timTaiKhoan(stk);
        if (tk != null) {
            tk.napTien(soTien);
        } else {
            System.out.println(" Không tìm thấy tài khoản.");
        }
    }

    public static void rutTien() {
        scanner.nextLine();
        System.out.print("Nhập số tài khoản muốn rút: ");
        String stk = scanner.nextLine();
        System.out.print("Nhập số tiền: ");
        double soTien = scanner.nextDouble();

        TaiKhoan tk = timTaiKhoan(stk);
        if (tk != null) {
            tk.rutTien(soTien);
        } else {
            System.out.println(" Không tìm thấy tài khoản.");
        }
    }

    public static void hienThiTatCa() {
        System.out.println("\n DANH SÁCH TÀI KHOẢN:");
        for (TaiKhoan t : danhSach) {
            t.hienThi();
        }
    }

    public static TaiKhoan timTaiKhoan(String stk) {
        for (TaiKhoan t : danhSach) {
            if (t.soTaiKhoan.equals(stk)) {
                return t;
            }
        }
        return null;
    }
}