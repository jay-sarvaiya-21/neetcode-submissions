class Solution {
    public boolean isAnagram(String s, String t) {

        int[] charc = new int [26];
        if (s.length()!=t.length()){
            return false;
        }
        for (int i =0; i <s.length();i++) {
            charc[s.charAt(i) - 'a']++;
            charc[t.charAt(i) - 'a']--;
        }

        for (int i: charc) {
            if (i !=0 ){
                return false;
            }
        }
        return true;
    }
}
