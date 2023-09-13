US_countries = []
with open("US_available_countries.txt", "r") as us_file:
    for line in us_file:
        US_countries.append(line.strip())

ROK_countries = []
with open("ROK_available_countries.txt", "r") as rok_file:
    for line in rok_file:
        ROK_countries.append(line.strip())

with open("common_countries.txt", "w") as common_file:
    if(len(ROK_countries) < len(US_countries)):
        for country in ROK_countries:
            if(country in US_countries):
                common_file.write(country + '\n')
    else:
        for country in US_countries:
            if(country in ROK_countries):
                common_file.write(country + '\n')
        


    