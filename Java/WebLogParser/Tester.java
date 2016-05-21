

import java.util.*;

public class Tester
{
    public void testLogEntry() {
        LogEntry le = new LogEntry("1.2.3.4", new Date(), "example request", 200, 500);
        System.out.println(le);
        LogEntry le2 = new LogEntry("1.2.100.4", new Date(), "example request 2", 300, 400);
        System.out.println(le2);
    }
    
    public void testLogAnalyzer() {
        LogAnalyzer test = new LogAnalyzer();
        test.readFile("short-test_log");
        test.printAll();
    }
    
    public void testUniqueIP(){
        LogAnalyzer test = new LogAnalyzer();
        test.readFile("short-test_log");
        int count = test.countUniqueIPs();
        System.out.println("There are " + count + " unique ips");
    
    
    }
    
    public void testServiceCode(){
        LogAnalyzer test = new LogAnalyzer();
        test.readFile("weblog1_log");
        test.printAllHigherThanNum(400);
    
    
    }
    
    public void testDateCode(){
        LogAnalyzer test = new LogAnalyzer();
        test.readFile("weblog1_log");
        ArrayList<String> count = test.uniqueIPVisitsOnDay("Mar 17");
        System.out.println("There are " + count.size() + " unique ips");
    
    
    }
    
    public void testIpsForDays(){
        LogAnalyzer test = new LogAnalyzer();
        test.readFile("weblog1_log");
        HashMap<String,ArrayList<String>> counts = test.iPsForDays();
        ArrayList<String> ips = test.iPsWithMostVisitsOnDay(counts,"Mar 17");
        System.out.println("There are " + ips + " unique ips");
    
    
    }
}
