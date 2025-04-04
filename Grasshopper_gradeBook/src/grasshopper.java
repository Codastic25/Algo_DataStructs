public class grasshopper {
    public static char getGrade(int s1, int s2, int s3) {
        //int final_grade = s1+s2+s3;
        double average_final_grade = (s1+s2+s3)/3;

        if (average_final_grade <= 100 && average_final_grade >= 90){
            return 'A';
        }
        else if (average_final_grade < 90 && average_final_grade >= 80){
            return 'B';
        }
        else if (average_final_grade < 80 && average_final_grade >= 70){
            return 'C';
        }
        else if (average_final_grade < 70 && average_final_grade >= 60){
            return 'D';
        }
        else{
            return 'F';
        }
    }

    public static void main (String[] args){
        getGrade(70, 80, 50);
    }
}
