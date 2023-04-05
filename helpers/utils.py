import random


def generate_random_string(prefix='', length=7, special_chars=False):
    special_characters = list("¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÂÃÄÆÇÉÊÎÏÐÑÖ×ØÜÝÞßàáäæçèêëìîïðñö÷ûüþÿ!#$%&'()*+,-./:;"
                              "<=>@[\]^_`{|}~,.;:你好世界ПриветñԲարեւহ্যালোس لabCD1234")
    if special_chars:
        return prefix + (''.join(random.choice(special_characters) for _ in range(length)))
    else:
        random_int = random.random()
        unique_int = str(random_int)[-length:]
        return prefix + unique_int


def generate_random_credentials():
    username = generate_random_string(prefix='Anna', length=3)
    email = f"{generate_random_string(prefix='hidav', length=5)}@soflex.com"
    password = generate_random_string(length=10, special_chars=True)
    return {'username': username, 'email': email, 'password': password}
