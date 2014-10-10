def reduce_file_path(path):
	path = path.split("/")
	folder_list = []
	for i, item in enumerate(path):
		if item == ".." and len(folder_list) > 0:
			folder_list.pop()
		if item != ".." and item != "." and item != "":
			folder_list.append(item)

	result = "/" + "/".join(folder_list)

	return result