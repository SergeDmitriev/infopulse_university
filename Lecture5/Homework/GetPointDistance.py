class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def dis_to_origin(self):
        from math import sqrt
        result = sqrt(self.x ** 2 + self.y ** 2)
        return result

    def convert_dmds_to_dd(self):
        lat_dd = -(self.x + 2 / 60 + 24 / 3600)
        lon_dd = -(self.y + 28 / 60 + 48 / 3600)
        return lat_dd, lon_dd

    def dis_to_point(self, second_point):
        from math import sqrt
        result = sqrt((second_point.x - self.x) ** 2 + (second_point.x - self.y) ** 2)
        return result



if __name__ == '__main__':
    p = Point(50, 70)
    p2 = Point(90, 70)

    print('Attributes:{0}, distance to 0,0 = {1}, distance to {2} = {3} DMS coordinates: {4}'
          .format(vars(p), p.dis_to_origin(), vars(p2), p.dis_to_point(p2), p.convert_dmds_to_dd()))
