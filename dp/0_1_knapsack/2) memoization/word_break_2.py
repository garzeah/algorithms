class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        return self.helper(s, word_set)

    def helper(self, substr, word_set):
        res = []
        for word in word_set:
            prefix = substr[0:len(word)]

            # If our current substr doesn't start with any of the
            # words in our word_set, keep going until it does
            if substr.startswith(word) is False:
                continue

            # If we are at the last word then we want to append it to the res
            # then we want to store it in our cache where {'dog': ['dog']}
            if prefix == substr:
                res.append(prefix)

            # This will keep calling until we hit the last word. For example, we have
            # "sanddog" because we start with "cat". "cat" leads to "sand".
            # rest_of_words = ["dog"]
            # word = "sand"
            # phrase = "sand dog"
            # res = ["sand dog"]
            # dp = { 'dog': ['dog'], 'sanddog': ['sand dog'] }
            else:
                rest_of_words = self.helper(substr[len(word):], word_set)
                for phrase in rest_of_words:
                    res.append(prefix + " " + phrase)

        return res