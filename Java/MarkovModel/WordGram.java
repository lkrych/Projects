import java.util.*;

public class WordGram {
    private String[] myWords;
    private HashMap<String,Integer> mapCodes;

    public WordGram(String[] source, int start, int size) {
        myWords = new String[size];
        System.arraycopy(source, start, myWords, 0, size);
        mapCodes = new HashMap<String,Integer>();
    }

    public String wordAt(int index) {
        if (index < 0 || index >= myWords.length) {
            throw new IndexOutOfBoundsException("bad index in wordAt "+index);
        }
        return myWords[index];
    }

    public int length(){
        return myWords.length;
    }

    public String toString(){
        String ret = "";
        for(int k = 0 ; k < myWords.length; k++){
            ret += myWords[k] + " ";
        }

        return ret.trim();
    }

    public boolean equals(Object o) {
        WordGram other = (WordGram) o;
        if(this.length() != other.length()){
            return false;
        }
        for(int k = 0; k < myWords.length; k++){
            if(! myWords[k].equals(other.wordAt(k))){
                return false;
            
            }
        }
        return true;
    }

    public WordGram shiftAdd(String word) {
        /* remove first element of Array and add to last element of Array by converting into ArrayList */
        ArrayList<String> myList =  new ArrayList<String>(Arrays.asList(myWords));
        myList.remove(0);
        myList.add(word);
        String[] modMyWords = myList.toArray(new String[myList.size()]);
         
        WordGram out = new WordGram(modMyWords, 0, myWords.length);
        // shift all words one towards 0 and add word at the end. 
        // you lose the first word
        
            
        
        return out;
    }
    
    public int hashCode(){
        String azString = String.join(" ", myWords);//String method to convert myWords array into string
        int code = azString.hashCode();
        if(mapCodes.containsKey(azString) == false){
            mapCodes.put(azString,code);
        }
        else{
            code = mapCodes.get(azString);
        }
        return code;
    
    
    }
}