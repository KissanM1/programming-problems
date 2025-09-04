/*
===============================
Recursion-1 > countHi
===============================

Given a string, compute recursively (no loops) the number of times lowercase "hi" appears in the string.

countHi("xxhixx") → 1
countHi("xhixhix") → 2
countHi("hi") → 1
*/

public class CountHi {
    public int countHi(String str) {
        if (str.length() <= 1) {
            return 0;
        }
        String check = str.substring(0,2);
        if (check.equals("hi")) {
            return 1 + countHi(str.substring(2));
        }
        return countHi(str.substring(1));
    }
}
