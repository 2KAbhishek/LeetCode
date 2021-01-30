class Solution {
    public boolean isPalindrome(int x) {
        StringBuffer xs = new StringBuffer();
        xs.append(x);
        return xs.toString().equals(xs.reverse().toString());
    }
}
