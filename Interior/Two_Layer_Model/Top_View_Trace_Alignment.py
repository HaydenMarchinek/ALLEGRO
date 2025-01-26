import matplotlib.pyplot as plt

def TopView():
    plt.figure()  # Create a new figure for the side view

    # Plot High Voltage Plane
    plt.fill_between([-30.6, -0.6], 0, 0.01, color='orange', alpha=1, label='High Voltage Pads')
    plt.fill_between([0, 30], 0, 0.01, color='orange', alpha=1)
    plt.fill_between([30.6, 45], 0, 0.01, color='orange', alpha=1)
    plt.fill_between([-30.6, -0.6], 1.29, 1.3, color='orange', alpha=1)
    plt.fill_between([0, 30], 1.29, 1.3, color='orange', alpha=1)
    plt.fill_between([30.6, 45.6], 1.29, 1.3, color='orange', alpha=1)

    # Plot Absorber Pads
    plt.fill_between([-30.6, -0.6], 0.11, 0.12, color='green', alpha=1, label='Readout Pads')
    plt.fill_between([0, 30], 0.11, 0.12, color='green', alpha=1)
    plt.fill_between([30.6, 45.6], 0.11, 0.12, color='green', alpha=1)
    plt.fill_between([0, 30], 1.18, 1.19, color='green', alpha=1)
    plt.fill_between([-30.6, -0.6], 1.18, 1.19, color='green', alpha=1)
    plt.fill_between([30.6, 45.6], 1.18, 1.19, color='green', alpha=1)

    # Plot Copper Flooding
    plt.fill_between([-4.5, 23.5], 0.645, 0.655, color='black', alpha=1)
    plt.fill_between([-30.6, -7.8], 0.645, 0.655, color='black', alpha=1)
    plt.fill_between([26.7, 45.6], 0.645, 0.655, color='black', alpha=1)

    # Plot Traces
    plt.fill_between([-5.6, 45.6], 0.370, 0.380, color='red', alpha=1, label='Transmission Line')
    plt.fill_between([25.6, 45.6], 0.92, 0.93, color='blue', alpha=1, label='Transmission Line')

    # Plot Copper Shielding
    plt.fill_between([-3, 45.6], 0.47, 0.48, color='black', alpha=1, label='Ground')
    plt.fill_between([-3, 45.6], 0.27, 0.28, color='black', alpha=1)
    plt.fill_between([28.1, 45.6], 1.02, 1.03, color='black', alpha=1)
    plt.fill_between([28.1, 45.6], 0.82, 0.83, color='black', alpha=1)

    # Plot Signal Extractor
    plt.fill_between([24.6, 25.6], 0.12, 1.18, color='purple', alpha=1, label='Signal Extractor')
    plt.fill_between([-6.6, -5.6], 0.12, 1.18, color='purple', alpha=1)

    # Set labels and title
    plt.ylabel('Y (mm)')
    plt.xlabel('X (mm)')
    plt.title("Side View")
    
    # Add legend outside of the plot
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    # Adjust layout to make room for the legend
    plt.tight_layout()

# Run the function to see the plot with the legend outside
TopView()
plt.show()
