complete_fine_name_plus_path = input().split("\\")
complete_file_name = complete_fine_name_plus_path[-1]
filename, extension = complete_file_name.split(".")

print(f"File name: {filename}\nFile extension: {extension}")



