
import java.util.*;

public class EfficientMarkovWord implements IMarkovModel {
    private String[] myText;
    private Random myRandom;
    private int myOrder;
    private HashMap<Integer,ArrayList<String>> map;
    
    public EfficientMarkovWord(int order) {
        myRandom = new Random();
        myOrder = order;
        map = new HashMap<Integer, ArrayList<String>>();
    }
    
    public void setRandom(int seed) {
        myRandom = new Random(seed);
    }
    
    public void setTraining(String text){
        myText = text.split("\\s+");
    }
    
    private int indexOf(String[] words, WordGram target, int start ){
       /* This method starts looking at the start position and returns the first index 
        * location in words that matches target. If no word is found, then this method returns -1.       */
       for(int k = start; k < words.length-target.length(); k++){
           WordGram wg = new WordGram(words,k,target.length());
           if(target.equals(wg)){
               return k;
            }
       
       }
       return -1;
       }
       
    public String getRandomText(int numWords){
        StringBuilder sb = new StringBuilder();
        int index = myRandom.nextInt(myText.length-myOrder);  // random word to start with
        WordGram key = new WordGram(myText,index, myOrder);
        sb.append(key);
        sb.append(" ");
        for(int k=0; k < numWords-myOrder; k++){
            ArrayList<String> follows = getFollows(key);
            if (follows.size() == 0) {
                break;
            }
            index = myRandom.nextInt(follows.size());
            String next = follows.get(index);
            sb.append(next);
            sb.append(" ");
            key = key.shiftAdd(next);
        }
        
        return sb.toString().trim();
    }
    
    private ArrayList<String> getFollows(WordGram kGram) {
        //create an arrayList of words that follow the key
        ArrayList<String> follows = new ArrayList<String>();
        int position = 0;
        int key = kGram.hashCode();
         if(map.containsKey(key) == false){ 
            while(position < myText.length-myOrder){
               int start = indexOf(myText,kGram,position);
               if(start == -1){
                   break;
                }
               if ((start+(kGram.length())) >= myText.length){
                   break;
                }
               String nextWord = myText[start + myOrder];
               
               follows.add(nextWord);
           
               position = start + myOrder;
            }
           
           map.put(key,follows);
         }
        else{
          follows = map.get(key);
        }
        return follows;
    }
    

    public void printHashMapInfo(){
        System.out.println("The HashMap has " + map.size() +  " entries.");
        int maxValue = 0;
        ArrayList<Integer> maxKeys = new ArrayList<Integer>();
        for (int key : map.keySet()) {
         // process each value in turn 
            int currentValue = map.get(key).size();
            if (currentValue >= maxValue){
                maxValue = currentValue;
            }
        }
        //use a second loop to add the keys with a highest value to the arrayList
        for(int key : map.keySet()){
            if (map.get(key).size() == maxValue){
                maxKeys.add(key);
                System.out.println(map.get(key) + " is the entry for a max key.");
            }
        
        }
        System.out.println("The keys with the most entries were " + maxKeys);
        System.out.println("The values of those keys were " + maxValue);
    }
}
