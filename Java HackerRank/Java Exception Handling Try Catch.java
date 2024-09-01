//Written by Gskd
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


public class Solution {


    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);


        try {

            int x = scanner.nextInt();
            int y = scanner.nextInt();


            int result = x / y;


            System.out.println(result);


        } catch (java.util.InputMismatchException e) {
            System.out.println("java.util.InputMismatchException");


        } catch (ArithmeticException e) {
            System.out.println("java.lang.ArithmeticException: / by zero");


        } finally {
            scanner.close();
        }

    }
}

