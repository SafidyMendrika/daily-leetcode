public class Solution {
    public int countPrefixSuffixPairs(String[] words) {
        int count = 0;

        String word = null;;
        for(int i=0 ; i< words.length-1 ; i++){
            word = words[i];
            for(int j=i+1 ; j< words.length ; j++){
                if (words[j].length() < word.length()){
                    continue;                    
                }
                if(!words[j].startsWith(word))continue;
                if(!words[j].endsWith(word)) continue;
                count++;
            }
        }
        return count;
    }
}
