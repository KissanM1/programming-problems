/*
===============================
Recursion-1 > noX
===============================

Given a string, compute recursively a new string where all the 'x' chars have been removed.

noX("xaxb") → "ab"
noX("abc") → "abc"
noX("xx") → ""
*/

public class NoX {
    public String noX(String str) {
        if (str.equals("")) {
            return "";
        }
        char firstChar = str.charAt(0);
        String ending = noX(str.substring(1));
        return firstChar == 'x' ? ending : firstChar + ending;
    }
}
