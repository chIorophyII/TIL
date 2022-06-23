package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class divisor {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int num = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine()," ");

        int max = 0;
        int min = 1000000;

        for (int i=0; i < num; i++) {
            int N = Integer.parseInt(st.nextToken());
            min = Math.min(N, min);
            max = Math.max(N, max);
        }
        System.out.println(max * min);

    }
}
