from typing import List

class Solution:

    def findItinerary(self, tickets, current):

        if not tickets:
            return current

        graph = {}

        # Create the keys that are needed for this data structure
    
        for source in tickets:

            graph[source[0]] = []
            graph[source[1]] = []

        # append each connection to the graph since we know the set of sources

        for source in tickets:

            graph[source[0]].append(source[1])

        print(graph)

        stack = []

        def helper(node):

            while graph[node]:

                helper(graph[node].pop(0))

            stack.append(node)

        helper('JFK')
        
        return stack[::-1]




sol = Solution()
print(sol.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]], []))
#print(sol.findItinerary([["MUC", "LHR"], ["SFO", "SJC"], ["LHR", "SFO"]], []))


# JFK MUC LHR SFO SJC 