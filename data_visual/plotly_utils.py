import plotly.graph_objects as go
import plotly.express as px


def scatter_3d_plot(df, x, y, z):
    fig = go.Figure(
        data = [
            go.Scatter3d(
                x = df["eturb_m1_steam_flow_in"],
                y = df["eturb_m1_steam_flow_side"],
                z = df["eturb_m1_electricity_generation"],
                mode = 'markers',
                marker = dict(
                    size = 3,
                    # color=z,                # set color to an array/list of desired values
                    # colorscale='Viridis',   # choose a colorscale
                    opacity = 0.8
                )
            )
        ]
    )
    # tight layout
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    fig.show()


def scatter_3d_plot(df, x, y, z):
    fig = plt.figure(figsize = (20, 8))
    # Plotly Express
    fig = px.scatter_3d(
        df, 
        x = x, 
        y = y, 
        z = z
    )
    # tight layout
    fig.update_layout(margin = dict(l = 3, r = 3, b = 3, t = 3))
    fig.show()