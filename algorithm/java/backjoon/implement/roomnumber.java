package backjoon.implement;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

class roomnumber {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String room = br.readLine();
        double[] cnt = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

        for (int i=0; i < room.length(); i++) {
            int num = room.charAt(i) - '0';
            if (num == 6 || num == 9) {
                cnt[6] += 0.5;
            } else {
                cnt[num] += 1;
            }
        }
        cnt[6] = (int) Math.ceil(cnt[6]);
        Arrays.sort(cnt);
        int answer = (int) cnt[cnt.length-1];
        System.out.println(answer);

    }
}
