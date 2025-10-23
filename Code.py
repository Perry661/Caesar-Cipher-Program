class Password:
    def __init__(self, code):
        self.code = code
        self.caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'    # 大写字母字典
        self.lower = 'abcdefghijklmnopqrstuvwxyz'   # 小写字母字典

# 加密模块
    def encode(self, shift):
        num = 0
        s = ''
        for i in self.code:
            if i in self.caps:
                num = self.caps.find(i) + shift
                if num >= 26:
                    num -= 26
                s += self.caps[num]
            elif i in self.lower:
                num = self.lower.find(i) + shift
                if num >= 26:
                    num -= 26
                s += self.lower[num]
            else:
                s += i
        print('这是已加密字符串的: {}'.format(s))

# 复原模块
    def recover(self, shift):
        for i0 in range(1, shift+1):
            num = 0
            s = ''
            for i in self.code:
                if i in self.caps:
                    num = self.caps.find(i) + i0
                    if num >= 26:
                        num -= 26
                    s += self.caps[num]
                elif i in self.lower:
                    num = self.lower.find(i) + i0
                    if num >= 26:
                        num -= 26
                    s += self.lower[num]
                else:
                    s += i
            print('结果{}: {}'.format(i0, s))


# encode() = 加密，recover() = 复原（目前只能自己暴力破解（指自己输入数字））

s = input("输入字符（英文）：")
a = Password(s)

mode = input("加密（e）还是复原（r）：")
while True:
    if mode == '加密' or mode == '复原' or mode == 'e' or mode == 'r':
        break
    else:
        mode = input("请重新输入一遍，加密还是复原：")

if mode == '加密' or mode == 'e':
    shift = int(input("移动几位（数字需要小于或等于26）："))
    if shift > 26:
        shift = int(input("请重新输入，移动几位（数字需要小于或等于26）："))
    a.encode(shift)
else:
    shift = int(input("移动几位："))
    if shift > 26:
        shift = int(input("请重新输入，移动几位（数字需要小于或等于26）："))
    a.recover(shift)


# 测试字符：SERR PBQR PNZC
# 转换（13）：FREE CODE CAMP
# ******************************
# 测试日志：发现了一个bug，打印出来的结果多了一个（目前已修复）
    # （比方说明明只需要移动13位时，他只有在结果14（移动14位）的时候才能显示出来正确的代码。
    #  后面发现是因为结果1将输入进去的字符串又打印了一遍）
        # （也就是说结果1实际上应该是结果0（我在说什么））
