"""
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака.
"""


def packing_backpack(goods, capacity):
    list_goods = []
    for i, j in goods.items():
        if j <= capacity:
            list_goods.append(i)
            capacity -= j
    return print(list_goods)


goods = {
    'bottle_of_water': 0.5,
    'matches': 0.01,
    'sleeping_bag': 1,
    'knife': 0.4,
    'folding_chair': 1.1,
    'raincoat': 0.7,
    'first_aid_kit': 0.5,
    'powerbank': 0.8,
    'flashlight': 0.3,
    'set_of_dishes': 0.4,
    'meal': 2.5,
}

backpack_capacity = 5.5

# var_1

packing_backpack(goods, backpack_capacity)

# var_2

sorted_goods = dict(sorted(goods.items(), key=lambda x: -x[1]))
packing_backpack(sorted_goods, backpack_capacity)
