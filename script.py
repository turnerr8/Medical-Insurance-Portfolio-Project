import csv

dataset = []
with open("insurance.csv", newline="") as file:
    csv_file = csv.DictReader(file)
    for line in csv_file:
        dataset.append(line)

print(dataset[0]["age"])


def find_average_age(dataset):
    age_sum = 0
    num_ages = len(dataset)
    for item in dataset:
        age_sum += int(item["age"])
    return round(age_sum / num_ages)


avg_age = find_average_age(dataset)
print("Average age in dataset is {}".format(avg_age))


def regions_ranked(dataset):
    ranked = {}
    for item in dataset:
        if item["region"] in ranked:
            ranked[item["region"]] += 1
        else:
            ranked[item["region"]] = 1
    sorted_ranked = sorted(ranked.items(), key=lambda x: x[1], reverse=True)
    return sorted_ranked


ranked_areas = regions_ranked(dataset)
for i in range(len(ranked_areas)):
    print("{}: {} with {} users.".format(i + 1, ranked_areas[i][0], ranked_areas[i][1]))


# find avg cost for smokers, non smokers and the difference
def find_smokers(dataset):
    smokers_total_cost = 0
    smoker_count = 0
    non_smoker_cost = 0
    non_smoker_count = 0
    for item in dataset:
        if item["smoker"] == "no":
            non_smoker_cost += round(float(item["charges"]), 3)
            non_smoker_count += 1
        else:
            smokers_total_cost += round(float(item["charges"]), 3)
            smoker_count += 1
    return round(smokers_total_cost / smoker_count, 2), round(
        non_smoker_cost / non_smoker_count, 2
    )


smoker_avg, non_smoker_avg = find_smokers(dataset)


print(
    "The avg total for smokers is {}.\nThe avg total for non-smokers is {}.\nOn average, smokers pay ${} more.".format(
        smoker_avg, non_smoker_avg, round(smoker_avg - non_smoker_avg, 2)
    )
)
