class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int m = s1.size(), n = s2.size(), k = s3.size();
        if (m + n != k) return false;
            while(m > 0 && n > 0 && s1[m-1] == s2[n-1] && s1[m-1] == s3[k-1]) {
                m--;
                n--;
                k--;
            }
            while(m > 0 && s1[m-1] == s3[k-1]) {
                m--;
                k--;
            }
            while(n > 0 && s2[n-1] == s3[k-1]) {
                n--;
                k--;
            }
            if (m == 0 && n == 0) return true;
            if (m == 0) return s2.substr(0, n) == s3.substr(0, n);
            if (n == 0) return s1.substr(0, m) == s3.substr(0, m);
            return s1.substr(0, m) == s3.substr(0, m) && s2.substr(0, n) == s3.substr(m, n);     
    }
};
