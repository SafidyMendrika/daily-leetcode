import java.util.ArrayList;

class Solution {
    public int maxScore(String s) {
        int maxScore = 0;

        int tempScore = 0;
        ArrayList<String> tempSplited = null;

        for(int i = 1; i< s.length() ; i++){
            tempSplited = this.split(s,i);

            tempScore = this.toInt(tempSplited.get(0),'0') + this.toInt(tempSplited.get(1),'1');
            if(tempScore > maxScore){
                maxScore = tempScore;
            }

        }
        return maxScore;
    }

    public ArrayList<String> split(String binaryString,int index){
        ArrayList<String> result = new ArrayList();
        
        result.add(binaryString.substring(0,index));
        result.add(binaryString.substring(index,binaryString.length()));

        return result;
    }

    public int toInt(String binary,char charToCount){
        char[] chars = binary.toCharArray();
        int count = 0;

        for(char c : chars){
            if(c == charToCount) count++;
        }
        return count;
    }
}