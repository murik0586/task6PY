import re


def validate_car_number(car_id):

    pattern = r'^([АВЕКМНОРСТУХ])(\d{3})([АВЕКМНОРСТУХ]{2})(\d{2,3})$'

    match = re.match(pattern, car_id)
    if match:

        full_number = f"{match[1]}{match[2]}{match[3]}"
        region = match[4]
        return f"Номер {full_number} валиден. Регион: {region}."
    else:
        return "Номер не валиден."



print(validate_car_number('А222ВС96'))
print(validate_car_number('АБ22ВВ193'))
print(validate_car_number('Е123КХ77'))  
