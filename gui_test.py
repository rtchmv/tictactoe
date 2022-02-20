import arcade
import arcade.gui


class MyWindow(arcade.Window):
    
    def __init__(self):
        
        super().__init__()
        
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.color.AERO_BLUE)

        self.v_box = arcade.gui.UIBoxLayout()
        

        # Create menu
        top_label = arcade.gui.UILabel(text='Tic Tac Toe', text_color=arcade.color.ALIZARIN_CRIMSON)
        self.v_box.add(top_label.with_space_around(bottom=20))
        
        st = {
            "bg_color": (221, 19, 21)
        }
        start_button = arcade.gui.UIFlatButton(text="Start Game", width=200, style=st)
        self.v_box.add(start_button.with_space_around(bottom=20))

        exit_button = arcade.gui.UIFlatButton(text='Exit', width=200)
        self.v_box.add(exit_button.with_space_around(bottom=20))

        #button.on_click = self.on_click_start

        self.manager.add(
                arcade.gui.UIAnchorWidget(
                    anchor_x='center_x', 
                    anchor_y='center_y', 
                    child=arcade.gui.UIPadding(child=self.v_box, padding=(10,10,10,10), bg_color=arcade.color.AFRICAN_VIOLET)))


    def on_click_start(self, event):
        print("Start:", event)
        button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        self.v_box.add(button.with_space_around(bottom=20))
        
        for i in self.v_box.children:
            print(i.center_y)
        
        self.manager.disable()

        self.manager.children.clear()


    def on_draw(self):
        self.clear()
        self.manager.draw()



def main():
    window = MyWindow()
    arcade.run()          


if __name__ == "__main__":
    main()