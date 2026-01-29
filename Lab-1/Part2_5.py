import json
import timeit

with open("large-file.json","r", encoding="utf-8") as file:
    data = json.load(file)

def compute_size():
    for record in data:
        if "size" in record:
            record["size"] = 42

data.reverse()

with open("output.2.3.json", "w", encoding="utf-8") as out:
    json.dump(data, out, indent=4)


runs = 10
total_time = timeit.timeit(compute_size, number=runs)
avg_time = total_time / runs

print("Average execution time over", runs, "runs:", avg_time, "seconds")