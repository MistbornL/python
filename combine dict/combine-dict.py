source1 = {"A": 1, "B": 2, "C": 3}
source2 = {"A": 4, "D": 5}


def combine(source1, source2):
    try:
        for i in source1:
            for b in source2:
                if i == b:
                    source1[i] = [source1[i], source2[b]]
                for i in source1:
                    for b in source2:
                        if b not in source1:
                            source2.update(source1)
                            return source2
    except:
        pass


print(f"We Have Two Dict {source1} and {source2}")
print(f"Combine: {combine(source1, source2)}")
