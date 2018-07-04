# implementation of card game - Memory

import simplegui
import random

cards = []
exposed = []
clicked_card1 = -1
clicked_card2 = -1
count = 0

# helper function to initialize globals
def new_game():
    global cards
    global exposed
    global state
    global count
    
    state = 0
    count = 0
    temp1 = range(0, 8)
    temp2 = range(0, 8)
    cards = temp1 + temp2
    random.shuffle(cards)
    # print cards
    
    exposed = [False, False, False, False, False, False, False, False]
    exposed.extend(exposed)

        
# define event handlers
def mouseclick(pos):
    # add game state logic here
    index = pos[0]//50
    global exposed
    global state
    global clicked_card1
    global clicked_card2
    global count

    if state == 0:
        state = 1
        clicked_card1 = index
        exposed[index] = True
    elif state == 1:
        if exposed[index] != True:
            state = 2
            clicked_card2 = index
            exposed[index] = True
            count += 1
    else:
        if exposed[index] == True:
            pass
        else:
            if cards[clicked_card1] != cards[clicked_card2]:
                exposed[clicked_card1] = False
                exposed[clicked_card2] = False

            state = 1
            clicked_card1 = index
            exposed[index] = True
            #print clicked_card1, clicked_card2
            
    
    #print state
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    
    label.set_text("Turns = " + str(count))
    
    for card_index in range(len(cards)):  
        card_pos = 50 * card_index
        if exposed[card_index]:
            canvas.draw_text(str(cards[card_index]), (card_pos+5, 75), 80, 'White')
        else:
            canvas.draw_polygon([[card_pos, 0], [card_pos+ 50, 0], [card_pos+50, 100], [card_pos, 100]], 4, 'White', 'Green')
         
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric