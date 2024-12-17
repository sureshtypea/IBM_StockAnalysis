# Install necessary libraries
!pip install pandas
!pip install plotly

# Import required libraries
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Define the make_graph function
def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        subplot_titles=("Historical Share Price", "Historical Revenue"),
        vertical_spacing=0.3
    )
    # Filter data up to June 2021 for stock and revenue
    stock_data_specific = stock_data[stock_data['Date'] <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data['Date'] <= '2021-04-30']

    # Add stock data trace
    fig.add_trace(
        go.Scatter(
            x=pd.to_datetime(stock_data_specific['Date'], infer_datetime_format=True),
            y=stock_data_specific['Close'].astype("float"),
            name="Share Price"
        ),
        row=1, col=1
    )

    # Add revenue data trace
    fig.add_trace(
        go.Scatter(
            x=pd.to_datetime(revenue_data_specific['Date'], infer_datetime_format=True),
            y=revenue_data_specific['Revenue'].astype("float"),
            name="Revenue"
        ),
        row=2, col=1
    )

    # Update layout
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(
        showlegend=False,
        height=900,
        title=stock,
        xaxis_rangeslider_visible=True
    )
    fig.show()

# Step 1: Replace with Full DataFrames for GameStop Stock and Revenue Data
# Assuming `gme_data` and `gme_revenue` were extracted in previous questions

# Example: Replace this with the actual full dataset for GameStop stock
gme_data = pd.DataFrame({
    "Date": ["2021-06-14", "2021-06-13", "2021-06-12", "2021-06-11", "2021-06-10"],
    "Close": [250, 240, 245, 230, 235]
})

# Example: Replace this with the actual full dataset for GameStop revenue
gme_revenue = pd.DataFrame({
    "Date": ["2021-04-30", "2021-03-31", "2021-02-28", "2020-12-31", "2020-09-30"],
    "Revenue": [5000, 5500, 5300, 5200, 5100]
})

# Convert the `Date` columns to datetime to ensure proper filtering
gme_data['Date'] = pd.to_datetime(gme_data['Date'])
gme_revenue['Date'] = pd.to_datetime(gme_revenue['Date'])

# Step 2: Call the make_graph function to plot the graph
make_graph(gme_data, gme_revenue, 'GameStop')
