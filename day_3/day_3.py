with open('day_3_input.txt', 'r') as slope:
	slope_map = []
	for line in slope:
		slope_map.append(line.strip('\n'))
	
	width = len(slope_map[0])
	end_of_slope = len(slope_map)
	idx = 0
	height = 0
	trees = 0

	while height < end_of_slope:
		trees += 1 if slope_map[height][idx % width] == '#' else 0
		height += 1
		idx += 3 



	print(trees)
