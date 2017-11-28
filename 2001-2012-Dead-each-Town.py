"""Process Data How many people suicides each Town in [2001-2012]"""
import json
import pygal
with open('data.json') as test_data: #receive data

    data = json.load(test_data)
    city = {}
    remove_case = ["Total (All India)", "Total (States)", "Total (Uts)"]

    for year, posit in zip(range(2001, 2013), range(12)):
        for i in data:
            """edit year to find 2001-2012 and check requestment"""
            if  i["State"] not in remove_case and i["Age_group"] != "0-100+" and i["Year"] == year:
                """check in have it dict already or not"""
                if i["State"] in city:
                    city[i["State"]][posit] += i["Total"]

                else:
                    city[i["State"]] = [i["Total"], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    print("***Complete***")    #finish

    """show data process"""
    list_city = sorted(list(city))
    line_chart = pygal.Line(height=800, width=1000)
    line_chart.title = "2001-2012"
    line_chart.x_labels = map(str, range(2001, 2013))
    for i in list_city:
        line_chart.add(i, city[i])
        print(i, ":", city[i])
    line_chart.render_to_file('2001-2012.svg')
