package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

class balancedworld {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        while (true) {
            String answer = "yes";
            String sentence = br.readLine();
            Stack<Character> stack = new Stack<>();
            if (sentence.equals(".")) break;

            for (int j=0; j < sentence.length(); j++) {
                char c = sentence.charAt(j);

                if (c == '.') {
                    break;
                }
                if (c == '(' || c == '[') {
                    stack.push(c);
                }
                if (c == ')') {
                    if (stack.empty()) {
                        answer = "no";
                        stack.push(')');
                        break;
                    } else if (stack.peek() == '('){
                        stack.pop();
                    } else {
                        answer = "no";
                    }
                }
                if (c == ']'){
                    if (stack.empty()) {
                        answer = "no";
                        stack.push(']');
                        break;
                    } else if (stack.peek() == '['){
                        stack.pop();
                    } else {
                        answer = "no";
                    }
                }

            }
            if (!stack.empty()) {
                answer = "no";
            }
            System.out.println(answer);

        }
    }
}
