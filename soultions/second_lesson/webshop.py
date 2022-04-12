class User:

    def __init__(self, username, email, title):
        self.username = username
        self.email = email
        self.title = title
        self.basket = {}

    def __str__(self):
        return f'{self.username};{self.email};{self.title}'

    def add_product(self, product):
        if product.product_id not in self.basket.keys():
            self.basket[product.product_id] = 1
        else:
            self.basket[product.product_id] += 1


class Product:
    def __init__(self, product_id, name):
        self.product_id = product_id
        self.name = name


def read_users_from_file(path):
    f = open(path, "r", encoding="UTF-8")
    user_list = []
    for user_line in f:
        temp = user_line.strip().split(";")
        user_list.append(User(temp[0], temp[1], temp[2]))
    return user_list


def find_users_by_title(users, title):
    return [item.username for item in users if item.title == title]


def is_there_username_twice(users):
    return len({item.username for item in users}) != len(users)


def group_users_by_title(users):
    my_dict = {}
    for item in users:
        if item.title not in my_dict.keys():
            my_dict[item.title] = 0
        my_dict[item.title] += 1
    return my_dict


def orders_of_normal_users(users):
    result_dict = {}
    for item in users:
        if item.title == "normal_user":
            for k, v in item.basket.items():
                if k not in result_dict.keys():
                    result_dict[k] = 0
                result_dict[k] += v
    return result_dict


def ordered_more_than(users, prod_id, amount):
    result_user_names = []
    for item in users:
        if prod_id in item.basket.keys() and item.basket[prod_id] > amount:
            result_user_names.append(item.username)
    return result_user_names


if __name__ == '__main__':
    my_users = read_users_from_file("users.csv")
    print(f'A beolvasott felhasználók: ')
    for user in my_users:
        print(f'{user}')

    title_in = input("Kérek egy jogosultságot:")
    print(f'Felhasználók ezzel a jogosultsággal: {find_users_by_title(my_users, title_in)}')

    if is_there_username_twice(my_users):
        print('Van user ami kétszer szerepel')
    else:
        print('Nincs user ami kétszer szerepel')

    print(f'Jogosultságonként a felhasználók:{group_users_by_title(my_users)}')

    my_users[1].add_product(Product(2, "Milk"))
    my_users[1].add_product(Product(2, "Milk"))
    my_users[1].add_product(Product(1, "Butter"))
    my_users[5].add_product(Product(2, "Milk"))
    my_users[5].add_product(Product(3, "Choclate"))

    print(f'Rendelések: {orders_of_normal_users(my_users)}')
    print(f'Többet rendeltek: {ordered_more_than(my_users,2,1)}')