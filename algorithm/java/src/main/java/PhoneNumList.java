import java.util.*;

class PhoneNumList {
    public boolean solution(String[] phoneBook) {
        Arrays.sort(phoneBook);

        for (int i=0; i < phoneBook.length-1; i++){
            if (phoneBook[i+1].startsWith(phoneBook[i])){
                return false;
            }
        }
        return true;
    }
}

// 해시를 이용한 방법
class PhoneNumHash {
    public boolean solution(String[] phone_book) {
        HashMap<String, String> hm = new HashMap<>();

        // 중복을 제거해서 해시 맵에 저장
        for (String p : phone_book) {
            hm.put(p, p);
        }
        for (String target : phone_book) {
            for (int i=0; i < target.length(); i++) {
                if (hm.get(target.substring(0,i)) != null) {
                    return false;
                }
            }
        }
        return true;
    }
}