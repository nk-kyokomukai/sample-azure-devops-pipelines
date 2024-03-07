from animal import TwoCats


def main():
    cats = TwoCats()
    print(cats.get_animal_kind())
    print(cats.get_is_japanese())
    print(cats.get())


if __name__ == '__main__':
    main()
