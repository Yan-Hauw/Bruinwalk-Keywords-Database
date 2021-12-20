# constants
from constants.scraping_keywords import scraping_keywords
from constants.test_data import test_results


# def convert_to_loadfile(results_by_course):


results_by_course = test_results


load_fp = open("ComputerScience.del", "w")

for data_of_class in results_by_course:

    for class_instance_by_prof in data_of_class:
        course_name = '"' + class_instance_by_prof[0] + '"'

        lecturer = ',"' + class_instance_by_prof[1] + '"'

        load_fp.write(course_name + lecturer)

        keywords_dict = class_instance_by_prof[2]

        for occurence in keywords_dict.values():
            occurence = str(occurence)

            load_fp.write("," + occurence)

        load_fp.write("\n")
