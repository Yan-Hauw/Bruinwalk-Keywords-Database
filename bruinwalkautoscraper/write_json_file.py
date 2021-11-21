import json
import re


def write_json_file(class_data, dept_keyword, class_number):
    filename = dept_keyword + class_number + ".json"

    filename = re.sub(r"[ ]", "", filename)

    f = open(filename, "w")

    for t in class_data:
        instructor_name, keywords = t[0], t[1]
        x = {"instructor": instructor_name, "keywordOccurrences": keywords}
        f.write(json.dumps(x) + "\n")
