class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false;
    
        const sChar = {};
        const tChar = {};
    
        // Count characters in both strings
        for (let i = 0; i < s.length; i++) {
            // Count in s
            const sCharAt = s[i];
            sChar[sCharAt] = (sChar[sCharAt] || 0) + 1;
            
            // Count in t
            const tCharAt = t[i];
            tChar[tCharAt] = (tChar[tCharAt] || 0) + 1;
        }
        
        // Compare objects by checking keys and values
        for (let key in sChar) {
            if (sChar[key] !== tChar[key]) return false;
        }
        
        return true;
    }
}
