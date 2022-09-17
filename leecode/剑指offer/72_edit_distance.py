class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        array = [[None for i in range(m+1)] for j in range(n+1)]

        # 初始化第一列
        for j in range(m+1):
            array[0][j] = j
        
        # 初始化第一行
        for i in range(n+1):
            array[i][0] = i

        for i in range(1, n+1):
            for j in range(1, m+1):
                left = array[i-1][j] + 1
                down = array[i][j-1] + 1
                left_down = array[i-1][j-1]
                if word1[i-1] != word2[j-1]:
                    left_down += 1
                else:
                    array[i][j] = min(left, down, left_down)
                    
        return array[n - 1][m - 1]

def stringToString(input):
    # return input[1:-1].decode('string_escape')
    return input

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            word1 = stringToString(line);
            line = next(lines)
            word2 = stringToString(line);
            
            ret = Solution().minDistance(word1, word2)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()