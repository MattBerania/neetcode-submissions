// import java.util.Hashtable;

class Solution {
    public boolean isAnagram(String s, String t) {
        Hashtable<Character, Integer> sHash = new Hashtable<>();
        Hashtable<Character, Integer> tHash = new Hashtable<>();

        for(int i = 0; i < s.length(); i++) {
            if(sHash.containsKey(s.charAt(i)) == false) {
                sHash.put(s.charAt(i),1);
            }
            else{
                int temp = sHash.get(s.charAt(i)) + 1;
                sHash.replace(s.charAt(i),temp);
            }
        }
        for(int i = 0; i < t.length(); i++) {
            if(tHash.containsKey(t.charAt(i)) == false) {
                tHash.put(t.charAt(i),1);
            }
            else{
                int temp = tHash.get(t.charAt(i)) + 1;
                tHash.replace(t.charAt(i),temp);
            }
        }

        return sHash.equals(tHash);
    }
}
