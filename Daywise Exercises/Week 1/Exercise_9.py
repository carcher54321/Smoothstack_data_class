accounts = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]


def get_data(rows):
    def add_10_lt_100(t):
        addition = 10 if t[1] < 100 else 0
        return t[0], t[1] + addition
    data = map(lambda x: [x[0], x[2] * x[3]], rows)
    data = map(add_10_lt_100, data)
    return data


print(*get_data(accounts))
# Output: (34587, 163.8) (98762, 284.0) (77226, 108.85000000000001) (88112, 84.97)


other_accounts = [
    [34587, (12, 4, 40.95), (13, 5, 56.80)],
    [77226, (6, 3, 32.95), (7, 3, 24.99)]
]


def scrape_data(rows):
    def map_func(t):
        order_n = t[0]
        total = sum(map(lambda x: x[1] * x[2], t[1:]))
        return order_n, total
    return list(map(map_func, rows))


print(scrape_data(other_accounts))
# Output: [(34587, 447.8), (77226, 173.82)]
