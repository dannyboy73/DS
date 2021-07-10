# pg 153 - Ruler drawing using recursion
def draw_line(tick_length, tick_label=''):
    ''' Draw a line with given tick length '''
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label

    print(line)

def draw_interval(center_length):
    ''' Draw tick interval based upon a central tick length'''
    if center_length > 0:
        draw_interval(center_length - 1)  # recursively draw top ticks
        draw_line(center_length)  # draw center tick
        draw_interval(center_length - 1)  # recursively draw bottom ticks

def draw_ruler(num_inches, major_length):
    ''' The driver function to draw the ruler '''
    draw_line(major_length, '0')  # draw inch 0 line
    for j in range(1, 1 + num_inches):  
        draw_interval(major_length - 1)  # draw interior ticks for inch
        draw_line(major_length, str(j))  # draw inch j line and label

draw_ruler(3, 3)
