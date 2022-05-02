package programmers;

import java.util.ArrayList;
import java.util.Collections;

class 방금그곡 {
    public String solution(String m, String[] musicinfos) {
        String answer = "";
        ArrayList<Boolean> list = new ArrayList<Boolean>();

        // 음악 제목 일치 여부
        for (int i = 0; i < musicinfos.length; i++) {
            String melody = musicinfos[i].split(",")[3];
            String melodies = melody;

            while (melody.length() < m.length()) {
                melodies = melodies.concat(melody);
            }

            if (melodies.contains(m)) {
                list.add(true);
            } else {
                list.add(false);
            }
        }

        if (Collections.frequency(list, true) == 1) {
            answer = musicinfos[list.indexOf(true)].split(",")[2];
        }

        return answer;
    }
}
