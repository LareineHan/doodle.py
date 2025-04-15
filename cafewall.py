import turtle                       # so that I can use Graphics
import Lab2_functions                # so that I can draw rectangles and lines

# set mortar joints between rows
MORTAR = 4

def main():

    turtle.setworldcoordinates(0, 400, 650, 0)
    turtle.clear()
    turtle.shape('turtle')
    turtle.pencolor('olive drab')
    turtle.fillcolor('sienna')
    turtle.bgcolor('grey')

    #### YOUR CODE GOES HERE #################
    turtle.speed(0)
    
    ### CALL FUNCTIONS ###

    ## upper left : a single row
    draw_a_row(0, 0, 4, 20)
    ## mid left : a single row
    draw_a_row(50, 70, 5, 30)
    ## lower left : rows
    draw_a_grid(10, 150, 4, 25, 1, 4, MORTAR)
    ## lower middle : rows
    draw_a_grid(250, 200, 3, 25, 10, 3, MORTAR)
    ## lower right : rows
    draw_a_grid(425, 180, 5, 20, 10, 5, MORTAR)
    ## upper right : rows
    draw_a_grid(400, 20, 2, 35, 35, 2, MORTAR)

    ### MY FUNCTIONS ###
    
    # 1. Draw a row by repeating pair of boxes 
def draw_a_row(x_pos, y_pos, pairs, size):
    steps = 0  
    for boxes in range(pairs):
        current_pen = x_pos + (size * steps)
        double = current_pen + size
        cross_from_to = y_pos + size
        ''' draw a black box
            & drawing lines for cross (first / and then  \) inside the box '''
        Lab2_functions.draw_rect(current_pen,y_pos,size,size,"black") 
        Lab2_functions.draw_line(current_pen,y_pos,double,cross_from_to,"blue")
        Lab2_functions.draw_line(current_pen,cross_from_to,double,y_pos,"blue")

        ''' draw a white box
            add box number 2 to update starting point of the next loop
            number 2 (steps) will be used to calculate adding width of 2 boxes '''
        Lab2_functions.draw_rect(double,y_pos,size,size,"white")
        steps += 2

    # 2. Drawing Grids (Rows)
def draw_a_grid(x_pos, y_pos, pairs, size, offset, repeat, motar):
    first_x_pos = x_pos
    first_y_pos = y_pos 
    second_x_pos = first_x_pos + offset
    second_y_pos = first_y_pos + size  + motar
    ''' Using for loop to repeat a set of rows
       after draw each row, update y position
       for following rows '''
    for row in range (1,repeat+1) : 
        draw_a_row(first_x_pos,first_y_pos,pairs,size) # 1st row
        first_y_pos += ((size + motar) * 2) 
        draw_a_row(second_x_pos,second_y_pos,pairs,size) # 2nd row
        second_y_pos += ((size + motar) * 2)
    ##########################################

if __name__ == "__main__":
    main()
    turtle.done()  # Finish drawing (optional)
