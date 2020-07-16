class Solution {
    public String reverseWords(String s) {
        String[] words = s.split(" +");
        String out = "";
        for (int i = words.length -1; i >= 0; i--){
            out += words[i] + " ";
        }
        return out.trim();
    }
}
