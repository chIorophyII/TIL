package backjoon.greedy;

import java.io.*;
import java.util.*;

class coin0 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int num = Integer.parseInt(st.nextToken());
        int money = Integer.parseInt(st.nextToken());
        int cnt = 0;
        Integer[] moneys = new Integer[num];

        for (int i=0; i < num; i++) {
            int N = Integer.parseInt(br.readLine());
            moneys[i] = N;
        }

        Arrays.sort(moneys, Collections.reverseOrder());
        for (int m : moneys) {
            if (money >= m) {
                cnt += money / m;
                money -= (money / m) * m;
            }
        }
        System.out.println(cnt);
    }
}
