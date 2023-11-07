from sklearn.manifold import TSNE
from sklearn.cluster import DBSCAN
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource
import numpy as np
def create_bokeh_html(vectors, labels, out_file = "tsne_plot.html"):
    # Define custom colors for each cluster
    colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#aec7e8', '#ffbb78'
    ]

    # Initialize the t-SNE model with 2 components for 2D visualization
    tsne = TSNE(n_components=2, random_state=0)

    # Fit the model to your data
    vectors_2d = tsne.fit_transform(vectors)
    dbscan = DBSCAN(eps=1.8, min_samples=3)
    cluster_labels = dbscan.fit_predict(vectors_2d)


    # Prepare data for plotting
    source = ColumnDataSource(data=dict(
        x=vectors_2d[:, 0],
        y=vectors_2d[:, 1],
        desc0 =[lab[0] for lab in labels],
        desc1 =[lab[1] if len(lab)>1 else "" for lab in labels],
        desc2 =[lab[2] if len(lab)>2 else "" for lab in labels],
        colors=[colors[i%len(colors)] for i in cluster_labels]
    ))

    # Create a figure
    p = figure(tools="pan,box_zoom,reset,save")

    # Add data points to the figure
    p.circle('x', 'y', size=10, source=source,fill_color='colors')


    # Add hover tool
    hover = HoverTool(tooltips=
        """
        <b>Comment</b>: @desc0
        <br>
        @desc1
        <br>
        @desc2
        """
    )
    # hover = HoverTool(tooltips=[("Label", "@desc")])
    # hover = HoverTool(tooltips=[("Comment", "@desc{safe}")], point_policy='follow_mouse')
    # hover = HoverTool(tooltips=[("Label", "@desc{safe}")], width=300)
    p.add_tools(hover)

    # Save the plot as an HTML file
    output_file(out_file)
    show(p)