# import re
# import time
# from selenium import webdriver
# # 11 Cafes
# driver = webdriver.Chrome('./chromedriver')
# driver.get('https://mxcity.mx/2019/12/10-cafes-ideales-para-conocer-en-diciembre/')
# out_container = driver.find_elements_by_class_name('content_post')[0]
# container = out_container.find_element_by_tag_name("div")
# titles = [title.text for title in container.find_elements_by_tag_name("h2") if title.text != "" and title.text != " "]
# addresses = [address.text for address in container.find_elements_by_tag_name("p") if re.search("^Dónde:.*", address.text)]
# schedules = [schedule.text for schedule in container.find_elements_by_tag_name("p") if re.search("^Cuándo:.*", schedule.text)]
# costs = [cost.text for cost in container.find_elements_by_tag_name("p") if re.search("^Cuánto:.*", cost.text)]
# main_tuple_list = zip(titles[1:], addresses, schedules, costs)
# main_list = [{
#     "name": rest_tuple[0],
#     "address": rest_tuple[1],
#     "schedule": rest_tuple[2],
#     "cost": rest_tuple[3]
# } for rest_tuple in main_tuple_list]
# print(main_list)
# driver.quit()

import csv

with open('clean_startups.csv', 'r+') as csv_file:
    with open('eggs.csv', 'w', newline='') as output_csv_file:

        spamwriter = csv.writer(output_csv_file)
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0 or row[11] != '':
                print(f'Column names are {", ".join(row)}, {type(row[11])}')
                spamwriter.writerow([*row])
                line_count += 1
            else:
                print(f'\tURL :{row[4]}, is Self Funded: {row[11]}')
                row = row[:-1]
                is_self_funded = input('simon? ')
                spamwriter.writerow([*row, is_self_funded])
                line_count += 1
    print(f'Processed {line_count} lines.')

