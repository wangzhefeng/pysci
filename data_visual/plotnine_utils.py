import plotly.graph_objects as go



def scatter_3d_plot(df):
    fig = go.Figure(data=[go.Scatter3d(
        x = df_0907["eturb_m1_steam_flow_in"],
        y = df_0907["eturb_m1_steam_flow_side"],
        z = df_0907["eturb_m1_electricity_generation"],
        mode = 'markers',
        marker = dict(
            size = 3,
            # color=z,                # set color to an array/list of desired values
            # colorscale='Viridis',   # choose a colorscale
            opacity = 0.8
        )
    )])

    # tight layout
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    fig.show()