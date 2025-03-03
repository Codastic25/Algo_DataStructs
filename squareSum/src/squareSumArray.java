public class squareSumArray {
    public static int squareSum(int[] n)
    {
        int cpt = 0;
        for (int elem = 0; elem < n.length; elem++) {
            n[elem]*=n[elem];
            cpt = cpt+n[elem];
        }
        return cpt;
    }
}
