import java.util.Scanner;

public class ScrabbleMain {
    public static void main(String[] args) {
        ScrabbleScore scorer = new ScrabbleScore();
        System.out.println("Enter The word to calculate the scrabble score:");
        Scanner scanner = new Scanner(System.in);
        String word = scanner.next();
        while (!word.equals("")){
            System.out.println("The score for " + word + " is " + scorer.getScrabbleScore(word));
            System.out.println("Enter The word to calculate the scrabble score:");
            word = scanner.next();
        }
    }
}

// Reference:
// 1 - Created with Sparta global Java Fundamentals course