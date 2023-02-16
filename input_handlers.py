from typing import Optional
import tcod.event
from actions import Action, EscapeAction, MovementAction

#We're creating a class EventHandler, which is a subclass of EventDispatch from the tcod library.
#EventHandler sends an event to its proper method based on what type of event it is.
class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()
    
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None #This method will receive receive key press events, and return either Action, or None if no valid key was pressed.

        key = event.sym

        if key == tcod.event.K_UP:
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = MovementAction(dx=1, dy=0)
        
        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        #No valid key was pressed
        return action