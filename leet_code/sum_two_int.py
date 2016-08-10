'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.


https://www.hrwhisper.me/leetcode-sum-two-integers/
'''

'''
// use a ^ b can calculate sum without carry
// use (a & b) << 1 can calculate carry

//  C solution 1
int getSum(int a, int b) {
    if (b == 0) return a;
    int sum = a ^ b;
    int carry = (a & b) << 1;
    return getSum(sum, carry);
}

//  C solution 2
int getSum(int a, int b) {
    while (b) {
        int carry = (a & b) << 1;
        a = a ^ b;
        b = carry;
    }
    return a;
}
'''


def get_sum_1(a, b):
    # b is carry , a is bit sum
    while b:
        a, b = (a ^ b), (a & b) << 1
    return a


def get_sum(a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    MAX_INT = 0x7FFFFFFF
    MIN_INT = 0x80000000
    MASK = 0x100000000
    while b:
        a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
    return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)


print get_sum_1(-1, 0)
