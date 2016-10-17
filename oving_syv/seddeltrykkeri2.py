__author__ = "Morten Bujordet"


from sys import stdin


widths = []
heights = []
values = []
for triple in stdin.readline().split():
    dim_value = triple.split(':', 1)
    dim = dim_value[0].split('x', 1)
    width = int(dim[0][1:])
    height = int(dim[1][:-1])
    value = int(dim_value[1])
    widths.append(int(width))
    heights.append(int(height))
    values.append(int(value))
for line in stdin:
    paper_width, paper_height = [int(x) for x in line.split('x', 1)]
    result = [None] * (paper_width + 1)
    for w in range(paper_width + 1):
        result[w] = [-1] * (paper_height + 1)
    for x in range(len(values)):
        if widths[x] <= paper_width and heights[x] <= paper_height and result[widths[x]][heights[x]] < values[x]:
            result[widths[x]][heights[x]] = values[x]
        if heights[x] <= paper_width and widths[x] <= paper_height and result[heights[x]][widths[x]] < values[x]:
            result[heights[x]][widths[x]] = values[x]
    # Calculate the other entries
    for w in range(paper_width + 1):
        for h in range(paper_height + 1):
            if result[w][h] == 0:
                continue
            if result[w][h] == -1:
                best = 0
            else:
                best = result[w][h]
            for cutWidth in range(1, w):
                if best < result[cutWidth][h] + result[w - cutWidth][h]:
                    best = result[cutWidth][h] + result[w - cutWidth][h]
            for cutHeight in range(1, h):
                if best < result[w][cutHeight] + result[w][h - cutHeight]:
                    best = result[w][cutHeight] + result[w][h - cutHeight]
            result[w][h] = best
    print(result[paper_width][paper_height])