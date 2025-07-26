import random


def main():

    data = ""
    for i in range(1, 10000000):
        data += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    with open("test3.txt", 'w') as f:
         f.write(data)

if __name__ == "__main__":
    main()
