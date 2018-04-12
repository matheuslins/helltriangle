import random


class HellTriangle(object):

    def __call__(self, triangle_size):
        self.triangle_size = int(triangle_size)
        self.build_triangle_random

    @property
    def build_triangle_random(self):
        triangle = []
        size_t = self.triangle_size + 1
        for t_subSize in range(1, size_t):
            subTriangle = []
            for item in range(t_subSize):
                subTriangle.append(random.randint(0, 9))
            triangle.append(subTriangle)
        print(f"You Triangle is: {triangle}")
        return self.summed_triangle(triangle)

    def summed_triangle(self, trianlge, test=False):
        items = []
        for idx, row_list in enumerate(trianlge):
            if idx == 0:
                items.append(row_list[0])
            else:
                dad_idx = idx - 1
                items.append(max(row_list[dad_idx], row_list[idx]))
        summed = sum(items)
        print (f"The sum is: {summed}")
        if test:
            return summed


