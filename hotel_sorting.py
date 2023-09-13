import csv

flight_cities = []
with open('best_price_list.csv', 'r') as flight_file:
    reader = csv.reader(flight_file)
    for row in reader:
        flight_cities.append(row)

hotel_cities =[]
with open('city_avg_hotel_price_copy.csv', 'r+') as hotel_file:
    reader = csv.reader(hotel_file)
    for row in reader:
        hotel_cities.append(row)
    writer = csv.writer(hotel_file)
    hotel_file.seek(0)
    for hotel in hotel_cities:
        for flight in flight_cities:
            if(hotel[0].split(',')[0] == flight[0].replace(' ', '').split(',')[0]):
                writer.writerow(hotel)
    hotel_file.truncate()