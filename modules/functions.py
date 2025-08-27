def print_todos(todos_lst):
    for i, item in enumerate(todos_lst):
        print(f"{i}.{item.strip('\n')}")


def write_todos(todos_list, filename='files/todos.txt'):
    with open(filename, 'w') as file:
        file.writelines(todos_list)


def read_todos(filename='files/todos.txt'):
    with open(filename, 'r') as file:
        return file.readlines()

if __name__ == "__main__":
    print_todos(read_todos("../files/todos.txt"))