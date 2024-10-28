from itertools import permutations


def make_list(n):
    x = []
    for i in range(1,n+1):
        x.append(i)
    return x

def print_all_permutations(nums, show_permutations=True):
    # Generate all distinct permutations of the given list
    all_permutations = list(permutations(nums))

    # Optionally print each permutation
    if show_permutations:
        for perm in all_permutations:
            print("".join(map(str, perm)))

    # Print the total number of permutations
    print(f"Total number of permutations: {len(all_permutations)}")


conditions = 6
print_all_permutations(make_list(conditions))