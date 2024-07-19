package Java.Fibonacci_Numbers;

import java.util.*;

public class fib_recursion {
    public static void main(String[] args){
        //Initalize variables
        int iterations;
        Scanner input = new Scanner(System.in);

        //Get number of iterations from user
        System.out.println("Enter number of iterations: ");
        iterations = input.nextInt();

        //Initalize array for Fibonacci sequence
        int[] sequence = new int[iterations];
        sequence[0] = 0;
        sequence[1] = 1;

        input.close();

        fibonacci(iterations, sequence);
    }

    public static void fibonacci(int n, int[] sequence){
        for(int i = 0; i < sequence.length; i++){
            if(i < n){

            }
        }
    }
}
