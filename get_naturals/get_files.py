def get_data_from_file(input_file):
	result = [ ]
	input_file = open(input_file, "r").read().split("\n")
	for n in range(0, len(input_file)-1):
		result_line = []
		input_line = input_file[n].split(",")
		result_line.append(input_line[0])
		result_line.append(input_line[1])
		result_line.append(float(input_line[2]))
		result_line.append(float(input_line[3]))
		result_line.append(float(input_line[4]))
		result_line.append(input_line[5])
		result_line.append(float(input_line[6]))
		result.append(result_line)
	return result
