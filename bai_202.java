class Solution {
    public boolean isHappy(int n) {
          int squareSum, digit;
    Set<Integer> previousResults = new HashSet<Integer>();
    
    while (previousResults.add(n)) {
        squareSum = 0;
        while (n > 0) {
            digit = n % 10;
            squareSum += digit * digit;
            n /= 10;
        }
        if (squareSum == 1) {
            return true;
        } else {
            n = squareSum;
        }
    }
    return false;
}
}