import pygame
import sys
from game.board import Board

class GUI:
    def __init__(self, board):
        self.board = board
        self.cell_size = 60
        self.margin = 20
        self.width = self.board.cols * self.cell_size + 2 * self.margin
        self.height = self.board.rows * self.cell_size + 2 * self.margin + 50 #这50额外空间用于放按钮
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("数连争霸")
        self.font = pygame.font.SysFont(None, 36)
    
        # 加载背景图片
        self.background_image = pygame.image.load("assets/images/technology_background.jpg").convert()
        # 调整背景图片大小以适应窗口
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))

    def draw_board(self):
        # 绘制背景图片
        self.screen.blit(self.background_image, (0, 0))

        # 填充屏幕背景色为白色
        self.screen.fill((255, 255, 255))
        
        # 遍历棋盘的每一行
        for i in range(self.board.rows):
            # 遍历棋盘的每一列
            for j in range(self.board.cols):
                # 如果当前单元格的值为0，跳过绘制
                if self.board.grid[i][j] == 0:
                    continue
                
                # 计算当前单元格的左上角位置
                rect = pygame.Rect(
                    self.margin + j * self.cell_size,
                    self.margin + i * self.cell_size,
                    self.cell_size,
                    self.cell_size
                )
                
                # 绘制单元格的背景为灰色
                pygame.draw.rect(self.screen, (200, 200, 200), rect)
                
                # 渲染单元格中的数字为黑色文本
                text = self.font.render(str(self.board.grid[i][j]), True, (0, 0, 0))
                # 获取文本的矩形区域，并设置其中心与单元格中心对齐
                text_rect = text.get_rect(center=rect.center)
                # 将文本绘制到屏幕上
                self.screen.blit(text, text_rect)

        # 绘制重置按钮
        reset_button_rect = pygame.Rect(
            self.margin, self.margin + self.board.rows * self.cell_size + 20,
            self.cell_size * 2, self.cell_size // 2
        )
        pygame.draw.rect(self.screen, (200, 200, 200), reset_button_rect)
        reset_text = self.font.render("重置", True, (0, 0, 0))
        reset_text_rect = reset_text.get_rect(center=reset_button_rect.center)
        self.screen.blit(reset_text, reset_text_rect)

        # 更新整个屏幕的显示
        pygame.display.flip()
    
    
    def run(self):
        running = True
        selected = None
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()

                    # 检查是否点击了重置按钮
                    reset_button_rect = pygame.Rect(
                        self.margin, self.margin + self.board.rows * self.cell_size + 20,
                        self.cell_size * 2, self.cell_size // 2
                    )
                    if reset_button_rect.collidepoint(x, y):
                        self.board.reset()
                        continue
                
                    # 计算点击的格子
                    col = (x - self.margin) // self.cell_size
                    row = (y - self.margin) // self.cell_size
                    
                    # 检查点击的行和列是否在棋盘范围内
                    if 0 <= row < self.board.rows and 0 <= col < self.board.cols:
                        # 检查点击的单元格是否为空
                        if self.board.grid[row][col] != 0:
                            # 如果之前没有选中任何单元格，或者再次点击同一个单元格
                            if selected is None:
                                selected = (row, col)
                            else:
                                # 如果两次点击的是同一个单元格，不执行任何操作
                                if selected == (row, col):
                                    selected = None
                                else:
                                    # 执行交换逻辑
                                    self.board.process_turn(selected, (row, col))
                                    selected = None
            # 绘制棋盘
            self.draw_board()
        
        # 退出pygame
        pygame.quit()