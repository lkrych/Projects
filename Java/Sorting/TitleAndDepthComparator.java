
import java.util.*;
import edu.duke.*;
public class TitleAndDepthComparator implements Comparator<QuakeEntry> {
    
    public TitleAndDepthComparator(){
    
    }
    
    public int compare(QuakeEntry qe1, QuakeEntry qe2){
        String title1 = qe1.getInfo();
        String title2 = qe2.getInfo();
        if(title1.compareTo(title2) == 0){
            return Double.compare(qe1.getDepth(),qe2.getDepth());
        }
        if(title1.compareTo(title2) > 0 ){
            return 1;
        }
        if(title1.compareTo(title2) < 0 ){
            return -1;
        }
        return 0;
    }

}
