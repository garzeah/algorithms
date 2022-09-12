class Codec:

    # SC: O(n) where n is the amount of total links
    def __init__(self):
        self.chars = string.ascii_letters + string.digits
        self.decoded = {} # { shortUrl: longUrl }
        self.encoded = {} # { longUrl: shortUrl }

    # Generates a random alphanumeric sequence of characters of size 6
    # TC: O(1)
    def generate(self) -> str:
        code = ''.join(choice(self.chars) for _ in range(6))
        return "http://tinyurl.com/" + code

    # Encodes a long url to its corresponding short url
    # TC: O(1)
    def encode(self, longUrl: str) -> str:
        if longUrl in self.encoded:
            return self.encoded[longUrl]

        # Generates a code, want to make sure it is unique
        shortUrl = self.generate()
        while shortUrl in self.decoded:
            shortUrl = self.generate()

        # Want to record short to long (decode) and long to short (encode)
        # key-value pairs if we want to decode or encode
        self.decoded[shortUrl] = longUrl
        self.encoded[longUrl] = shortUrl

        return shortUrl

    # Decodes a short url to its corresponding long url
    # TC: O(1)
    def decode(self, shortUrl: str) -> str:
        return self.decoded[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

# Solution: https://leetcode.com/problems/encode-and-decode-tinyurl/discuss/1110551/JS-Python-Java-C%2B%2B-or-Easy-Map-Solution-w-Explanation