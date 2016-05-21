import java.util.*;
import edu.duke.*;
import java.io.*;

public class VigenereBreaker {
    public String sliceString(String message, int whichSlice, int totalSlices) {
        /** This method is used to break a vigenere cipher, it takes the encrypted message as input, as
           well as the keyLength = totalSlices, and the int value for which slice we are currently
           decrypting = whichSlice. It returns the sliced string indexed by whichSlice*/
        StringBuilder slice = new StringBuilder();
        Character currVal = ' ';
        for(int i = whichSlice; i < message.length(); i += totalSlices){
            
            currVal = message.charAt(i);
            slice.append(currVal);
        }
        return slice.toString();
    }

    public int[] tryKeyLength(String encrypted, int klength, char mostCommon) {
        /** This method takes in an encrypted string and finds the vigenere key( an array of caesar cipher keys) 
           given the length of the key. It also takes in a character for the most common character of a specific language 
           which is used in the caesar cipher object*/
        int[] key = new int[klength];
        for(int i = 0; i < klength; i++){
            String slice = sliceString(encrypted, i, klength);
            CaesarCracker cc = new CaesarCracker(mostCommon);
            int currKey = cc.getKey(slice);
            key[i] = currKey;
        }
        return key;
    }

    public void breakVigenere () {
        /** This method allows you to select an encrypted file, and decrypt it */
        FileResource file = new FileResource();
        DirectoryResource dr = new DirectoryResource();
        HashMap<String, HashSet<String>> mapDictionary = new HashMap<String, HashSet<String>>();
        for(File dictionary : dr.selectedFiles()){
            String fullFilePath = dictionary.toString();
            String shortFilePath = fullFilePath.substring(fullFilePath.lastIndexOf("/") + 1, fullFilePath.length());
            FileResource f = new FileResource(fullFilePath);
            HashSet<String> set = readDictionary(f);
            mapDictionary.put(shortFilePath,set);
            System.out.println("The " + shortFilePath + " dictionary has been made" );
        }
        String encrypted = file.asString();
        String decrypted = breakForAllLanguages(encrypted, mapDictionary);
        

       
        //System.out.println(decrypted);
    
        }
    
    public HashSet<String> readDictionary(FileResource fr) {
        /** This method saves the words in a language file into a HashSet */
        HashSet<String> hash =  new HashSet<String>();
        String file = fr.asString();
        String[] words= file.split("\\W+");
        for(int i = 0; i < words.length; i++){
            String currWord = words[i].toLowerCase();
            hash.add(currWord);
        
        }
        return hash;
    }
    
    public int countWords(String message, HashSet<String> dictionary){
        /** This method compares the words in message to the words in the HashSet dictionary
           We will use this method to evaluate whether the encrypted message has words from the 
           language we are looking at*/
        String[] currWords = message.split("\\W+");
        int count = 0;
        for(int i = 0; i < currWords.length; i++){
            String currentWord = currWords[i].toLowerCase();
            if(dictionary.contains(currentWord) && currentWord != "s"){
                count += 1;
            }           
        }
        return count;
    }
    
    public String breakForLanguage(String encrypted, HashSet<String> dictionary, char mostCommon){
        /** This method compares the words found in encrypted to the words in the HashSet dictionary  */
        int max = 0;
        int maxDex = 0;
        int[] rightArray = new int[1];
        for (int i = 1; i <= 100; i++){
            int[] keyArray = tryKeyLength(encrypted, i, mostCommon);
            VigenereCipher vc = new VigenereCipher(keyArray);
            String decrypted = vc.decrypt(encrypted);
            int currCount = countWords(decrypted, dictionary);
            if(currCount > max){
                max = currCount;
                maxDex = i;
                rightArray = keyArray;
            }
            
        }
        System.out.println("The key length used is " + maxDex + " and the number of words is " + max);
        VigenereCipher vc = new VigenereCipher(rightArray);
        String decrypted = vc.decrypt(encrypted);
        return decrypted; 
    
    }
    
    public char mostCommonCharIn(HashSet<String> dictionary){
        /** This method does three things
           1) creates a HashMap counts of the alphabet and counts of those letters
           2) counts the amount of times the letters are used in the Hashset dictonary that's passed into the method
           3) loops through the Hashmap counts and returns the letter that was used the most.*/
        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        HashMap<Character,Integer> counts = new HashMap<Character,Integer>();//initialize count map
        for(int i = 0; i < alphabet.length(); i++){
            char c = alphabet.charAt(i);
            counts.put(c,0);
        }
    
        for (String s : dictionary){ //add letters to counts
            for(int i = 0; i < s.length(); i++){
                char c = s.charAt(i);
                if(counts.containsKey(c)){
                    counts.put(c,counts.get(c) + 1);
            }
           }
        }
        
        int max = 0;//check to see which letter has highest count
        char maxChar = 0;
        
        for(int i = 0; i < alphabet.length(); i++){
            char c = alphabet.charAt(i);
            int currVal = counts.get(c);
            if(currVal > max){
                max = currVal;
                maxChar = c;
            }
        }
        return maxChar;
        }
        
    public String breakForAllLanguages(String encrypted, HashMap<String, HashSet<String>> languages){
        int max = 0;
        int maxDex = 0;
        String mostLikely = "";
        int[] rightArray = new int[1];
        for(String language : languages.keySet() ){
            HashSet<String> languageCount = languages.get(language);
            char mostCommon = mostCommonCharIn(languageCount);
            int currMax = 0;
            int currMaxDex = 0;
            int[] currRightArray = new int[1];
            for (int i = 1; i <= 100; i++){
                int[] keyArray = tryKeyLength(encrypted, i, mostCommon);
                VigenereCipher vc = new VigenereCipher(keyArray);
                String decrypted = vc.decrypt(encrypted);
                int currCount = countWords(decrypted, languageCount);
                if(currCount > max){
                    max = currCount;
                    mostLikely = language;
                    maxDex = i;
                    rightArray = keyArray;
                }
            }
        }
        System.out.println("The key length used is " + maxDex + " and the number of words is " + max);
        System.out.println("The language used was " + mostLikely);
        VigenereCipher vc = new VigenereCipher(rightArray);
        String decrypted = vc.decrypt(encrypted);
        return decrypted; 
    
    }    
    }

