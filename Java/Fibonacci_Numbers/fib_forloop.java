package Java.Fibonacci_Numbers;

import java.util.*;

public class fib_forloop{
    public static void main(String[] args){
        //Initialize 0 and 1 for Fibonacci sequence 
        int x = 0;
        int y = 1;

        //Initalize input scanner
        Scanner input = new Scanner(System.in);

        //Prompt user for number of iterations
        System.out.println("Enter number of iterations: ");
        int n = input.nextInt();

        //Print first two numbers
        System.out.println();
        System.out.println(x);
        System.out.println(y);

        //Generate Fibonacci sequence with n iterations
        for(int i = 0; i < n; i++){
            int newFibo = y + x;
            System.out.println(newFibo);
            x = y;
            y = newFibo;
        }

        input.close();
    }
}