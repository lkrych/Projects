
/**
 * Reads through DNA string input to return genes found in string
 * 
 * @author LelandK 
 * 
 */
import edu.duke.*;
import java.io.*;

public class findAllGenes_update {
    public int findStopIndex(String dna, int index){
   
    int stop1 = dna.indexOf("tga",index);
    if (stop1 == -1 || (stop1-index)% 3 != 0){
        stop1 = dna.length();
    }
    int stop2 = dna.indexOf("taa",index);
    if (stop2 == -1 || (stop2-index)% 3 != 0){
        stop2 = dna.length();
    }
    int stop3 = dna.indexOf("tag",index);
    if (stop3 == -1 || (stop3-index)% 3 != 0){
        stop3 = dna.length();
    }
    int minLength = Math.min(stop1,Math.min(stop2,stop3));
    if (minLength == dna.length()){
        return -1;
    }
    else{
        return minLength;
    }
    }


    public void printAll(String dna){
        int start = 0;
        dna = dna.toLowerCase();
        while(true){
            int tag = dna.indexOf("atg",start);
            if(tag == -1){
                break;
            }
            int end =findStopIndex(dna,tag+3);

            if(end != dna.length()){
                System.out.println(dna.substring(tag,end+3));
                start = end +3;
            }
            else{
                start = start + 3;
            }
        }
    }

    public StorageResource storeAll(String dna){
        StorageResource store = new StorageResource();
        dna = dna.toLowerCase();
        int start = 0;
        while(true){
            int tag = dna.indexOf("atg",start);
            if(tag == -1){
                break;
            }
            int end =findStopIndex(dna,tag+3);

            if(end != -1){
                store.add(dna.substring(tag,end+3));
                start = end +3;
            }
            else{
                start = start + 3;
            }
        }
        return store;
    }

    public void testFinder(){
        printAll("ATGAAATGAAAA");
        printAll("ccatgccctaataaatgtctgtaatgtaga");
        //printAll("CATGTAATAGATGAATGACTGATAGATATGCTTGTATGCTATGAAAATGTGAAATGACCCA");

    }
    
    public float cgRatio(String dna){
        dna = dna.toLowerCase();
        int countC = 0;
        int countG = 0;
        
        int index = 0;
        while(true){
           int start = dna.indexOf("c", index);
           if(start == -1){
               break;
               }
           index = start + 1;
           countC = countC + 1;
            }
        index = 0;    
        while(true){
           int start = dna.indexOf("g", index);
           if(start == -1){
               break;
               }
           index = start + 1;
           countG = countG + 1;
            }    
 
        float gc = countG + countC;
        return gc/dna.length();
        
    }

    public int ctgCount(String dna){
        dna = dna.toLowerCase();
        int countCTG = 0;
        int index = 0;
        while(true){
            int start = dna.indexOf("ctg",index);
            if(start == -1){
                break;
            }
            index = start + 1;
            countCTG = countCTG + 1;
        }
        return countCTG;

    }

    public void testStorageFinder(String file){
        FileResource f = new FileResource(file);
		String source = f.asString();
        StorageResource s1 = storeAll(source);
        printGenes(s1);
        System.out.println("There are " + s1.size() + " genes");
       }
    

    public void printGenes(StorageResource sr){
        int threefive = 0;
        int greatsixty = 0;
        int longest = 0;
        for(String gene: sr.data()){
            if (cgRatio(gene) > 0.35){
                System.out.println(gene.length() + "\t" + gene );
                threefive = threefive + 1;
            }
            if (gene.length() > 60){
                System.out.println(gene.length() + "\t" + gene );
                greatsixty = greatsixty + 1;
            }
            if (gene.length() > longest){
                longest = gene.length();
            }
        }
        System.out.println("There are " + threefive + " genes with greater than 35% gc content");
        System.out.println("There are " + greatsixty + " genes longer than 60 codons");
        System.out.println("The longest gene has " + longest + " codons.");
    }   
}
