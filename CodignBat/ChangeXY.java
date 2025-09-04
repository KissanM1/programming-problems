/*
===============================
Recursion-1 > changeXY
===============================

Given a string, compute recursively (no loops) a new string where all the lowercase 'x' chars have been changed 
to 'y' chars.

changeXY("codex") → "codey"
changeXY("xxhixx") → "yyhiyy"
changeXY("xhixhix") → "yhiyhiy"
*/

public class ChangeXY {
    public String changeXY(String str) {
        if (str.equals("")) {
            return "";
        }
        char lastCharInput = str.charAt(str.length() - 1);
        char lastCharOutput = lastCharInput == 'x' ? 'y': lastCharInput;
        int lastCharIndex = str.length() - 1;
        return changeXY(str.substring(0, lastCharIndex)) + lastCharOutput;
    }
}
