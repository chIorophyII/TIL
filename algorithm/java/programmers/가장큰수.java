package programmers;

import java.util.ArrayList;
import java.util.Arrays;

public class 가장큰수 {
    public static void main(String[] args) {
        System.out.println(solution(new int[] {6, 10, 2}));
    }

    public static String solution(int[] numbers) {
        String answer = "";
        Arrays.sort(numbers); // {2, 6, 10}
        for (int i : numbers) {
            System.out.println(i);
        }
//        System.out.println(Arrays.toString(numbers));

//        ArrayList<String> nums = new ArrayList<>();
        return answer;
    }
}
