class Solution {
public:
    bool isPalindrome(int x) {
        string s = to_string(x);
        string str = s;
        reverse(str.begin(), str.end()); 
        return str == s;
    }
};
