public class dnaToRna {
    public String dnaToRna(String dna) {
        // if there is a U in the dna String, replace it with T
        String ans = "";
        for (char elem : dna.toCharArray()){
            if (elem == 'T'){
                ans = ans + 'U';


            }
            else {
                ans = ans + elem;
            }
        }
        dna = ans;

        return dna;  // Do your magic!
    }
}
