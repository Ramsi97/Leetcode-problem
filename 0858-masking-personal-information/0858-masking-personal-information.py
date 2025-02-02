class Solution(object):
    def maskPII(self, s):
        """
        :type s: str
        :rtype: str
        """
        if '@' in s:
            at = s.find('@')
            dot = s.find('.')
            return s[0].lower() + '*'*5 + s[at-1].lower()+ '@' + s[at+1:dot].lower() +'.'+s[dot+1:].lower()
        else:
            phone = ''
            for char in s:
                if char.isdigit():
                    phone+=char
            if len(phone) == 10:
                return "***-***-"+phone[-4:]
            elif len(phone) == 11:
                return "+*-***-***-"+phone[-4:]
            elif len(phone) == 12:
                return "+**-***-***-"+phone[-4:]
            else:
                return "+***-***-***-"+phone[-4:]
            


        