import random
import math

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

    def initialize(self):
        """初始化游戏盘面，填充1-9的随机数字"""
        for i in range(self.rows):
            for j in range(self.cols):
                self.grid[i][j] = random.randint(2, 9)

    def reset(self):
        """重置游戏盘面"""
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.initialize()

    def get_cell(self, row, col):
        """获取指定位置的数字"""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.grid[row][col]
        return None

    def set_cell(self, row, col, value):
        """设置指定位置的数字"""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.grid[row][col] = value

    def process_turn(self, pos1, pos2):
        """处理玩家的一次操作"""
        r1, c1 = pos1
        r2, c2 = pos2

        num1 = self.get_cell(r1, c1)
        num2 = self.get_cell(r2, c2)

        # 如果两个数字相同，直接消除
        if num1 == num2:
            self.set_cell(r1, c1, 0)
            self.set_cell(r2, c2, 0)
            return True

        # 如果数字不同且没有1
        if num1 != num2 and num1 != 1 and num2 != 1:
            gcd = math.gcd(num1, num2)
            # 确保较小的数字除以公约数
            if num1 > num2:                
                new_num1 = num1 // gcd
                new_num2 = num2 // gcd
                if new_num2 == 1:
                    # 保留大的数字，消除小的数字
                    self.set_cell(r1, c1, new_num1)
                    self.set_cell(r2, c2, 0)
                    return True
                else:
                    # 替换为除后的结果
                    self.set_cell(r1, c1, new_num1)
                    self.set_cell(r2, c2, new_num2)
                    return True
            else:
                new_num1 = num1 // gcd
                new_num2 = num2 // gcd
                if new_num1 == 1:
                    # 保留大的数字，消除小的数字
                    self.set_cell(r1, c1, 0)
                    self.set_cell(r2, c2, new_num2)
                    return True
                else:
                    # 替换为除后的结果
                    self.set_cell(r1, c1, new_num1)
                    self.set_cell(r2, c2, new_num2)
                    return True  
        return False