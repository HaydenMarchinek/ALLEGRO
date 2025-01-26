import matplotlib.pyplot as plt

def FrontView():
    plt.figure() 

    # Plot High Voltage
    plt.fill_between([-2, 2], 0, 0.035, color='orange', alpha=1, label='High Voltage Pads')
    plt.fill_between([-2, 2], 2.11 - 0.67+0.24, 2.145 - 0.67+0.24, color='orange', alpha=1)

    # Plot Absorber Pads
    plt.fill_between([-2, 2], 0.135, 0.17, color='green', alpha=1, label='Readout Pads')
    plt.fill_between([-2, 2], 1.975 - 0.67+0.24, 2.010 - 0.67+0.24, color='green', alpha=1)

    # Plot Copper Flooding
    plt.fill_between([-2, 2], 0.72+0.12, 0.755+0.12, color='black', alpha=1)

    # Plot Traces
    plt.fill_between([0.4425, 0.5325], 0.595+0.06, 0.63+0.06, color='red', alpha=1, label='Transmission Line')
    plt.fill_between([-0.4425, -0.5325], 1.515 - 0.67+0.18, 1.55 - 0.67+0.18, color='blue', alpha=1, label='Transmission Line')

    # Plot Copper Shielding
    plt.fill_between([0.3975, 0.5775], 0.47, 0.505, color='black', alpha=1, label='Ground')
    plt.fill_between([-0.3975, -0.5775], 1.64 - 0.67+0.24, 1.675 - 0.67+0.24, color='black', alpha=1)

    # Plot Traces 2
    plt.fill_between([0.4425 - 2 * 0.975, 0.5375 - 2 * 0.975], 0.595+0.06, 0.63+0.06, color='red', alpha=1)
    plt.fill_between([-0.4425 + 2 * 0.975, -0.5375 + 2 * 0.975], 1.515 - 0.67+0.18, 1.55 - 0.67+0.18, color='blue', alpha=1)

    # Plot Copper Shielding 2
    plt.fill_between([0.3975 - 2 * 0.975, 0.5775 - 2 * 0.975], 0.47, 0.505, color='black', alpha=1)
    plt.fill_between([-0.3975 + 2 * 0.975, -0.5775 + 2 * 0.975], 1.64 - 0.67+0.24, 1.675 - 0.67+0.24, color='black', alpha=1)

    # Plot Lateral Shielding
    plt.fill_between([-0.4425, -0.5325], 0.595+0.06, 0.63+0.06, color='black', alpha=1)
    plt.fill_between([0.4425, 0.5325], 1.515 - 0.67+0.18, 1.55 - 0.67+0.18, color='black', alpha=1)
    plt.fill_between([-0.4425 + 2 * 0.975, -0.5325 + 2 * 0.975], 0.595+0.06, 0.63+0.06, color='black', alpha=1)
    plt.fill_between([0.4425 - 2 * 0.975, 0.5325 - 2 * 0.975], 1.515 - 0.67+0.18, 1.55 - 0.67+0.18, color='black', alpha=1)

    # Set labels and title
    plt.ylabel('Y (mm)')
    plt.xlabel('X (mm)')
    plt.title("Front View")
    plt.gca().set_aspect('equal', adjustable='box')
    # Add legend outside the plot
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # Adjust layout to make room for the legend
    plt.tight_layout()

# Run the function to see the plot with the legend outside
FrontView()
plt.show()

