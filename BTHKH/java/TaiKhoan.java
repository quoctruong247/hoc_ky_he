import java.io.PrintStream;

class TaiKhoan {
    String ten;
    String sdt;
    String soTaiKhoan;
    double soDu;

    public TaiKhoan(String ten, String sdt, String soTaiKhoan) {
        this.ten = ten;
        this.sdt = sdt;
        this.soTaiKhoan=soTaiKhoan;
        this.soDu = 0;
    }
    public void napTien(double soTien){
        if(soTien>soDu) {
            soDu += soTien;
            System.out.println("Da nap: " + soTien + "VND");
        }
        else if (soTien<=0) {
            System.out.println("so du khong du");
        }
        else {
            soDu -=soTien;
            System.out.println("da rut thanh cong"+ soTien +"VND");
        }
    }
    public void rutTien(double soTien){
        if (soTien <= 0){
            System.out.println("so tien phai lon hon 0");
        } else if (soTien > soDu) {
            System.out.println("phai nap tien");
        }
        else {
            soDu -=soTien;
            System.out.println("da rut thanh cong"+ soTien +"VND"+"so du con lai la"+soDu);
        }

    }
    public void hienThi(){
        System.out.println("ten: "+ten);
        System.out.println("sdt: "+sdt);
        System.out.println("STK: "+sdt);
        System.out.println("so du: "+soDu+"VND");
    }
}