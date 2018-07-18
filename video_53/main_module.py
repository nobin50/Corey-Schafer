if __name__ == '__main__':
    print("It's main module")

else:
    print("Second module")

print("Main modules name: {}".format(__name__))

if __name__ == '__main__':
    print("Run directly")

else:
    print("Run from import")


def main():
    print("I'm from main module")

if __name__ == '__main__':
    main()

