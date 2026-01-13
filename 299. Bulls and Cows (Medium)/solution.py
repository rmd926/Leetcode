class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        count_A = 0
        count_B = 0
        
        lookup_B = {}

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                count_A += 1
            else:
                if secret[i] in lookup_B:
                    lookup_B[secret[i]] += 1
                else:
                    lookup_B[secret[i]] = 1
            

        for j in range(len(guess)):
            if guess[j] != secret[j]:
                if guess[j] in lookup_B and lookup_B[guess[j]] > 0:
                    count_B += 1
                    lookup_B[guess[j]] -= 1
        
        return f"{count_A}A{count_B}B"
