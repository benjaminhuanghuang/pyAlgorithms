'''
93. Restore IP Addresses

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

'''


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def dfs(s, sub, ips, ip):
            if sub == 4:  # should be 4 parts
                if s == '':
                    ips.append(ip[1:])  # remove first '.'
                return
            for i in range(1, 4):  # the three ifs' order cannot be changed!
                if i <= len(s):  # if i > len(s), s[:i] will make false!!!!
                    if int(s[:i]) <= 255:
                        dfs(s[i:], sub + 1, ips, ip + '.' + s[:i])
                    if s[0] == '0':
                        break  # make sure that res just can be '0.0.0.0' and remove like '00'

        ips = []
        dfs(s, 0, ips, '')
        return ips
