# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        host = startUrl.split("/", 3)[2] # Want to get hostname to compare with sub-urls
        print(host)
        queue, visited = [startUrl], set([startUrl])

        # For every url, we want to get the sub-urls and for every sub-urls,
        # we want to get its sub-urls until we have visited everything and
        # get all the unique sub-urls. We can use BFS or DFS for this
        for url in queue:
            for subUrl in htmlParser.getUrls(url):

                # Want to make sure we haven't visited and matches our host name
                if subUrl not in visited and host in subUrl:
                    visited.add(subUrl) # Mark as visited
                    queue.append(subUrl) # Add to queue to check if it has sub-urls

        return visited

# Time Complexity: O(n) on average because we traverse through each "vertex" once
# and we compare the host with the subUrl per traversal.

# Space Complexity: O(n)

# Solution: https://leetcode.com/problems/web-crawler/discuss/416021/Easy-Python-with-find-and-stack/448055