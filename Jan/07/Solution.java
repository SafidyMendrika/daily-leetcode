class Solution {
    public List<String> stringMatching(String[] words) {
        ArrayList<String> result = new ArrayList();

        String s = null;
        for(int i = 0 ; i < words.length; i++) {
            s = words[i];
            if(this.isSubString(s,words,i)) result.add(s);
        }
        return result;
    }

    public boolean isSubString(String s, String[] words,int index){
        String word = null;
        for(int i = 0 ; i < words.length ; i++){
            if(i == index) continue;

            word = words[i];
            if(word.equals(s) == false && word.indexOf(s) != -1)return true;
        }
        return false;
    }

}