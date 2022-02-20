import arcade

# 0 - empty, 1 - X, 2 - 0

# grid size
ROW_COUNT = 3
COLUMN_COUNT = 3

# grid cell size
WIDTH = 200
HEIGHT = 200

# толщина линий
LINE_WIDTH = 10

# grid margin
MARGIN = 10

# screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN
SCREEN_TITLE = "Tic Tac Toe"

class Cell():
    
    def __init__(self, position_x, position_y, status):
        self.position_x = position_x
        self.position_y = position_y
        self.status = status

    def draw(self):
        arcade.draw_rectangle_filled(self.position_x, self.position_y, WIDTH, HEIGHT, arcade.color.WHITE)

        if self.status == 1:
            arcade.draw_line(self.position_x - WIDTH / 2, self.position_y - HEIGHT / 2, self.position_x + WIDTH / 2, self.position_y + WIDTH / 2, arcade.color.RED, LINE_WIDTH)
            arcade.draw_line(self.position_x - WIDTH / 2, self.position_y + HEIGHT / 2, self.position_x + WIDTH / 2, self.position_y - WIDTH / 2, arcade.color.RED, LINE_WIDTH)

        if self.status == 2:
            arcade.draw_circle_outline(self.position_x, self.position_y, WIDTH / 2, arcade.color.RED, LINE_WIDTH)




class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)
        
        self.grid = []

        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)

        self.grid_sprite_list = []

        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                x = column * (WIDTH + MARGIN) + (WIDTH / 2 + MARGIN)
                y = row * (HEIGHT + MARGIN) + (HEIGHT / 2 + MARGIN)
                self.grid_sprite_list.append(Cell(x, y, 0))

        self.turn = 1
        self.count = 0


    def resync_grid_with_sprites(self):

        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                pos = row * COLUMN_COUNT + column
                self.grid_sprite_list[pos].status = self.grid[row][column]
    

    def game_over(self):
        arcade.draw_text('GAME OVER', 100, 100, arcade.color.AFRICAN_VIOLET, 50)
    
    
    def all_the_same(self, test_list):
        
        if len(test_list) == test_list.count(0):
            return False

        return len(test_list) == test_list.count(test_list[0])

    
    def win_prove(self):
        for row in range(ROW_COUNT):
            test_list = []
            for column in range(COLUMN_COUNT):
                test_list.append(self.grid[row][column])
            print(self.all_the_same(test_list))

        for column in range(COLUMN_COUNT):
            test_list = []
            for row in range(ROW_COUNT):
                test_list.append(self.grid[row][column])
            print(self.all_the_same(test_list))

    
    def on_draw(self):
        
        self.clear()
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                pos = row * COLUMN_COUNT + column
                self.grid_sprite_list[pos].draw()

        if self.count == 9:
            self.game_over()
    
    
    
    def on_mouse_press(self, x, y, button, modifiers):
        
        column = int(x // (WIDTH + MARGIN))
        row = int (y // (HEIGHT + MARGIN))

        if row < ROW_COUNT and column < COLUMN_COUNT:
            if self.grid[row][column] == 0:
                self.count = self.count + 1
                if self.turn == 1:
                    self.grid[row][column] = 1
                    self.turn = 2                    
                else:
                    self.grid[row][column] = 2
                    self.turn = 1


        self.resync_grid_with_sprites()

        self.win_prove()

       


def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()          


if __name__ == "__main__":
    main()