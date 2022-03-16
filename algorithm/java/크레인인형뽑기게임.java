import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        ArrayList<Integer> bucket = new ArrayList<>();
        
        for (int i : moves) {
            for (int j=0; j < board.length; j++) {
                if (board[j][i-1] != 0) {
                    bucket.add(board[j][i-1]);
                    board[j][i-1] = 0;
                    break;
                }
            }
            if (bucket.size() >= 2 && (bucket.get(bucket.size()-1) == bucket.get(bucket.size()-2))) {
                    bucket.remove(bucket.size()-1);
                    bucket.remove(bucket.size()-1);
                    answer += 2;
            }
        }
        
        return answer;
    }
}