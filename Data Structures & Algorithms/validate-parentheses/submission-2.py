class Solution:

    def isValid(self, s: str) -> bool:

        if len(s) == 0:
            return True
        elif len(s) == 1:
            return False
        else:
            x = s[0]
            y = s[-1]
            z = s[1]
            if [x,y] == ['(',')'] or [x,y] == ['{','}'] or [x,y] == ['[',']']:
                return self.isValid(s[1:-1])
            elif [x,z] == ['(',')'] or [x,z] == ['{','}'] or [x,z] == ['[',']']:
                return self.isValid(s[2:])
            else:
                return False

            

        

        
        
        