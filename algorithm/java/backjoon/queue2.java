//package backjoon;
//
//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;
//import java.util.LinkedList;
//import java.util.Queue;
//import java.util.StringTokenizer;
//
//class queue2 {
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        int num = Integer.parseInt(br.readLine());
//        Queue<Integer> queue = new LinkedList<>();
//
//        int last = 0;
//        int answer = 0 ;
//        for (int i=0; i < num; i++) {
//            StringTokenizer st = new StringTokenizer(br.readLine());
//            String order = st.nextToken();
//
//            switch (order) {
//                case "push" :
//                    last = Integer.parseInt(st.nextToken());
//                    queue.add(last);
//                    break;
//                case "pop" :
//                    if (queue.isEmpty()) {
//                        answer = -1;
//                        break;
//                    }
//                    answer = queue.poll();
//                    break;
//                case "size" :
//                    answer = queue.size();
//                    break;
//                case "empty" :
//                    answer = queue.isEmpty()? 1: 0;
//                    break;
//                case "front" :
//                    answer = queue.isEmpty()? -1: queue.peek();
//                    break;
//                case "back" :
//                    answer = queue.isEmpty()? -1: last;
//                    break;
//            }
//            System.out.println(answer);
//        }
//    }
//}
