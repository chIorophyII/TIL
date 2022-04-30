package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class acmHotel {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());

        for (int i=0; i < num; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int floor = Integer.parseInt(st.nextToken());
            int rooms = Integer.parseInt(st.nextToken());
            int whom = Integer.parseInt(st.nextToken());
            int answer;

            if (whom % floor != 0) {
                answer = (whom % floor) * 100 + (whom / floor) + 1;
            } else {
                answer = (floor * 100) + (whom / floor);
            }

//            int ho = (whom / floor) + 1;

            System.out.println(answer);
        }

    }
}
