package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class snailGoup {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int up = Integer.parseInt(st.nextToken());
        int down = Integer.parseInt(st.nextToken());
        int total = Integer.parseInt(st.nextToken());

        int day = (total - down) / (up - down);

        if ((total - down) % (up - down) != 0) {
            day ++;
        }

        System.out.println(day);

    }
}
