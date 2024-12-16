def main(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        # print(file_contents)
        count = len(file_contents.split())
        return count
    
    
def character_appearance(path_to_file):
    empty_dict = {}
    with open(path_to_file) as f:
        file_contents = f.read().lower()
        for i in file_contents:
            # check in empty_dict if the key exists, if not create.
            if i in empty_dict:
                empty_dict[i] += 1
            else:
                empty_dict[i] = 1
    return(empty_dict)
        
print("--- Begin report of books/frankenstein.txt ---")
count = (main("books/frankenstein.txt"))
print(f"{count} words found in the document")

results = (character_appearance("books/frankenstein.txt"))
for key, values in results.items():
    print(f"the {key} character was found {values} times")