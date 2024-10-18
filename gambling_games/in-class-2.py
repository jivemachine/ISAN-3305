def create_arrays(num_arrays):
    arrays = []
    for i in range(num_arrays+1): # + 1 because dealer maybe?
        arrays.append([])
    return arrays





    # usability
    #print(arrays) # display all all arrays
    #print(arrays[0]) # array 0
    #print(arrays[1]) # ayyay 1


# def create_players(num_arrays):
#     players_dict = {}
#     for i in num_players:
#         name = i
#         players_dict[name] = 0
#     return players_dict


if __name__ == "__main__":
    num_arrays = int(input("How many arrays do you want to create? "))
    arrays = create_arrays(num_arrays)
    # players = create_players(num_arrays)
    # print(players)
    print(arrays)
    print(arrays[0])
    print(arrays[1])