class Solution(object):
    def findThePrefixCommonArray(self, A, B):

        setA = set()
        setB = set()
        result = []

        for i in range(len(A)):
            setA.add(A[i])
            setB.add(B[i])

            common = setA & setB
            result.append(len(common))

        return result


obj = Solution()

A = [1, 3, 2, 4]
B = [3, 1, 2, 4]

print(obj.findThePrefixCommonArray(A, B))