class Solution {
    public int arrangeCoins(int n) {
       int r = 1;
while (n > r) {
    n = n - r;
    r++;
}

if(n ==r){
    return r;
}
else{
    return r-1;
}
        
    }
}