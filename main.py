def main(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        # print(file_contents)
        count = len(file_contents.split())
        return count
    
    
def character_appearance(path_to_file):
    empty_dict = {}
    with open(path_to_file) as f:
        file_contents = f.read()
        for i in file_contents:
            # check in empty_dict if the key exists, if not create.
            if i in empty_dict:
                empty_dict[i] += 1
            else:
                empty_dict[i] = 1
    print(empty_dict)
        
    
# count = (main("books/frankenstein.txt"))
# print(count)

(character_appearance("books/frankenstein.txt"))