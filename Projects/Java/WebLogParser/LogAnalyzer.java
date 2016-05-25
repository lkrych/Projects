


import java.util.*;
import edu.duke.*;

public class LogAnalyzer
{
     private ArrayList<LogEntry> records;
     
     public LogAnalyzer() {
         records = new ArrayList<LogEntry>();
         
     }
        
     public void readFile(String filename) {
         FileResource file = new FileResource(filename);
         for(String line : file.lines()){
            LogEntry logEnt = WebLogParser.parseEntry(line);
            records.add(logEnt);
            }
     }
        
     public void printAll() {
         for (LogEntry le : records) {
             System.out.println(le);
         }
     }
     public int countUniqueIPs(){
         ArrayList<String> copy = new ArrayList<String>();
            for (LogEntry le: records){
                String address = le.getIpAddress();
                if(!copy.contains(address)){
                    copy.add(address);
                }
            
            }
        
         return copy.size();
        }
     
     public void printAllHigherThanNum(int num){
        
        for (LogEntry le: records){
                int code = le.getStatusCode();
                if(code > num){
                   System.out.println(le);
                }
            
            }
        
        }
     
     public ArrayList uniqueIPVisitsOnDay(String someday){
        ArrayList<String> copy = new ArrayList<String>();
        
        for (LogEntry le: records){
                Date date = le.getAccessTime();
                String address = le.getIpAddress();
                String date2 = date.toString();
                if(date2.indexOf(someday) > 0 && !copy.contains(address)){
                    copy.add(le.getIpAddress());
                }
                
                
                }
        return copy;
            }
     
     public int countUniqueIPsInRange(int low, int high){
        ArrayList<String> copy = new ArrayList<String>();
        
        int count = 0;
        for (LogEntry le : records){
           int code = le.getStatusCode();
           String address = le.getIpAddress();
           if(code >= low && code <= high && !copy.contains(address)){
               count +=1;
               copy.add(le.getIpAddress());
                }
                
                
                }
        return count;
            }
     
     public HashMap<String,Integer> countVisitsPerIP(){
        HashMap<String,Integer> counts = new HashMap<String,Integer>();
        
        for(LogEntry le : records){
            
            String ip = le.getIpAddress();
            
            if(! counts.containsKey(ip)){
                counts.put(ip,1);
            }
            else{
                counts.put(ip,counts.get(ip) +1);
            }
        
        }
        return counts;
        }
        
     public int mostNumberVisitsByIP(HashMap<String,Integer> map){
        int max = 0;
        String maxKey = "";
        for(String key : map.keySet()){
           int currentVal = map.get(key);
           if(currentVal > max){
               max = currentVal;
               maxKey = key;
            }
            
        }
        return max;
        }
     
    public ArrayList<String> iPsMostVisits(HashMap<String,Integer> map){
        int max = 0;
        String maxKey = "";
        ArrayList<String> mostIP = new ArrayList<String>();
        for(String key : map.keySet()){
           int currentVal = map.get(key);
           if(currentVal > max){
               max = currentVal;
               maxKey = key;
            }
            
        }
        
        for(String key : map.keySet()){
           int currentVal = map.get(key);
           if(currentVal == max){
               mostIP.add(key);
            }
            
        }
        return mostIP;
        } 
        
    public HashMap<String,ArrayList<String>> iPsForDays(){
        HashMap<String,ArrayList<String>> map = new HashMap<String,ArrayList<String>>();
        
            for (LogEntry le: records){
                String ip = le.getIpAddress();
                Date date = le.getAccessTime();
                String date2 = date.toString();
                String date3 = date2.substring(4,10);
                
                if(! map.containsKey(date3)){ //if map doesnt contain date, add it and ip
                   ArrayList<String> copy = new ArrayList<String>();
                   copy.add(ip);
                   map.put(date3, copy);
                }
                else{
                  
                       ArrayList<String> list = map.get(date3);
                       list.add(ip);
                       map.put(date3,list);
                    }
                }
        
        
        return map;
    
    }
    
    public String dayWithMostIpVisits(HashMap<String,ArrayList<String>> map){

        
            for (LogEntry le: records){
                String ip = le.getIpAddress();
                Date date = le.getAccessTime();
                String date2 = date.toString();
                
                
                if(! map.containsKey(date2)){ //if map doesnt contain date, add it and ip
                   ArrayList<String> copy = new ArrayList<String>();
                   copy.add(ip);
                   map.put(date2, copy);
                }
                else{
                   if(!map.get(date2).contains(ip)){ // if map does contain date, but not the ip
                       ArrayList<String> list = map.get(date2);
                       list.add(ip);
                       map.put(date2,list);
                    }
                }
        
            }
            int max = 0;
            String maxDay = "";
        for(String day : map.keySet()){
            
            ArrayList<String> currList = map.get(day);
            int currCount = currList.size();
            if(currCount >= max){
                max = currCount;
                maxDay = day;
            }
            
        
        }
        return maxDay;
    }
    
    public ArrayList<String> iPsWithMostVisitsOnDay(HashMap<String, ArrayList<String>> map, String date){
        
        ArrayList<String> day = map.get(date);
        HashMap<String,Integer> counts = new HashMap<String,Integer>();
        for(String ip : day){
            if(!counts.containsKey(ip)){
                counts.put(ip,1);
            
            }
            else{
                counts.put(ip,counts.get(ip)+1);
            
            }
        
        }
        int max = mostNumberVisitsByIP(counts);
        ArrayList<String> newList = new ArrayList<String>();
        for(String ip: counts.keySet()){
            if(counts.get(ip) == max){
                newList.add(ip);
            }
        
        }
        
        return newList;
    }
    
    }
        

