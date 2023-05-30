from scipy.spatial import KDTree

class Kd_tree():

    def __init__(self, points):
        self.points = points

    def build(self):
        self.kdtree = KDTree(points)

    def query(self, point):
        return self.kdtree.query(point)



if __name__ == '__main__':

    from helper import gen_random_points

    points = gen_random_points(20)

    kdtree = Kd_tree(points)

    kdtree.build()

    query_point = gen_random_points(1)[0]

    distance, index = kdtree.query(query_point)

    print(f'Query point: {query_point}')
    print(f'Nearest Neighbor: {points[index]}, distance: {distance}')
