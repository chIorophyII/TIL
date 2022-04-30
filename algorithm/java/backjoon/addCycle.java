package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class addCycle {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());
        int add = num;
        int cnt = 0;

        while (true) {
            add = ((add%10)*10) + ((add/10)+(add%10))%10;
            cnt++;
            if (add == num) break;
        }
        System.out.println(cnt);
    }
}
