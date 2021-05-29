import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # 188ms
        names = collections.defaultdict(str) 
        graph = collections.defaultdict(set)
        visited = set()
        ans = []
        for account in accounts:
            for address in account[1:]:
                graph[account[1]].add(address)
                graph[address].add(account[1])
                names[address] = account[0]
        for email in graph:
            if email in visited:
                continue
            visited.add(email)
            stack = [email]
            mails = []
            while stack:
                current = stack.pop()
                mails.append(current)
                for next in graph[current]:
                    if next not in visited:
                        stack.append(next)
                        visited.add(next)
            ans.append([names[current]]+sorted(mails))
        return ans

    # 292ms
    class Account:
        def __init__(self, l):
            self.name = l[0]
            self.emails = l[1:]

        def __hash__(self):
            return hash(str(self))

        def __eq__(self, other):
            return self.name == other.name and len(self.emails) == len(other.emails) \
                   and set(self.emails) == set(other.emails)

    def accountsMerge2(self, accounts: List[List[str]]) -> List[List[str]]:
        accounts = [self.Account(a) for a in accounts]
        email_dict, visited, finalres = collections.defaultdict(set), set(), []

        for acc in accounts:
            for email in acc.emails:
                email_dict[email].add(acc)

        for acc in accounts:
            if acc in visited:
                continue
            res = set()
            self.dfs(acc, email_dict, visited, res)
            finalres.append([acc.name] + sorted(res))
        return finalres

    def dfs(self, acc: Account, email_dict: Dict, visited: Dict, res: List[List[str]]) -> None:
        if acc in visited:
            return
        visited.add(acc)
        for email in acc.emails:
            res.add(email)
            for a in email_dict[email]:
                self.dfs(a, email_dict, visited, res)

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python {0} <testdata.txt>".format(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("{0} not found...".format(argv[1]))
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = {0}".format(temp))
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    accounts = [[_ for _ in fld.split(",")] for fld in flds]
    print("accounts = \"{0}\"".format(accounts))

    sl = Solution()
    time0 = time.time()

    result = sl.accountsMerge(accounts)

    time1 = time.time()

    print("result = \"{0}\"".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
