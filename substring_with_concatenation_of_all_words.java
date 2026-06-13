class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> ans = new ArrayList<>();
        if (s.length() == 0 || words.length == 0) return ans;

        int len = words[0].length();
        int total = len * words.length;

        Map<String, Integer> map = new HashMap<>();
        for (String w : words)
            map.put(w, map.getOrDefault(w, 0) + 1);

        for (int i = 0; i <= s.length() - total; i++) {
            Map<String, Integer> seen = new HashMap<>();
            int j = 0;

            while (j < words.length) {
                String word = s.substring(i + j * len, i + (j + 1) * len);

                if (!map.containsKey(word)) break;

                seen.put(word, seen.getOrDefault(word, 0) + 1);

                if (seen.get(word) > map.get(word)) break;

                j++;
            }

            if (j == words.length) ans.add(i);
        }

        return ans;
    }
}