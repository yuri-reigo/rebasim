from libs import my_print, my_add, send_to_api

def main():
    num = my_add(1, 2)
    my_print(f"The number is ....: {num} !")
    send_to_api("work complete")

if __name__ == "__main__":
    main()