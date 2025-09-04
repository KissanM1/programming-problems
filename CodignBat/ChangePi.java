/*
===============================
Recursion-1 > changePi
===============================

Given a string, compute recursively (no loops) a new string where all appearances of "pi" have been replaced
by "3.14".


changePi("xpix") → "x3.14x"
changePi("pipi") → "3.143.14"
changePi("pip") → "3.14p"
*/

public class ChangePi {
    public String changePi(String str) {
        if (str.length() < 2){
            return str;
        } 
        int strLength = str.length();
        String check = str.substring(strLength - 2);
        String endingString = check.equals("pi") ? "3.14" : "" + str.charAt(strLength - 1);
        int indexEnd = check.equals("pi") ? strLength - 2 : strLength - 1; 

        return changePi(str.substring(0, indexEnd)) + endingString;
    }
}
