import java.util.*;

public class triangletype {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double a = sc.nextDouble();
        double b = sc.nextDouble();
        double c = sc.nextDouble();

        double eps = 0.000001;

        // Step 1: Check valid triangle
        if (a + b <= c || a + c <= b || b + c <= a) {
            System.out.println("invalid");
            return;
        }

        // Step 2: Check right-angled
        double a2 = a * a;
        double b2 = b * b;
        double c2 = c * c;

        if (Math.abs(a2 + b2 - c2) <= eps ||
            Math.abs(a2 + c2 - b2) <= eps ||
            Math.abs(b2 + c2 - a2) <= eps) {
            System.out.println("right-angled");
        }
        // Step 3: Check equilateral
        else if (Math.abs(a - b) <= eps && Math.abs(b - c) <= eps) {
            System.out.println("equilateral");
        }
        // Step 4: Check isosceles
        else if (Math.abs(a - b) <= eps ||
                 Math.abs(b - c) <= eps ||
                 Math.abs(a - c) <= eps) {
            System.out.println("isosceles");
        }
        // Step 5: Otherwise
        else {
            System.out.println("notspecial");
        }

        sc.close();
    }
}
