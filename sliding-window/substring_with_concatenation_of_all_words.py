class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_freq = {}

        for word in words:
            if word not in word_freq:
                word_freq[word] = 0
            word_freq[word] += 1

        result = []
        len_word = len(words[0])
        len_words = len(words)
        len_substr = len_word * len_words

        for i in range((len(s) - len_substr) + 1):
            words_seen = {}
            for j in range(0, len_words):
                # Gives us the index of the current next word
                next_word_index = i + j * len_word

                # Get the next word from the string
                word = s[next_word_index:next_word_index + len_word]

                # Since it's not in the list of words we're looking for
                # head on to the next set of words
                if word not in word_freq:
                    break;

                # Since words are in word_freq, record it in words_seen
                if word not in words_seen:
                    words_seen[word] = 0
                words_seen[word] += 1

                # If the frequencies don't match then while the word
                # may be in the string but the concatenated substring
                # is not
                if words_seen[word] > word_freq[word]:
                    break;

                # If we hit j + 1 == len_words, that means we found
                # the substring w/ concatenation of all words
                if j + 1 == len_words:
                    result.append(i)

        return result

# Time Complexity: The time complexity of the above algorithm will be
# O(N * M * Len) where ‘N’ is the number of characters in
# the given string, ‘M’ is the total number of words, and ‘Len’
# is the length of a word.

# Space Complexity: The space complexity of the algorithm is O(M + N)
# Since at most, we will be storing all the words in the two HashMaps.