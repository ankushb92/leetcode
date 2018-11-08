class Solution:
    #KMP
    def findFirstMatch(self, A, B):
        P = [0]*len(A)
        j = 0
        i = 1
        while i < len(P):
            if A[j] == A[i]:
                P[i] = j + 1
                i += 1
                j += 1
            else:
                if j==0:
                    i += 1
                else:
                    j = P[j-1]

        i = 0
        j = 0
        while j<len(A) and i<len(B):
            if B[i]==A[j]:
                i += 1
                j += 1
            else:
                if j==0:
                    i += 1
                else:
                    j = P[j-1]

        if j==len(A):
            return i - j
        else:
            return -1

    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if len(A) > len(B):
            if self.findFirstMatch(B, A) == -1:
                if self.findFirstMatch(B, A+A) != -1:
                    return 2
                else:
                    return -1
            else:
                return 1

        match_ind = self.findFirstMatch(A, B)

        if match_ind==-1:
            if self.findFirstMatch(B, A+A) != -1:
                return 2
            else:
                return -1
        
        if match_ind>0:
            if B[:match_ind] != A[-match_ind:]:
                return -1 
            cnt = 1
        else:
            cnt = 0
        
        while B[match_ind:match_ind+len(A)]==A:
            cnt += 1
            match_ind += len(A)

        if match_ind < len(B):
            cnt += 1

        if B[match_ind:] != A[:len(B)-match_ind]:
            return -1

        return cnt