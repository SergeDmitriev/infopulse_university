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



if __name__ == '__main__':
    p = Point(50, 70)
    attr = vars(p)
    print('Attributes:{0}, distance: {1}, DMS coordinates: {2}'
          .format(attr, p.dis_to_origin(), p.convert_dmds_to_dd()))
