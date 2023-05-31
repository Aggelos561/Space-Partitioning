import matplotlib.pyplot as plt


class Node:

    def __init__(self, point):
        self.point = point
        self.left = None
        self.right = None


class Kd_tree:

    def __init__(self, points):
        self.points = points
        self.root = None


    def __split_space(self, points):
        middle_index = self.__get_middle_index(points)
        return [points[:middle_index], points[middle_index+1:]]


    def __get_middle_index(self, points):
        return (len(points) - 1) // 2


    def __construct_space(self, space_points, depth):

        space_size = len(space_points)

        if space_size == 1:
            return Node(space_points[0])
        
        if not space_size:
            return None

        space_points.sort(key=lambda p: p[depth % 2])

        middle_index = self.__get_middle_index(space_points)
        
        node = Node(space_points[middle_index])
        
        left_points, right_points = self.__split_space(space_points)

        if (len(left_points)):
            node.left = self.__construct_space(left_points, depth+1)
        
        if (len(right_points)):
            node.right = self.__construct_space(right_points, depth+1)
        
        return node


    def __construct(self):

        if not len(self.points):
            return

        self.points.sort(key=lambda p: p[0])

        left_points, right_points = self.__split_space(self.points)

        self.root = Node(self.points[self.__get_middle_index(self.points)])
        self.root.left = self.__construct_space(left_points, 1)
        self.root.right = self.__construct_space(right_points, 1)


    def build(self):
        self.__construct()


    def search_rectangle(self, lower_left_p, upper_right_p):

        if self.root is None:
            return None

        points_inside = []
        self.__search_rect(self.root, lower_left_p, upper_right_p, points_inside, 0)
        return points_inside


    def __search_rect(self, node, lower_left_p, upper_right_p, points_inside, depth):
        
        if node is None:
            return

        x, y = node.point

        x_min, y_min = lower_left_p
        x_max, y_max = upper_right_p

        if x >= x_min and x_max >= x:
            if y >= y_min and y <= y_max:
                points_inside.append(node.point)

        if not depth % 2:
            if x >= x_min:
                self.__search_rect(node.left, lower_left_p, upper_right_p, points_inside, depth+1)
            if x <= x_max:
                self.__search_rect(node.right, lower_left_p, upper_right_p, points_inside, depth+1)
        else:
            if y >= y_min:
                self.__search_rect(node.left, lower_left_p, upper_right_p, points_inside, depth+1)
            if y <= y_max:
                self.__search_rect(node.right, lower_left_p, upper_right_p, points_inside, depth+1)


    def plot_rectangle(self, lower_left_p, upper_right_p, points_ins_rect):

        if not len(self.points):
            return
        
        fig, ax = plt.subplots()

        x = [point[0] for point in self.points]
        y = [point[1] for point in self.points]

        ax.scatter(x, y, color='blue')

        x_in_box = [point[0] for point in points_ins_rect]
        y_in_box = [point[1] for point in points_ins_rect]

        ax.scatter(x_in_box, y_in_box, color='red')

        width = upper_right_p[0] - lower_left_p[0]
        height = upper_right_p[1] - lower_left_p[1]

        rect = plt.Rectangle(lower_left_p, width, height, edgecolor='green', facecolor='none')
        ax.add_patch(rect)

        plt.show()



if __name__ == '__main__':

    from genpoints import gen_random_points
    
    # Search Inside Box Point Using KD-Tree

    # Generate 60 random points
    points = gen_random_points(60)

    kdtree = Kd_tree(points)

    # Building kd-tree
    kdtree.build()

    # Search in rectangle
    lower_left_p, upper_right_p = (30, 20), (70, 60)

    inside_rect = kdtree.search_rectangle(lower_left_p, upper_right_p)

    # Visualize rectangle
    kdtree.plot_rectangle(lower_left_p, upper_right_p, inside_rect)
