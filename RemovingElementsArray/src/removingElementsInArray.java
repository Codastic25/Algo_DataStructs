import java.util.ArrayList;

public class removingElementsInArray {
    public static Object[] removeEveryOther(Object[] arr) {
        // happy coding
        // Créer une ArrayList pour stocker les éléments à conserver
        ArrayList<Object> resultList = new ArrayList<>();

        // Parcourir le tableau d'origine et ajouter les éléments aux indices pairs
        for (int i = 0; i < arr.length; i++) {
            if (i % 2 == 0) {  // Garde les éléments aux indices pairs
                resultList.add(arr[i]);
            }
        }

        // Convertir l'ArrayList en tableau et le retourner
        return resultList.toArray(new Object[resultList.size()]);
    }
}
