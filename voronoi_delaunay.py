import matplotlib.pyplot as plt
from scipy.spatial import Delaunay, Voronoi, voronoi_plot_2d
from helper import gen_random_points


points = gen_random_points(20)

x = [point[0] for point in points]
y = [point[1] for point in points]

delaunay_res = Delaunay(points)

voronoi = Voronoi(points)

fig, ax = plt.subplots()

ax.scatter(x, y)

voronoi_plot_2d(voronoi, ax=ax, show_vertices=False, line_colors='b', line_width=1)

ax.triplot(x, y, delaunay_res.simplices, color ='red')

ax.set_title('Voronoi Diagram and Delaunay Triangulation')

plt.show()
