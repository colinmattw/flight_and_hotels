import matplotlib.pyplot as plt
import re
import csv

labels = []
price_dat_price_sheet = []
flight_dat_price_sheet = []
price_dat_time_sheet = []
flight_dat_time_sheet = []
time_file_lines = []
price_file_lines = []
with open('best_time_options.txt', 'r') as time_file:
    time_file_lines = time_file.readlines()
with open('best_price_options.txt', 'r') as price_file:
    price_file_lines = price_file.readlines()

for i in range(0, len(time_file_lines), 2):
    indy_line = time_file_lines[i]
    seoul_line = time_file_lines[i + 1]

    indy_price = re.search(r'\$\d{1,3}(?:,\d{3})*', indy_line)
    if(indy_price):
        indy_price = int(indy_price.group(0).replace('$', '').replace(',', ''))
        seoul_price = re.search(r'\$\d{1,3}(?:,\d{3})*', seoul_line)
        if(seoul_price):
            seoul_price = int(seoul_price.group(0).replace('$', '').replace(',', ''))
            the_price = (indy_price + seoul_price) / 2
            price_dat_time_sheet.append(the_price)
    
            indy_time_regex = re.search(r'(\d+)\s*hr\s*(\d+)\s*min|(\d+)\s*hr|(\d+)\s*min', indy_line)
            indy_time = 0
            if(indy_time_regex.group(1) is not None):
                indy_time += (int(indy_time_regex.group(1)) * 60)
            if(indy_time_regex.group(2) is not None):
                indy_time += (int(indy_time_regex.group(2)))
            if(indy_time_regex.group(3) is not None):
                indy_time += (int(indy_time_regex.group(3)) * 60)
            if(indy_time_regex.group(4) is not None):
                indy_time += (int(indy_time_regex.group(4)))
            indy_time = indy_time / 60

            seoul_time_regex = re.search(r'(\d+)\s*hr\s*(\d+)\s*min|(\d+)\s*hr|(\d+)\s*min', seoul_line)
            seoul_time = 0
            if(seoul_time_regex.group(1) is not None):
                seoul_time += (int(seoul_time_regex.group(1)) * 60)
            if(seoul_time_regex.group(2) is not None):
                seoul_time += (int(seoul_time_regex.group(2)))
            if(seoul_time_regex.group(3) is not None):
                seoul_time += (int(seoul_time_regex.group(3)) * 60)
            if(seoul_time_regex.group(4) is not None):
                seoul_time += (int(seoul_time_regex.group(4)))
            seoul_time = seoul_time / 60

            if(indy_time > seoul_time):
                flight_dat_time_sheet.append(indy_time)
            else:
                flight_dat_time_sheet.append(seoul_time)
            labels.append(indy_line.split(',')[1] + ', ' + indy_line.split(',')[2])

for i in range(0, len(price_file_lines), 2):
    indy_line = price_file_lines[i]
    seoul_line = price_file_lines[i + 1]

    if(indy_line.split(',')[1] == ' Tokyo'):
        print('Tokyo')

    indy_price = re.search(r'\$\d{1,3}(?:,\d{3})*', indy_line)
    if(indy_price):
        indy_price = int(indy_price.group(0).replace('$', '').replace(',', ''))
        seoul_price = re.search(r'\$\d{1,3}(?:,\d{3})*', seoul_line)
        if(seoul_price):
            seoul_price = int(seoul_price.group(0).replace('$', '').replace(',', ''))
            the_price = (indy_price + seoul_price) / 2
            price_dat_price_sheet.append(the_price)
        
            indy_time_regex = re.search(r'(\d+)\s*hr\s*(\d+)\s*min|(\d+)\s*hr|(\d+)\s*min', indy_line)
            indy_time = 0
            if(indy_time_regex.group(1) is not None):
                indy_time += (int(indy_time_regex.group(1)) * 60)
            if(indy_time_regex.group(2) is not None):
                indy_time += (int(indy_time_regex.group(2)))
            if(indy_time_regex.group(3) is not None):
                indy_time += (int(indy_time_regex.group(3)) * 60)
            if(indy_time_regex.group(4) is not None):
                indy_time += (int(indy_time_regex.group(4)))
            indy_time = indy_time / 60

            seoul_time_regex = re.search(r'(\d+)\s*hr\s*(\d+)\s*min|(\d+)\s*hr|(\d+)\s*min', seoul_line)
            seoul_time = 0
            if(seoul_time_regex.group(1) is not None):
                seoul_time += (int(seoul_time_regex.group(1)) * 60)
            if(seoul_time_regex.group(2) is not None):
                seoul_time += (int(seoul_time_regex.group(2)))
            if(seoul_time_regex.group(3) is not None):
                seoul_time += (int(seoul_time_regex.group(3)) * 60)
            if(seoul_time_regex.group(4) is not None):
                seoul_time += (int(seoul_time_regex.group(4)))
            seoul_time = seoul_time / 60

            if(indy_time > seoul_time):
                flight_dat_price_sheet.append(indy_time)
            else:
                flight_dat_price_sheet.append(seoul_time)


flight_time_super_list = []
best_price_super_list = []
for i in range(len(labels)):
    flight_time_super_list.append((labels[i], price_dat_time_sheet[i], flight_dat_time_sheet[i]))
    best_price_super_list.append((labels[i], price_dat_price_sheet[i], flight_dat_price_sheet[i]))


with open('flight_time_list.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Destination', 'Price Per Person', 'Longest Flight'])
    for i in range(len(flight_time_super_list)):
        csv_writer.writerow([flight_time_super_list[i][0], flight_time_super_list[i][1], flight_time_super_list[i][2]])

with open('best_price_list.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Destination', 'Price Per Person', 'Longest Flight'])
    for i in range(len(best_price_super_list)):
        csv_writer.writerow([best_price_super_list[i][0], best_price_super_list[i][1], best_price_super_list[i][2]])


# Create a scatter plot (dot plot)
plt.scatter(flight_dat_price_sheet, price_dat_price_sheet, label='Best Price Destinations', color='blue', marker='o')

for i, label in enumerate(labels):
    plt.text(flight_dat_price_sheet[i], price_dat_price_sheet[i], label, fontsize=5, ha='center', va='top')

# Add labels and a title
plt.xlabel('Time to Destination')
plt.ylabel('Cost Per Person')
plt.title('Dot Plot Example')

# Show legend (optional)
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
