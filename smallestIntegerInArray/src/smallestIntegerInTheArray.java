public class smallestIntegerInTheArray {
    public static int findSmallestInt(int[] args) {
        int minValue = args[0];
        for (int i = 0; i < args.length; i++){
            if (args[i] < minValue){
                minValue = args[i];
            }
        }
        return minValue;
    }
}
