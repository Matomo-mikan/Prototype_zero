def jaccard(set1, set2):
    # Create a set of intersection of A and B
    set_intersection = set.intersection(set(set1), set(set2))
    # Get the number of elements from A and B
    num_intersection = len(set_intersection)

    # Create set of sum of A and B
    set_union = set.union(set(set1), set(set2))
    # Get the number of elements from A and B
    num_union = len(set_union)

    # Calculate Jaccard by dibiding number of
    # first set by sets of sum
    try:
        return float(num_intersection) / num_union
    except ZeroDivisionError:
        return 1.0

if __name__== '__main__':
    set1 = ["Apple", "Banana", "strauberry","Melon", "Kiwi"] # Set A
    set2 = ["Melon", "Pineapple", "strawberry", "Apple", "Banana"] # Set B

    jaccard =  jaccard(set1, set2) # Calculate Jaccard
    print(jaccard)
