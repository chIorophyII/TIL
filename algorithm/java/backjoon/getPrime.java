package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class getPrime {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int mini = Integer.parseInt(st.nextToken());
        int maxi = Integer.parseInt(st.nextToken());

        boolean[] arr = new boolean[maxi + 1];
        arr[0] = arr[1] = false;

        // {false, false, true, true, true, ..., true}
        for (int j = 2; j < maxi+1; j++) {
            arr[j] = true;
        }

        // {false, false, true, true, false, true, false, true, ...}
        for (int j = 2; j*j < maxi+1; j++) {
            if(arr[j]) {
                for (int p = j*j; p <= maxi; p += j) {
                    arr[p] = false;
                }
            }

        }

        for (int h=mini; h < maxi+1; h++) {
            if (arr[h]) {
                System.out.println(h);
            }
        }


    }
}
