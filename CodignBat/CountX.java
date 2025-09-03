/*
===============================
Recursion-1 > countX
===============================

Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string.

countX("xxhixx") → 4
countX("xhixhix") → 3
countX("hi") → 0
*/

public class CountX {
    public int countX(String str) {
        if (str.equals("")){
            return 0;
        }
        int nextVal = countX(str.substring(1));
        return str.charAt(0) == 'x' ? 1 + nextVal : nextVal;
    }

}
