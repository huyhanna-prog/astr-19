def main():
    def f(x):
        return x**3 + 8
    result = f(9)
    print(f"{result}")
    if result > 27:
        print("YAY!")

if __name__ == "__main__":
    main()

