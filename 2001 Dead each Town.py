"""Process Data How many people suicides each Town in [2001]"""
import json
with open('data.json') as test_data: #receive data

    data = json.load(test_data)
    city = {}
    remove_case = ["Total (All India)", "Total (States)", "Total (Uts)"]

    for i in data:
        """edit year to find 2001-2012 and check requestment"""
        if  i["State"] not in remove_case and i["Type_code"] == "Causes" and i["Year"] == 2001:
            """check in have it dict already or not"""
            if i["State"] in city:
                city[i["State"]] += i["Total"]

            else:
                city[i["State"]] = i["Total"]

        print("Processing")    #check it runing or not

    print("***Complete***")    #finish

    """show data process"""
    list_city = sorted(list(city))

    for i in list_city:
        print("%s : %d" %(i, city[i]))
