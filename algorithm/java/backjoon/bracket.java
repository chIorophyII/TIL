package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

class bracket {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());

        for (int i=0; i < num; i++) {
            String bra = br.readLine();
            Stack<Character> stack = new Stack<>();

            for (int j=0; j < bra.length(); j++) {
                char c = bra.charAt(j);

                if (c == '(') {
                    stack.push(c);
                } else if (stack.empty()) {
                    stack.push(c);
                    break;
                } else {
                    stack.pop();
                }
            }

            if (stack.empty()) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }
}
