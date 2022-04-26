package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class bertrangGongjun {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // {1, 10, 13, 100, 1000, 10000, 100000, 0}

        while (true) {
            int s = Integer.parseInt(br.readLine());
            int end = s*2;
            int cnt = 0;
            if(s==0) break;

            boolean[] arr = new boolean[end + 1];
            arr[0] = arr[1] = false;

            // {false, false, true, true, true, ..., true}
            for (int j = 2; j < end+1; j++) {
                arr[j] = true;
            }

            // {false, false, true, true, false, true, false, true, ...}
            for (int j = 2; j*j < end+1; j++) {
                if(arr[j]) {
                    for (int p = j*j; p <= end; p += j) {
                        arr[p] = false;
                    }
                }

            }

            for (int h=s+1; h < end+1; h++) {
                if (arr[h]) {
                    cnt ++;
                }
            }
            System.out.println(cnt);


        }
    }
}
