"""
Given two version numbers, version1 and version2, compare them.

Version numbers consist of one or more revisions joined by a dot '.'.
Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.

To compare version numbers, compare their revisions in left-to-right order.
Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

Return the following:

If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.
 

Example 1:

Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both "01" and "001" represent the same integer "1".
"""
def compareVersion(self, version1: str, version2: str) -> int:
    version1 = version1.split(".")
    version2 = version2.split(".")
    while len(version1) < len(version2):
        version1.append("0")
    while len(version1) > len(version2):
        version2.append("0")
    for i in range(len(version1)):
        x = int(version1[i])
        y = int(version2[i])
        if x > y:
            return 1
        if x < y:
            return -1
    return 0
"""
TC = o(n)
SC = o(n)
"""