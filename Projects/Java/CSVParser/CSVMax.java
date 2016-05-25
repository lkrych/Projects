/**
 * Find the highest (hottest) temperature in any number of files of CSV weather data chosen by the user.
 * 
 * @author Duke Software Team 
 */
import edu.duke.*;
import org.apache.commons.csv.*;
import java.io.*;

public class CSVMax {
    public CSVRecord hottestHourInFile(CSVParser parser) {
        //start with largestSoFar as nothing
        CSVRecord largestSoFar = null;
        //For each row (currentRow) in the CSV File
        for (CSVRecord currentRow : parser) {
            // use method to compare two records
            largestSoFar = getLargestOfTwo(currentRow, largestSoFar);
        }
        //The largestSoFar is the answer
        return largestSoFar;
    }

    public void testHottestInDay () {
        FileResource fr = new FileResource("data/2015/weather-2015-01-01.csv");
        CSVRecord largest = hottestHourInFile(fr.getCSVParser());
        System.out.println("hottest temperature was " + largest.get("TemperatureF") +
                   " at " + largest.get("TimeEST"));
    }

    public CSVRecord hottestInManyDays() {
        CSVRecord largestSoFar = null;
        DirectoryResource dr = new DirectoryResource();
        // iterate over files
        for (File f : dr.selectedFiles()) {
            FileResource fr = new FileResource(f);
            // use method to get largest in file.
            CSVRecord currentRow = hottestHourInFile(fr.getCSVParser());
            // use method to compare two records
            largestSoFar = getLargestOfTwo(currentRow, largestSoFar);
        }
        //The largestSoFar is the answer
        return largestSoFar;
    }

    public CSVRecord getLargestOfTwo (CSVRecord currentRow, CSVRecord largestSoFar) {
        //If largestSoFar is nothing
        if (largestSoFar == null) {
            largestSoFar = currentRow;
        }
        //Otherwise
        else {
            double currentTemp = Double.parseDouble(currentRow.get("TemperatureF"));
            double largestTemp = Double.parseDouble(largestSoFar.get("TemperatureF"));
            //Check if currentRow’s temperature > largestSoFar’s
            if (currentTemp > largestTemp) {
                //If so update largestSoFar to currentRow
                largestSoFar = currentRow;
            }
        }
        return largestSoFar;
    }

    public void testHottestInManyDays () {
        CSVRecord largest = hottestInManyDays();
        System.out.println("hottest temperature was " + largest.get("TemperatureF") +
                   " at " + largest.get("DateUTC"));
    }
    
    public CSVRecord coldestHourInFile(CSVParser parser) {
        //start with largestSoFar as nothing
        CSVRecord smallestSoFar = null;
        //For each row (currentRow) in the CSV File
        for (CSVRecord currentRow : parser) {
            // use method to compare two records
            smallestSoFar = getSmallestOfTwo(currentRow, smallestSoFar);
        }
        //The largestSoFar is the answer
        return smallestSoFar;
    }
    
    public CSVRecord getSmallestOfTwo (CSVRecord currentRow, CSVRecord smallestSoFar) {
        //If smallestSoFar is nothing
        if (smallestSoFar == null) {
            smallestSoFar = currentRow;
        }
        //Otherwise
        else {
            double currentTemp = Double.parseDouble(currentRow.get("TemperatureF"));
            double smallestTemp = Double.parseDouble(smallestSoFar.get("TemperatureF"));
            //Check if currentRow’s temperature > smallestSoFar’s
            if (currentTemp < smallestTemp && currentTemp != -9999) {
                //If so update smallestSoFar to currentRow
                smallestSoFar = currentRow;
            }
        }
        return smallestSoFar;
    }
    
    public void testColdestHourInFile () {
        FileResource fr = new FileResource();
        CSVParser parser = fr.getCSVParser();
        CSVRecord smallest = coldestHourInFile(fr.getCSVParser());
        System.out.println("coldest temperature was " + smallest.get("TemperatureF") +" at " + smallest.get("DateUTC"));
    }
    
    //returns whether or not the the filepath was changed
    public boolean getSmallestOfTwoFile (CSVRecord currentRow, CSVRecord smallestSoFar) {
        boolean changed = false;
        if (smallestSoFar == null) {
            smallestSoFar = currentRow;
        }
        //Otherwise
        else {
            double currentTemp = Double.parseDouble(currentRow.get("TemperatureF"));
            double smallestTemp = Double.parseDouble(smallestSoFar.get("TemperatureF"));
            //Check if currentRow’s temperature > smallestSoFar’s
            if (currentTemp < smallestTemp && currentTemp != -9999) {
                //If so update smallestSoFar to currentRow
                changed = true;
            }
        }
        return changed;
    }
    //returns string of filename with coldest temp, uses a similar method to getSmallestOfTwo, but this method
    //indicates whether or not the file has been updated, if so it saves the name of the new file
    public String fileWithColdestTemperature() {
        CSVRecord smallestSoFar = null;
        DirectoryResource dr = new DirectoryResource();
        String fname = "";
        // iterate over files
        for (File f : dr.selectedFiles()) {
            FileResource fr = new FileResource(f);
            // use method to get smallest in file.
            CSVRecord currentRow = coldestHourInFile(fr.getCSVParser());
            // use method to compare two records
            boolean boolSmallestSoFar = getSmallestOfTwoFile(currentRow,smallestSoFar);
            smallestSoFar = getSmallestOfTwo(currentRow, smallestSoFar);
            
            if(boolSmallestSoFar == true || smallestSoFar == currentRow){
                fname = f.getName();
            }
            }
         
        return fname;
    }
    
    
    public void testFileWithColdestTemperature() {
        String coldest = fileWithColdestTemperature();
        
        System.out.println("Coldest temperature was in file " + coldest);
        
        
     }
     
