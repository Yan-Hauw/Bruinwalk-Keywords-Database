import csv

# constants
from constants.test_data import test_results


# def convert_to_loadfile(results_by_course):


results_by_course = test_results

f = open("scraper_data.csv", "w", newline="")

writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)

for data_of_class in results_by_course:

    for class_instance_by_prof in data_of_class:
        course_name = class_instance_by_prof[0]

        lecturer = class_instance_by_prof[1]

        row = []

        row.append(course_name)
        row.append(lecturer)

        keywords_dict = class_instance_by_prof[2]

        for occurence in keywords_dict.values():
            occurence = occurence

            row.append(occurence)

        print(row)

        writer.writerow(row)

f.close()
