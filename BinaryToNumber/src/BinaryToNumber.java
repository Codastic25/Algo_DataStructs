import java.util.List;
import java.lang.Math;

public class BinaryToNumber {
    public static int ConvertBinaryArrayToInt(List<Integer> binary) {
        // Your Code
        int n = binary.size();
        int sum = 0;

        for (int i = 0;i < n; i++){

            sum += binary.get(i) * (int) Math.pow(2, n - 1 - i);
        }
        return sum;
    }
}
