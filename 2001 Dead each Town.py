"""Process Data How many people suicides each Town in [2001]"""
import json
import pygal
with open('data.json') as test_data: #receive data

    data = json.load(test_data)
    city = {}
    remove_case = ["Total (All India)", "Total (States)", "Total (Uts)"]

    for i in data:
        """edit year to find 2001-2012 and check requestment"""
        if  i["State"] not in remove_case and i["Age_group"] != "0-100+" and i["Year"] == 2001:
            """check in have it dict already or not"""
            if i["State"] in city:
                city[i["State"]] += i["Total"]

            else:
                city[i["State"]] = i["Total"]

    print("***Complete***")    #finish

    """show data process"""
    list_city = sorted(list(city))
    line_chart = pygal.HorizontalBar(height=800, width=1000)
    line_chart.title = "2001"
    for i in list_city:
        line_chart.add(i, city[i])
        print("%s : %d" %(i, city[i]))
    line_chart.render_to_file('2001.svg')
