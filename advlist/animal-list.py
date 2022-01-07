#!/usr/bin/env python3

def main():
    animal_list = ["cat", "dog", "fly", "cow", "fox"]
    animal_name = ["mew", "Leo", "Tom"]
    animal_list.extend(animal_name)
    print(animal_list)
if __name__ == "__main__":
    main()
