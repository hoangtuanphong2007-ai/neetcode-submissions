class Solution:
    def alnum(self, c):
        # Sửa lại logic so sánh ký tự biên chuẩn Python
        return 'a' <= c <= 'z' or '0' <= c <= '9'

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s) - 1
        
        while j > i:
            # Dùng while để nhảy qua TẤT CẢ khoảng trắng/dấu câu liên tiếp
            while j > i and (s[i] == " " or not self.alnum(s[i])):
                i += 1
            while j > i and (s[j] == " " or not self.alnum(s[j])):
                j -= 1
                
            if s[i] != s[j]:
                return False
                
            i += 1
            j -= 1
            
        return True