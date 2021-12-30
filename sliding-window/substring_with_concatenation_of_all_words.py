class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_freq = {}

        for word in words:
            if word not in word_freq:
              word_freq[word] = 0
            word_freq[word] += 1

        result = []
        len_str = len(s)
        len_word = len(words[0])
        len_words = len(words)
        len_substr = len(words) * len_word # Length of concatenated word

        # Our range given our substring
        for i in range((len(s) - len_substr)+1):
            words_seen = {}

            # Searches for words in our given point in the substring
            for j in range(0, len_words):
                next_word_index = i + j * len_word

                # Get the next word from the string
                word = s[next_word_index: next_word_index + len_word]

                # Break if we don't need this word and check next word
                if word not in word_freq:
                    break

                # Add the word to the 'words_seen' map
                if word not in words_seen:
                    words_seen[word] = 0
                words_seen[word] += 1

                # If the word is in words_seen but is not in
                # word_freq then break bc we are looking
                # for words in word_freq
                if words_seen[word] > word_freq[word]:
                    break

                # Store index if we have found all the words
                if j + 1 == len_words:
                    result.append(i)

        return result

# Time Complexity: The time complexity of the above algorithm will be
# O(N * M * Len) where ‘N’ is the number of characters in
# the given string, ‘M’ is the total number of words, and ‘Len’
# is the length of a word.

# Space Complexity: The space complexity of the algorithm is O(M + N)
# Since at most, we will be storing all the words in the two HashMaps.