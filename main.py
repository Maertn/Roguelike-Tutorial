#!/usr/bin/env python3
import tcod
from actions import EscapeAction, MovementAction
from input_handlers import EventHandler


def main() -> None:
    #Defining variables for screen size.
    screen_width = 80
    screen_height = 50

    #Gives coordinates for the players position.
    #'int' is used to prevent the creation of floats, which'll crash the program.
    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    #Specifying the tileset
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )
    #Importing EventHandler into main
    event_handler = EventHandler()

    #This creates the screen
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset = tileset,
        title = "Yet another roguelike tutorial",
        vsync = True, 
    ) as context:
        #This creates the console we'll be drawing to. The "order" argument allows us to draw 2D arrays as [x,y] instead of NumPy's standard [y,x]
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True: #while True creates the gameloop which'll run until explicitly stopped 
            root_console.print(x=player_x, y=player_y, string="@") #This line tells us where to put the @

            context.present(root_console) #The command context.present allows us to update the screen

            root_console.clear()

            for event in tcod.event.wait(): #This line asks the program to wait for user input.
                action = event_handler.dispatch(event)

                if action is None:
                    continue
                
                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy
                
                elif isinstance(action,EscapeAction):
                    raise SystemExit()


if __name__ == "__main__":
    main()