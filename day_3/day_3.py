with open('day_3_input.txt', 'r') as slope:
	slope_map = []
	paths = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
	for line in slope:
		slope_map.append(line.strip('\n'))
	
	def tree_count(slope_map, right, down):
		width = len(slope_map[0])
		end_of_slope = len(slope_map)
		idx = 0
		height = 0
		trees = 0

		while height < end_of_slope:
			trees += 1 if slope_map[height][idx % width] == '#' else 0
			height += down
			idx += right

		return trees

	def trees_aggregate(tree_counter, slope_map, paths_array):
		total_trees = tree_counter(slope_map, paths_array[0][0], paths_array[0][1])

		for idx in range(1, len(paths_array)):
			right = paths_array[idx][0]
			down = paths_array[idx][1]
			total_trees *= tree_counter(slope_map, right, down)

		return total_trees


	print(trees_aggregate(tree_count, slope_map, paths))
	# print(tree_count(slope_map, 3, 1))
