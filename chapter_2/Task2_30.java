public class Task2_30 {
    public static void main(String[] args) {
        double x1 = 0, y1 = 0;
        double x2 = 4, y2 = 0;
        double x3 = 4, y3 = 3;
        double x4 = 0, y4 = 3;

        double area = Math.abs(x1*(y2 -y3) + x2*(y3 - y1) + x3*(y1-y2)) / 2 + Math.abs(x1*(y3 - y4) + x3*(y4-y1) + x4*(y1-y3)) / 2;
        System.out.println(area);
    }
}