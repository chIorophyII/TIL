package programmers;

import java.util.*;

class 완주하지못한선수 {
    public String solution(String[] participant, String[] completion) {
        String answer = "";

        Arrays.sort(participant);
        Arrays.sort(completion);

        for (int i=0; i < completion.length; i++) {
            if (!participant[i].equals(completion[i])) {
                answer = participant[i];
                return answer;
            }
        }
        answer = participant[participant.length-1];
        return answer;
    }
}

class 완주하지못한선수_Hash {
    public String solution(String[] participant, String[] completion) {
        String answer = "";

        // 배열을 해시맵으로 변환 ["mislav", "stanko", "mislav", "ana"] -> {ana=1, mislav=2, stanko=1}
        HashMap<String, Integer> hashMap = new HashMap<>();

        // hashMap.getOrDefault -> hashMap에 해당하는 값이 없으면 default 값 반환
        for (String p : participant) hashMap.put(p, hashMap.getOrDefault(p, 0) + 1);
        // {ana=1, mislav=2, stanko=1}
        for (String c : completion) hashMap.put(c, hashMap.get(c) - 1);
        // {ana=0, mislav=1, stanko=0}

        for (String rest : hashMap.keySet()) {
            if (hashMap.get(rest) != 0) {
                answer = rest;
                break;
            }
        }
        return answer;
    }
}