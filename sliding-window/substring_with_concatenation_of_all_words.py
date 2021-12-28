class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0 or len(words[0]) == 0:
            return []

        word_frequency = {}

        for word in words:
            if word not in word_frequency:
              word_frequency[word] = 0
            word_frequency[word] += 1

        result_indices = []
        len_str = len(s)
        len_word = len(words[0])
        len_words = len(words)
        len_substr = len(words) * len_word # Length of concatenated word

        # Our range given our substring
        for i in range((len(s) - len_substr)+1):
            words_seen = {}

            # Our range given the length of our words array
            for j in range(0, len_words):
                next_word_index = i + j * len_word

                # Get the next word from the string
                word = s[next_word_index: next_word_index + len_word]

                # Break if we don't need this word
                if word not in word_frequency:
                    break

                # Add the word to the 'words_seen' map
                if word not in words_seen:
                    words_seen[word] = 0
                words_seen[word] += 1

                # No need to process further if the word has higher frequency than required
                if words_seen[word] > word_frequency.get(word, 0):
                    break

                # Store index if we have found all the words
                if j + 1 == len_words:
                    result_indices.append(i)

        return result_indices