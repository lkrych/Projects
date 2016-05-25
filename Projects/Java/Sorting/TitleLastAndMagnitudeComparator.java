
import java.util.*;
import edu.duke.*;
public class TitleLastAndMagnitudeComparator implements Comparator<QuakeEntry> {
    
     public TitleLastAndMagnitudeComparator(){
    
    }
    
    public int compare(QuakeEntry qe1, QuakeEntry qe2){
        String title1 = qe1.getInfo();
        String lastWord1 = title1.substring(title1.lastIndexOf(" ")+1);
        String title2 = qe2.getInfo();
        String lastWord2 = title2.substring(title2.lastIndexOf(" ")+1);
        if(lastWord1.compareTo(lastWord2) == 0){
            return Double.compare(qe1.getMagnitude(),qe2.getMagnitude());
        }
        if(lastWord1.compareTo(lastWord2) > 0 ){
            return 1;
        }
        if(lastWord1.compareTo(lastWord2) < 0 ){
            return -1;
        }
        return 0;
    }

}
