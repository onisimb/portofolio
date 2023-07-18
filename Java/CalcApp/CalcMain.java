import java.util.Scanner;

// The calc functions have been saved on a different file
public class CalcMain {
    public static void main(String[] args) {
        Calculator calc = new Calculator(); // A variable storing the data has been created
        System.out.println(calc.substract(12, 15)); // just testing its functionality
        Scanner scanner = new Scanner(System.in); // will allow to scan the keyboard for user inputs
        boolean moreOperations = true;
        System.out.println("Which Operation? (a, s, m, d or x to exit):");
        String choice = scanner.next(); // Stores the user inputs
        while (!choice.equals("x")) {
            System.out.println("Enter first number:");
            int firstNumber = scanner.nextInt();
            System.out.println("Enter the second number:");
            int secondNumber = scanner.nextInt();
            if (choice.equals("a")) {
                System.out.println(calc.add(firstNumber, secondNumber));
            } else if (choice.equals("s")) {
                System.out.println(calc.substract(firstNumber, secondNumber));
            } else if (choice.equals("m")) {
                System.out.println(calc.multiply(firstNumber, secondNumber));
            } else if (choice.equals("d")) {
                System.out.println(calc.division(firstNumber, secondNumber));
            } else {
                System.out.println("Try again, invalid choice.");
            }
            System.out.println("Which Operation? (a, s, m, d or x to exit):");
            choice = scanner.next();

        }
    }
}

// Reference:
// 1 - Created with Sparta global Java Fundamentals course.