# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def isValid(self, s: str) -> bool:
        result = False
        i = 0
        while i < len(s) != 0:
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                result = False
                i += 1
                continue
            if s[i] == ')':
                result = True
                if i != 0 and s[i - 1] == '(':
                    s = s[0: i - 1:] + s[i + 1::]
                    i -= 1
                    continue
                else:
                    return False
            if s[i] == ']':
                result = True
                if i != 0 and s[i - 1] == '[':
                    s = s[0: i - 1:] + s[i + 1::]
                    i -= 1
                    continue
                else:
                    return False
            if s[i] == '}':
                result = True
                if i != 0 and s[i - 1] == '{':
                    s = s[0: i - 1:] + s[i + 1::]
                    i -= 1
                    continue
                else:
                    return False
        if len(s) != 0:
            return False
        return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Solution()
    print(obj.isValid("([]"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
