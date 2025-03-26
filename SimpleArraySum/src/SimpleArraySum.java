import java.util.List;

public class SimpleArraySum {
    /*
     * Complete the 'simpleArraySum' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts INTEGER_ARRAY ar as parameter.
     */

    public static int simpleArraySum(List<Integer> ar) {
        // Write your code here
        int res = 0;
        for(int i = 0; i<ar.size(); i++){
            res = res + ar.get(i);
        }
        return res;
    }
}
