global values
values = {}
def observe(int):   
    
    if ("count" in values):
        values["count"] += 1
    else:
        values.update({"count": 1})
    if int in values:
        values[int] += 1
    else:
        values.update({int: 1})
    return None

def probability_of(int):
    return values[int]/values["count"]

def reset():
    values.clear()




    