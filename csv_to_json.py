import csv
import json


def convert_csv_to_json(csv_path, json_path):
    with open(csv_path, 'r', encoding="ISO-8859-1") as csv_file:
        reader = csv.reader(csv_file)
        data = list()
        count = 1
        for row in reader:
            try:
                print(count)
                if count == 1:
                    header = row
                else:
                    if len(row) == len(header):
                        data.append(dict(zip(header, row)))
                count += 1

            except Exception as e:
                print(e.__class__)

    final_data = list()
    for doc in data:
        changed_doc = dict()
        final_dict = dict()

        for key, value in doc.items():
            if not value:
                value = None
            if key == 'ÿuniq_id':
                key = "uniq_id"
            elif key == "product_specifications" and value:
                value = value.replace("=>", ":")
            elif key == "is_FK_Advantage_product" and value:
                if value.lower() == "true":
                    value = True
                else:
                    value = False
            elif key == "product_rating":
                if not isinstance(value, float):
                    value = None
            elif key == "overall_rating":
                if not isinstance(value, float):
                    value = None
            try:
                value = json.loads(value)
            except Exception as e:
                pass
            changed_doc[key] = value
        final_dict["model"] = "Products.AllProducts"
        final_dict["pk"] = "uniq_id"
        final_dict["fields"] = changed_doc
        final_data.append(final_dict)

    with open(json_path, 'w') as json_file:
        json.dump(final_data, json_file, indent=4)


convert_csv_to_json("/Users/macbook/PycharmProjects/Django_Sample_Project/flipkart.csv",
                    "/Users/macbook/PycharmProjects/Django_Sample_Project/sample.json")
