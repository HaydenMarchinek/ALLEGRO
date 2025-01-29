# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 14:51:28 2024

@author: hayde
"""
import matplotlib.pyplot as plt

def FrontView():
    plt.figure() 

    # Plot High Voltage
    plt.fill_between([-30, -0.5], 0, 0.035, color='orange', alpha=1, label='High Voltage Pads')
    plt.fill_between([0.5, 30], 0, 0.035, color='orange', alpha=1)
    plt.fill_between([-30, -0.5], 1.19+0.12, 1.225+0.12, color='orange', alpha=1)
    plt.fill_between([0.5, 30], 1.19+0.12, 1.225+0.12, color='orange', alpha=1)

    # Plot Absorber Pads
    plt.fill_between([-30, -0.5], 0.135, 0.17, color='green', alpha=1, label='Readout Pads')
    plt.fill_between([0.5,30], 0.135, 0.17, color='green', alpha=1,)
    plt.fill_between([-30, -0.5], 1.055+0.12, 1.09+0.12, color='green', alpha=1)
    plt.fill_between([0.5, 30], 1.055+0.12, 1.09+0.12, color='green', alpha=1)

    # Plot Trace Line
    plt.fill_between([-5, 30], 0.595+0.06, 0.63+0.06, color='red', alpha=1, label='Transmission Line')

    # Plot Copper Shielding
    plt.fill_between([-2.5, 30], 0.47, 0.505, color='black', alpha=1, label='Ground')
    plt.fill_between([-2.5, 30], 0.72+0.12, 0.755+0.12, color='black', alpha=1)

    # Plot Signal Extraction Line
    plt.fill_between([-7.5,-5], 0.17, 1.055 + 0.12, color = 'purple', alpha = 1, label = 'Signal Extractor')

    # Set labels and title
    plt.ylabel('Y (mm)')
    plt.xlabel('X (mm)')
    plt.title("Transmission Extraction Layout")

    # Add legend outside the plot
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    # plt.gca().set_aspect('equal', adjustable='box')
    
    # Adjust layout to make room for the legend
    plt.tight_layout()

# Run the function to see the plot with the legend outside
FrontView()
plt.show()
