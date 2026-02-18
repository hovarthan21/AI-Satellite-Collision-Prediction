import plotly.graph_objects as go

sat_ids = list(satellites.keys())
xs = [satellites[s]['x'] for s in sat_ids]
ys = [satellites[s]['y'] for s in sat_ids]
zs = [satellites[s]['z'] for s in sat_ids]
colors = ['red' if satellites[s]['collision_prob']>0.5 else 'blue' for s in sat_ids]

fig = go.Figure(data=[go.Scatter3d(
    x=xs, y=ys, z=zs,
    mode='markers',
    marker=dict(size=4, color=colors)
)])
fig.update_layout(scene=dict(
    xaxis_title='X (km)',
    yaxis_title='Y (km)',
    zaxis_title='Z (km)'
))
fig.show()
