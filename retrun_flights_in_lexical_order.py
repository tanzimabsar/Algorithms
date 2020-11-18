from typing import List

class Solution:

    def findItinerary(self, tickets, current, start):

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

        # Sort based on lexographical order so that alphabetical airports come first 
        for ticket in tickets:
            graph[ticket[0]].sort(reverse=True)

        """for item in graph.values():

            graph[item].sort()"""

        print(graph)

        stack = []

        def helper(node):

            # while there is a node and we are not at a dead end then visit the nect node and mark as visited
            while graph[node]:
                
                    helper(graph[node].pop(0))

            # record the return values (visited nodes) into the stack
            stack.append(node)

        # this is our starting point
        helper(start)
        
        return stack[::-1]




sol = Solution()
print(sol.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]], [], 'JFK'))
# This is a cyclical graph
print(sol.findItinerary([['a','b'],['b','c'],['c','s'],['s','a']], [], 'a'))


# JFK MUC LHR SFO SJC 