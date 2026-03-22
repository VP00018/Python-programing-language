def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country = 91, area = 966, first =500 , last = 6630)

print(phone_num)