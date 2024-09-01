//Written by Gskd
public PerformOperation isOdd() {
       return n -> n % 2 != 0;
   }

   public PerformOperation isPrime() {
       return n -> {
           if (n < 2)
               return false;
           for (int i = 2; i * i <= n; i++) {
               if (n % i == 0)
                   return false;
           }
           return true;
       };
   }

   public PerformOperation isPalindrome() {
       return n -> {
           int reversed = 0, original = n;
           while (n != 0) {
               int digit = n % 10;
               reversed = reversed * 10 + digit;
               n /= 10;
           }
           return original == reversed;
       };
   }
}

