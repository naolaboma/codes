# Problem: Remove Letter To Equalize Frequency - https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = Counter(word)
        freq_values = list(freq.values())
        for i in range(len(freq_values)):
            modified_freq = freq_values[:]
            modified_freq[i] -= 1
            modified_freq = [f for f in modified_freq if f > 0]
            if len(set(modified_freq)) == 1:
                return True
        return False