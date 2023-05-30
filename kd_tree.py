from scipy.spatial import cKDTree


# Complexity O(nlogn)


class Kd_tree():

    def __init__(self, points):
        self.points = points

    def build(self):
        self.kdtree = cKDTree(points)

    def query(self, point):
        distance, index = self.kdtree.query(point)
        return distance, self.points[index]

    def search_rectangle(self, lower_left_p, upper_right_p):
        indices = self.kdtree.query_ball_point([lower_left_p, upper_right_p], r=1)
        points_in_rect = [self.points[index] for index_list in indices for index in index_list]
        return points_in_rect


if __name__ == '__main__':

    from helper import gen_random_points


    # Search Nearest Neighbor Point Using KD-Tree

    points = gen_random_points(50)

    kdtree = Kd_tree(points)

    kdtree.build()

    query_point = gen_random_points(1)[0]

    distance, nearest_point = kdtree.query(query_point)

    print(f'Query point: {query_point}')
    print(f'Nearest Neighbor: {nearest_point}, distance: {distance}\n')


    # Rectangle Search Using KD-Tree

    points = gen_random_points(60)

    kdtree = Kd_tree(points)

    kdtree.build()

    lower_left_p, upper_right_p = gen_random_points(2)

    points_ins_rect = kdtree.search_rectangle(lower_left_p, upper_right_p)

    print(f'Points inside rectangle: {points_ins_rect}')
