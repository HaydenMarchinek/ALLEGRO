# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 00:58:58 2024

@author: hayde
"""

import numpy as np
import matplotlib.pyplot as plt

# Function create villas
def villas(x, y, color='black'):
    x_values = np.linspace(x - 0.03, x + 0.03, 100)
    y_values = np.linspace(y - 0.03, y + 0.03, 100)
    xpos = []
    xneg = []
    ypos = []
    yneg = []
    for i in range(len(x_values)):
        xpos.append(x + 0.03)
        ypos.append(y + 0.03)
        xneg.append(x - 0.03)
        yneg.append(y - 0.03)
    plt.plot(xneg, y_values, color=color, linewidth=1)
    plt.plot(xpos, y_values, color=color, linewidth=1)
    plt.plot(x_values, yneg, color=color, linewidth=1)
    plt.plot(x_values, ypos, color=color, linewidth=1)
    return x_values, y_values  


def plot_CircuitBoard(x_bounds, y_bounds):
    # Generate Initial Conditions for Ellipses
    num_ellipses = 32
    semi_minor_lengths = []
    current_length = 42.13  

    for i in range(num_ellipses):
        semi_minor_lengths.append(current_length)
        if i % 2 == 0:
            current_length += 1707 / 800
        else:
            current_length += 0.06

    angle_rad = np.radians(49)
    semi_major_lengths = [b / np.cos(angle_rad) for b in semi_minor_lengths]

    plt.figure(figsize=(10, 10))

    x_values = np.linspace(-34.3, 34.3, 1000)
    downward_shift = 35.462979

    ## PLOT FRAME ##
    
    b1_black = 42
    a1_black = b1_black / np.cos(angle_rad)
    b2_black = 77.3
    a2_black = b2_black / np.cos(angle_rad)
    y_bl = b1_black * np.sqrt(1 - (x_values ** 2) / (a1_black ** 2)) - downward_shift
    y_b2 = b2_black * np.sqrt(1 - (x_values ** 2) / (a2_black ** 2)) - downward_shift

    # Ellipse 1
    plt.plot(x_values, y_bl, color='black')

    # Ellipse 2
    plt.plot(x_values, y_b2, color='black')
    
    # Add black boundary lines
    plt.plot([-34.3, -34.3], [0, 38.4891196], color='black', linewidth=1)
    plt.plot([34.3, 34.3], [0, 38.4891196], color='black', linewidth=1)

    ## PLOT ORANGE ELLIPSES ##
    
    for i, (b, a) in enumerate(zip(semi_minor_lengths, semi_major_lengths)):
        y_values = b * np.sqrt(1 - (x_values ** 2) / (a ** 2))
        y_values_shifted = y_values - downward_shift
        y_values_shifted_positive = y_values_shifted[y_values_shifted >= 0]
        x_values_positive = x_values[:len(y_values_shifted)][y_values_shifted >= 0]

        if i == 0:
            y_bottom_orange = y_values_shifted
        if i == len(semi_minor_lengths) - 1:
            y_top_orange = y_values_shifted
    
    # Get parameters for the lowest and topmost black ellipses (first and last ellipses)
    b_lowest = 42  
    a_lowest = b_lowest / np.cos(angle_rad) 

    b_topmost = 77.3  
    a_topmost = b_topmost / np.cos(angle_rad)
    
    #Fill Orange Ellipse Gaps
    orange_y_values = []
    for i, (b, a) in enumerate(zip(semi_minor_lengths, semi_major_lengths)):
        y_values = b * np.sqrt(1 - (x_values ** 2) / (a ** 2))
        y_values_shifted = y_values - downward_shift
        orange_y_values.append(y_values_shifted)
    
    # Fill regions between every other ellipse
    for i in range(1, len(orange_y_values) - 1, 2):
        # Get the y-values for the two ellipses
        y_bottom = orange_y_values[i]
        y_top = orange_y_values[i + 1]
        
        # Fill the area between them
        plt.fill_between(
            x_values,            
            y_bottom,             
            y_top,               
            where=(y_top > y_bottom),
            color='orange',      
        )
    #Fill Border Region
    
    plt.fill_between(
        x_values,                
        y_bottom_orange,       
        y_bl,                    
        color='orange',          
        )
    
    plt.fill_between(
    x_values,
    y_b2,                    
    y_top_orange,         
    color='orange',        
    )
    
    ## Plot Traces ##

    Trace_Start = []
    current_trace = 42.18
    while len(Trace_Start) < 16:
        Trace_Start.append(current_trace)
        current_trace += 1707 / 800 + 0.06
    
    for C in Trace_Start:
        num_ellipses = 22
        semi_minor_lengths = []
        current_length = C
        for i in range(num_ellipses):
            semi_minor_lengths.append(current_length)
            current_length += 0.0975
    
        semi_major_lengths = [b / np.cos(angle_rad) for b in semi_minor_lengths]
        x_value_ranges = [(-31.5 + i*(6621/2200 +0.06), 33.3) for i in range(num_ellipses)]
    
        for i, (b, a) in enumerate(zip(semi_minor_lengths, semi_major_lengths)):
            x_start, x_end = x_value_ranges[i]
            x_values = np.linspace(x_start, x_end, 1000)
            y_values = b * np.sqrt(1 - (x_values**2) / (a**2))
            y_values_shifted = y_values - downward_shift
            y_values_shifted_positive = y_values_shifted[y_values_shifted >= 0]
            x_values_positive = x_values[:len(y_values_shifted)][y_values_shifted >= 0]
    
            # Alternate color between blue and red
            color = 'blue' if i % 2 == 0 else 'red'
    
            # Plot the ellipses
            plt.plot(x_values_positive, y_values_shifted_positive, color=color, linewidth = 0.65)
    
            # Use villas() at the left-most point of each ellipse with matching color
            if len(x_values_positive) > 0:
                left_most_x = x_values_positive[0]
                left_most_y = y_values_shifted_positive[0]
                villas(left_most_x, left_most_y, color=color)

    ## SET VERTICAL LINES ##
    
    x_vertical_lines = []
    current_x = -34.17
    increment1 = (6621 / 2200)
    increment2 = 0.06
    toggle = True

    while current_x <= 33.35:
        x_vertical_lines.append(current_x)
        if toggle:
            current_x += increment1
        else:
            current_x += increment2
        toggle = not toggle

    ## FILL REGIONS BETWEEN VERTICAL LINES ##
    
    for i in range(1, len(x_vertical_lines) - 1, 2):
        x_left = x_vertical_lines[i]
        x_right = x_vertical_lines[i + 1]

        # Define the x range for fill
        x_fill = np.linspace(x_left, x_right, 1000)

        # Compute the y-values for the bottom black ellipse
        y_lowest_ellipse = np.zeros_like(x_fill)
        for j, x in enumerate(x_fill):
            if abs(x) <= a1_black:
                y_lowest = b1_black * np.sqrt(1 - (x ** 2) / (a1_black ** 2))
                y_lowest_shifted = y_lowest - downward_shift
            else:
                y_lowest_shifted = -downward_shift  
            y_lowest_ellipse[j] = y_lowest_shifted

        # Compute the y-values for the top black ellipse
        y_topmost_ellipse = np.zeros_like(x_fill)
        for j, x in enumerate(x_fill):
            if abs(x) <= a2_black:
                y_topmost = b2_black * np.sqrt(1 - (x ** 2) / (a2_black ** 2))
                y_topmost_shifted = y_topmost - downward_shift
            else:
                y_topmost_shifted = 40 
            y_topmost_ellipse[j] = y_topmost_shifted

        # Fill the area between the two ellipses for this x range
        plt.fill_between(
            x_fill,
            y_lowest_ellipse, 
            y_topmost_ellipse,  
            color='orange',  
        )
 
    # Get the x-value of the leftmost black boundary line and the leftmost orange vertical line
    x_left_black = -34.3  
    x_left_orange = x_vertical_lines[0]
    
    # Compute the y-values for the lowest and topmost black ellipses at these x positions
    y_lowest_black_left = b_lowest * np.sqrt(1 - (x_left_black ** 2) / (a_lowest ** 2)) - downward_shift
    y_topmost_black_left = b_topmost * np.sqrt(1 - (x_left_black ** 2) / (a_topmost ** 2)) - downward_shift
    
    y_lowest_black_orange = b_lowest * np.sqrt(1 - (x_left_orange ** 2) / (a_lowest ** 2)) - downward_shift
    y_topmost_black_orange = b_topmost * np.sqrt(1 - (x_left_orange ** 2) / (a_topmost ** 2)) - downward_shift
    
    # Left Border Fill
    plt.fill_between(
        [x_left_black, x_left_orange],
        [y_lowest_black_left, y_lowest_black_orange],  
        [y_topmost_black_left, y_topmost_black_orange],
        color='orange',
    )
    
    ## PLOT CONNECTOR STRIP ##    

    x_fill = np.linspace(x_vertical_lines[-1], 34.3, 1000)
    
    # Compute the y-values for the lowest black ellipse (same as before)
    y_lowest_ellipse = np.zeros_like(x_fill)
    for i, x in enumerate(x_fill):
        if abs(x) <= a_lowest:
            y_lowest = b_lowest * np.sqrt(1 - (x ** 2) / (a_lowest ** 2))
            y_lowest_shifted = y_lowest - downward_shift
        else:
            y_lowest_shifted = -downward_shift  
        y_lowest_ellipse[i] = y_lowest_shifted
    
    # Compute the y-values for the topmost black ellipse
    y_topmost_ellipse = np.zeros_like(x_fill)
    for i, x in enumerate(x_fill):
        if abs(x) <= a_topmost:
            y_topmost = b_topmost * np.sqrt(1 - (x ** 2) / (a_topmost ** 2))
            y_topmost_shifted = y_topmost - downward_shift
        else:
            y_topmost_shifted = 40  
        y_topmost_ellipse[i] = y_topmost_shifted
    
    # Now fill the area between the lowest ellipse curve and the topmost ellipse curve
    plt.fill_between(
        x_fill,           
        y_lowest_ellipse,  
        y_topmost_ellipse,    
        color='grey', 
        alpha = 1
    )
    
    ## GET FINAL PLOT ##
    
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title('ALLEGRO EndCap Calorimeter Electrode Board Layout')
    plt.xlabel('X (cm)')
    plt.ylabel('Y (cm)')
    plt.xlim(x_bounds)
    plt.ylim(y_bounds)

    plt.show()

# Run the updated plot function
plot_CircuitBoard(x_bounds=(-40, 40), y_bounds=(-10, 70))