from libs import my_print, my_add, send_to_api

def main():
    num = my_add(1, 2)
    my_print(f"My num is: {num}!")
    send_to_api("Some data")


if __name__ == "__main__":
    main()