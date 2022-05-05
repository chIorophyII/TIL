package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

class minheap {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();
        int num = Integer.parseInt(br.readLine());

        for (int i=0; i < num; i++) {
            int heap = Integer.parseInt(br.readLine());

            if (heap == 0) {
                if (priorityQueue.isEmpty()) {
                    System.out.println(0);
                } else {
                    System.out.println(priorityQueue.poll());
                }
            } else {
                priorityQueue.add(heap);
            }

        }
    }
}
