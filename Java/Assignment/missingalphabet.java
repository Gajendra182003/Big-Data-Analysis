import java.util.*;
class missing{
    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        
        System.out.println("Enter start and End Charater:");
        char start = sc.next().charAt(0);
        char end = sc.next().charAt(0);
        
        sc.nextLine();
        System.out.println("Enter Alphabet :");
        String input = sc.nextLine();
        
        for (char ch = start ; ch <= end ; ch ++) {
            if (input.indexOf(ch) == -1) {
                System.out.println("Missing Alphabet is : " +ch);
                break;    
            }
        }        
    }   
}

