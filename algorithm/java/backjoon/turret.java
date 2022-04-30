package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class turret {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());

        for (int i=0; i < num; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int r1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());
            int r2 = Integer.parseInt(st.nextToken());
            double length = Math.sqrt(Math.pow(x2-x1, 2) + Math.pow(y2-y1, 2));

            if (length == 0 && r1 == r2) {
                System.out.println(-1); // 두 원이 같다.
            } else if (length > (r1+r2) || length < Math.abs(r2-r1)) {
                System.out.println(0);; // 만나지 않는다(외부, 내부)
            } else if (length == (r1+r2) || length == Math.abs(r2-r1)) {
                System.out.println(1);; // 한 점에서 만날때 (외접, 내접)
            } else {
                System.out.println(2);; // 두 점에서 만난다
            }
        }
    }
}
