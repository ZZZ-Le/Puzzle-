from ui.gui import GUI
from game.board import Board

def main():
    # 初始化游戏盘面
    board = Board(8, 8)
    board.initialize()

    # 初始化图形界面
    gui = GUI(board)

    # 运行图形界面
    gui.run()

if __name__ == "__main__":
    main()