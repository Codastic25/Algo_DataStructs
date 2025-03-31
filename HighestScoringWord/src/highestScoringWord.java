public class highestScoringWord {
    public static String high(String s) {
        // Your code here...
        int maximum = 0;
        String bestWord = "";

        String[] allWords = s.split(" "); // tous les mots sont coupés
        for (String mot : allWords) {
            System.out.println(mot);
            int score = 0;
            for (int i = 0; i<mot.length(); i++){
                score += mot.charAt(i) - 'a' + 1; // 'a' = 1, 'b' = 2, ..., 'z' = 26
            }
            if (score > maximum){
                maximum = score;
                bestWord = mot;
            }


        }

        return bestWord;
    }
}
