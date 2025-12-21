import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple


def generate_sales_data(
    months: int = 12,
    base_sales: float = 50000.0,
    volatility: float = 15000.0,
    seed: int = 42
) -> List[float]:
    """
    Generate random sales data for a specified number of months.

    Parameters:
    months (int): Number of months of data to generate.
    base_sales (float): Base sales value around which data fluctuates.
    volatility (float): Standard deviation of sales variations.
    seed (int): Random seed for reproducibility.

    Returns:
    List[float]: List of sales values for each month.
    """
    np.random.seed(seed)
    sales_data = np.random.normal(
        loc=base_sales,
        scale=volatility,
        size=months
    )
    # Ensure all sales values are positive
    return [max(value, 1000.0) for value in sales_data]


def create_cyberpunk_chart(
    sales_data: List[float],
    months: List[str]
) -> None:
    """
    Create and display a dark-themed cyberpunk neon line chart.

    Parameters:
    sales_data (List[float]): Sales values to plot.
    months (List[str]): Month labels for x-axis.

    Returns:
    None: Displays the plot directly.
    """
    # Set up the figure and axis with dark background
    fig, ax = plt.subplots(figsize=(14, 8), facecolor='#0a0e27')
    ax.set_facecolor('#0a0e27')

    # Plot the main line with neon cyan color
    x_values = np.arange(len(sales_data))
    line = ax.plot(
        x_values,
        sales_data,
        color='#00ffff',
        linewidth=3,
        label='Monthly Sales',
        marker='o',
        markersize=8,
        markerfacecolor='#ff006e',
        markeredgecolor='#00ffff',
        markeredgewidth=2
    )

    # Add a glowing effect with a thicker, semi-transparent line
    ax.plot(
        x_values,
        sales_data,
        color='#00ffff',
        linewidth=8,
        alpha=0.15,
        zorder=1
    )

    # Add gradient fill under the line for cyberpunk effect
    ax.fill_between(
        x_values,
        sales_data,
        alpha=0.2,
        color='#ff006e'
    )

    # Customize the axis
    ax.set_xlabel('Month', fontsize=14, color='#00ffff', fontweight='bold')
    ax.set_ylabel('Sales ($)', fontsize=14, color='#00ffff', fontweight='bold')
    ax.set_title(
        'CYBERPUNK SALES ANALYTICS',
        fontsize=18,
        color='#ff006e',
        fontweight='bold',
        pad=20
    )

    # Set x-axis with month labels
    ax.set_xticks(x_values)
    ax.set_xticklabels(months, color='#00ffff', fontsize=10)

    # Style the y-axis
    ax.tick_params(colors='#00ffff', labelsize=10)

    # Add cyberpunk grid
    ax.grid(True, color='#00ffff', alpha=0.2, linestyle='--', linewidth=1)
    ax.set_axisbelow(True)

    # Style the spines (axes borders)
    for spine in ax.spines.values():
        spine.set_edgecolor('#ff006e')
        spine.set_linewidth(2)

    # Add legend with neon styling
    legend = ax.legend(
        loc='upper left',
        fontsize=12,
        framealpha=0.9,
        facecolor='#0a0e27',
        edgecolor='#00ffff',
        labelcolor='#00ffff'
    )
    legend.get_frame().set_linewidth(2)

    # Add a futuristic annotation
    ax.text(
        0.98,
        0.02,
        '[SYSTEM ONLINE] • REAL-TIME MONITORING',
        transform=ax.transAxes,
        fontsize=10,
        color='#00ff00',
        ha='right',
        va='bottom',
        family='monospace',
        bbox=dict(
            boxstyle='round,pad=0.5',
            facecolor='#0a0e27',
            edgecolor='#00ff00',
            alpha=0.8
        )
    )

    # Adjust layout and display
    plt.tight_layout()
    plt.show()


def main() -> None:
    """
    Main function to generate sales data and create the visualization.

    Generates random sales data for 12 months and creates a cyberpunk-themed
    neon line chart with dark background and futuristic styling.
    """
    # Month labels
    months = [
        'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
        'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'
    ]

    # Generate sales data
    sales_data = generate_sales_data(
        months=12,
        base_sales=60000,
        volatility=18000
    )

    # Create and display the cyberpunk chart
    create_cyberpunk_chart(sales_data, months)


if __name__ == '__main__':
    main()
