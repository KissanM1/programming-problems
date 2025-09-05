/*
===============================
Recursion-1 > countAbc
===============================

Count recursively the total number of "abc" and "aba" substrings that appear in the given string.

countAbc("abc") → 1
countAbc("abcxxabc") → 2
countAbc("abaxxaba") → 2
*/


public class CountAbc {
    public int countAbc(String str) {
        if (str.length() < 3){
            return 0;
        }
        String strCheck = str.substring(0, 3);
        int nextSection =  countAbc(str.substring(1));
        return strCheck.equals("aba") || strCheck.equals("abc") ? nextSection + 1 : nextSection;
    }
}
