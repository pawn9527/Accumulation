#!/usr/bin/env python
# coding:utf8
"""
作者:pawn
邮箱:pawn9537@gmail.com
日期:18-3-9
时间:下午5:30
"""


class Solution:
    # 矩形覆盖
    def rect_cover(self, number):
        """
        问题:
        我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形.
        请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
        分析:
        误区: 陷入 面积的误区
        n     count
        1       1
        2       2
                        n
        [                                     ]
        [                                     ]
        思路: 放置最后一个 正方形就两种情况
        1. 横着放: 下方下方必须是两个竖着放的 所以 f(n-2)种摆放方式
        2. 竖着放:  除了自己前面随意拜访:  f(n-1)种摆放方式
        n      f(n-1) + f(n - 2)
        结论: 变形的斐波那契数列
        :param number:
        :return:
        """
        if number <= 1:
            return 1
        elif number == 2:
            return 2
        a = 1
        b = 1
        for x in range(1, number + 1):
            a, b = b, a + b
        return a

    # 看错题目了, 看成计算二进制了
    def NumberOf1(self, n):
        """
        输入一个整数,输出该数二进制.其中负数用补码表示.
        原理: 10进制数字如何转化为2进制的数字
        10 进制的数字被2  辗转相除得到的余数倒序排列

        得到数字的 源码
        按位取反得到 反码
        反码加+1 得到补码
        :param n:
        :return:
        """
        binary_list = []

        def gen(x):
            divisor = x // 2
            remainder = x - divisor * 2
            binary_list.append(remainder)
            if divisor <= 1:
                binary_list.append(divisor)
                # 倒序相排
                return binary_list[::-1]
            else:
                return gen(divisor)

        if n < 0:
            origin = gen(abs(n))
            reverse_code = list(map(lambda x: 1 - x, origin))

            def up(origin_list, index):

                end_number = origin_list[index]
                if end_number == 1:
                    origin_list[index] = 0
                    return up(origin_list, index - 1)
                else:
                    origin_list[index] = 1
                    return origin_list

            complement_code = up(reverse_code, len(reverse_code) - 1)
            return complement_code
        elif n == 0:
            return [0]
        else:
            return gen(n)

    def NumbersOf1(self, n):
        """
        输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示.
        思路: 如果一个整数不为0，那么这个整数至少有一位是1。如果我们把这个整数减1，那么原来处在整数最右边的1就会变为0，
        原来在1后面的所有的0都会变成1(如果最右边的1后面还有0的话)。其余所有位将不会受到影响。
        举个例子：
        一个二进制数1100，从右边数起第三位是处于最右边的一个1。减去1后，第三位变成0，
        它后面的两位0变成了1，而前面的1保持不变，因此得到的结果是1011.我们发现减1的结果是把最右边的一个1开始的所有位都取反了。
        这个时候如果我们再把原来的整数和减去1之后的结果做与运算，从原来整数最右边一个1那一位开始所有位都会变成0。
        如1100&1011=1000.也就是说，把一个整数减去1，再和原整数做与运算，会把该整数最右边一个1变成0.那么一个整数的二进制有多少个1，就可以进行多少次这样的操作。
        :param n:
        :return:
        """
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            count += 1
            n = (n - 1) & n
        return count

    def power(self, base, n):
        """
        问题: 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
        思路:
             * 1.全面考察指数的正负、底数是否为零等情况。
             * 2.写出指数的二进制表达，例如13表达为二进制1101。
             * 3.举例:10^1101 = 10^0001*10^0100*10^1000。
             * 4.通过&1和>>1来逐位读取1101，为1时将该位代表的乘数累乘到最终结果。
        :param base: 浮点数(有正负)
        :param n: 幂(有正负, 有奇偶)
        :return:
        """
        res = 1
        curr = base
        exponent = n
        if n < 0:
            assert base != 0, "分母不能w为零"
            exponent = -n
        elif n == 0:
            return 1
        while exponent != 0:
            if exponent & 1 == 1:
                res *= curr
            curr *= curr
            exponent >>= 1
        return res if n >= 0 else (1 / res)


if __name__ == '__main__':
    solution = Solution()
    # print(solution.rect_cover(number=1000))
    # print(solution.NumberOf1(n=29))
    print(solution.power(-2, -1))
