input=[1,2,3,[4,[5,6]],[7]]

def flatten_list(input):
    lst = []
    for i in input:
        if type(i) is list:
            lst.extend(flatten_list(i))

        else:
            lst.append(i)
    return lst

print(flatten_list(input))