    public CSVRecord getSmallestHumidityTwo (CSVRecord currentRow, CSVRecord smallestSoFar) {
        double currentHum = 0.0;
        if (smallestSoFar == null) {
            smallestSoFar = currentRow;
        }else{
            
            if( currentRow.get("Humidity") == "N/A" ){
                 currentHum = Double.parseDouble(smallestSoFar.get("Humidity"));
            }else{
                 currentHum = Double.parseDouble(currentRow.get("Humidity"));
            }
            
            double smallestHum = Double.parseDouble(smallestSoFar.get("Humidity"));
            //Check if currentRow’s temperature > smallestSoFar’s
            if (currentHum < smallestHum) {
                //If so update smallestSoFar to currentRow
                smallestSoFar = currentRow;
            }
        }
        return smallestSoFar;
    }
     
   public CSVRecord lowestHumidityInFile(CSVParser parser) {
        //start with largestSoFar as nothing
        CSVRecord smallestSoFar = null;
        //For each row (currentRow) in the CSV File
        for (CSVRecord currentRow : parser) {
            // use method to compare two records
            smallestSoFar = getSmallestHumidityTwo(currentRow, smallestSoFar);
        }
        //The largestSoFar is the answer
        return smallestSoFar;
    } 
    
    public void testLowestHumidityInFile () {
        FileResource fr = new FileResource();
        CSVParser parser = fr.getCSVParser();
        CSVRecord smallest = lowestHumidityInFile(fr.getCSVParser());
        System.out.println("lowest humidity was " + smallest.get("Humidity") +
                   " at " + smallest.get("DateUTC"));
    }
    
    public CSVRecord lowestHumidityInManyFiles() {
        CSVRecord smallestSoFar = null;
        DirectoryResource dr = new DirectoryResource();
        // iterate over files
        for (File f : dr.selectedFiles()) {
            FileResource fr = new FileResource(f);
            // use method to get largest in file.
            CSVRecord currentRow = lowestHumidityInFile(fr.getCSVParser());
            // use method to compare two records
            smallestSoFar = getSmallestOfTwo(currentRow, smallestSoFar);
        }
        //The largestSoFar is the answer
        return smallestSoFar;
    }
    
     public void testLowestHumidityInManyDays () {
        CSVRecord largest = lowestHumidityInManyFiles();
        System.out.println("Lowest Humidity was " + largest.get("Humidity") +
                   " at " + largest.get("DateUTC"));
    }
    
   public double averageTemperatureInFile(CSVParser parser) {
        //start with largestSoFar as nothing
        double sum = 0;
        double count = 0;
        //For each row (currentRow) in the CSV File
        for (CSVRecord currentRow : parser) {
            // use method to compare two records
            double current = Double.parseDouble(currentRow.get("TemperatureF"));
            sum = sum + current;
            count = count + 1;
        }
        //The largestSoFar is the answer
        return sum/count;
    }
    
   public void testAverageTemperatureInFile() {
        FileResource fr = new FileResource();
        CSVParser parser = fr.getCSVParser();
        double average = averageTemperatureInFile(fr.getCSVParser());
        System.out.println("Average temperature in file is " + average);
    }
    
   public double averageTemperatureWithHighHumidityInFile(CSVParser parser, int value) {
        //start with largestSoFar as nothing
        double sum = 0;
        double count = 0;
        //For each row (currentRow) in the CSV File
        for (CSVRecord currentRow : parser) {
            // use method to compare two records
            if(Double.parseDouble(currentRow.get("Humidity")) >= value ){
                double current = Double.parseDouble(currentRow.get("TemperatureF"));
            sum = sum + current;
            count = count + 1;
           }
        }
        return sum/count;
    }

    
   public void testAverageTemperatureWithHighHumidityInFile() {
        FileResource fr = new FileResource();
        CSVParser parser = fr.getCSVParser();
        double average = averageTemperatureWithHighHumidityInFile(fr.getCSVParser(),80);
         if(average > 0 ){
            System.out.println("Average temperature in file is " + average);
        }else{
            System.out.println("No temperatures with that humidity");
        };
        
    }
   }
