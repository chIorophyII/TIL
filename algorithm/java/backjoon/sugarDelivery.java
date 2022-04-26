package backjoon;

import java.util.Scanner;

class sugarDelivery {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int answer = 0;

        for (int i=0; i < N / 3; i++) {
            if ((N-(3*i)) % 5 == 0) {
                answer = ((N-(3*i)) / 5) + i;
                break;
            } else if (N % 3 == 0){
                answer = N / 3;
            } else {
                answer = -1;
            }
        }
        System.out.println(answer);;
    }
}

