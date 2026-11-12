class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> seenChars = new HashMap<>(); //char, index last seen
        int firstIndex = 0;
        int curMax = 1;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (seenChars.getOrDefault(c, -1) >= firstIndex) {
                curMax = Math.max(i - firstIndex, curMax);
                firstIndex = seenChars.get(c) + 1;
            } else if (i == s.length() - 1) {
                curMax = Math.max(s.length() - firstIndex, curMax);
            }
            seenChars.put(c, i);
            
        }
        if (firstIndex == 0) {
            return s.length();
        }
        return curMax;
    }
}
