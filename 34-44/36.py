n = int(input())
people_list = [i for i in range(1, n + 1)]
def close(pp_list, ordinal_numbers):
    if len(pp_list) == 1:
        return pp_list[0]
    remove_index = (ordinal_numbers + 2) % len(pp_list)
    pp_list.pop(remove_index)
    return close(pp_list, remove_index)
print(f"剩下的人的编号{close(people_list, 0)}")