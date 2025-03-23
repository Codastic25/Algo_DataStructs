public class collatzConjecture {
    public static int hotpo(int n) {
        // TODO: Implement the function
        int cpt = 0;

        while (cpt > -1){
            if (n == 1){
                return cpt;
            }
            else if (n % 2 == 0){ //pair
                n = n/2;
                cpt++;
            }
            else {
                n = 3*n+1;
                cpt++;
            }
        }
        return cpt;
    }
}
