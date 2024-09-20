"""def calculate_distance(good_string, name):
    prev_good = 0
    total_distance = 0

    for char in name:
        if char in good_string:
            prev_good = char
            continue
        keys=[]
        closest_good_dict = {}
        closest_good = good_string[0]
        min_distance = abs(ord(char) - ord(closest_good))
        closest_good_dict[0] = good_string[0]

        for j in range(1, len(good_string)):
            current_distance = abs(ord(good_string[j]) - ord(char))

            if current_distance < min_distance:
                closest_good_dict.clear()
                closest_good_dict[j] = good_string[j]
                min_distance = current_distance
            elif current_distance == min_distance:
                 closest_good_dict[j] = good_string[j]
                 keys = closest_good_dict.keys()
        for k in range(len(keys)):
            if keys[k]-"""












def main():
    good_string = input("Enter the good string: ")
    name = input("Enter the name: ")

    total_distance = calculate_distance(good_string, name)
    print(f"The total distance for the given name is: {total_distance}")

if __name__ == "__main__":
    main()