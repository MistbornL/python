import os
def counter():
    List = []
    path = os.listdir('C:/Users/Lasha/OneDrive/სამუშაო დაფა/PY')

    for item in path:
        if ".jpeg" in item:
            List.append(item)
    return len(List)       