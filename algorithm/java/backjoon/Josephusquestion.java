package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Josephusquestion {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        Queue queue = new LinkedList<>();

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        for (int i=0; i < n; i++) {
            queue.add(i+1);
        }

        sb.append("<");
        while(true) {
            for (int i=0; i<k-1; i++) {
                queue.add(queue.poll());
            }
            sb.append(queue.poll());
            if (queue.size() == 0) {
                break;
            }
            sb.append(", ");
        }
        sb.append(">");

        System.out.println(sb);
    }
}
