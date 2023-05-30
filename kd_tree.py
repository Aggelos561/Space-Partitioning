from scipy.spatial import cKDTree
import matplotlib.pyplot as plt
import numpy as np

# Complexity O(nlogn)


class Kd_tree():

    def __init__(self, points):
        self.points = points

    def build(self):
        self.kdtree = cKDTree(self.points)

    def query(self, point):
        distance, index = self.kdtree.query(point)
        return distance, self.points[index]

    def search_rectangle(self, lower_left_p, upper_right_p):

        rect_tree = cKDTree([lower_left_p, upper_right_p])

        indices = self.kdtree.query_ball_tree(rect_tree, r=float('inf'))

        flattened_indices = [index for sublist in indices for index in sublist]

        points_within_rectangle = [self.points[index] for index in flattened_indices]

        return points_within_rectangle
    
    
    def plot_rectangle(self, lower_left_p, upper_right_p, points_ins_rect):
        fig, ax = plt.subplots()

        x, y = zip(*self.points)
        ax.scatter(x, y, color='blue')

        x_in_box, y_in_box = zip(*points_ins_rect)
        ax.scatter(x_in_box, y_in_box, color='red')

        width = upper_right_p[0] - lower_left_p[0]
        height = upper_right_p[1] - lower_left_p[1]

        rect = plt.Rectangle(lower_left_p, width, height, edgecolor='green', facecolor='none')
        ax.add_patch(rect)

        plt.show()



if __name__ == '__main__':

    from helper import gen_random_points
    

    # Search Nearest Neighbor Point Using KD-Tree

    # points = gen_random_points(50)

    # kdtree = Kd_tree(points)

    # kdtree.build()

    # query_point = gen_random_points(1)[0]

    # distance, nearest_point = kdtree.query(query_point)

    # print(f'Query point: {query_point}')
    # print(f'Nearest Neighbor: {nearest_point}, distance: {distance}\n')


    # Rectangle Search Using KD-Tree

    points = gen_random_points(60)

    kdtree = Kd_tree(points)

    kdtree.build()

    lower_left_p, upper_right_p = gen_random_points(2)
    print(lower_left_p, upper_right_p)
    points_ins_rect = kdtree.search_rectangle(lower_left_p, upper_right_p)

    print(f'Points inside rectangle: {points_ins_rect}')

    kdtree.plot_rectangle(lower_left_p, upper_right_p, points_ins_rect)
