public class Task2_33 {
    public static void main(String[] args) {
        int year_Tanya = 12;
        int year_Mitya = 34;

        int avg_year = (year_Mitya + year_Tanya) / 2;
        int from_avg_Tanya = Math.abs(avg_year - year_Tanya);
        int from_avg_Mitya = Math.abs(avg_year - year_Mitya);
        System.out.println(avg_year);
        System.out.println(from_avg_Mitya);
        System.out.println(from_avg_Tanya);
    }
}
