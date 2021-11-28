from service.parser import parser
from service.writer import writer

info, header = [], ["Title, Location, KM, Flat, Floor, Price"]


def main():
    # parse data from website
    parser(info)
    # write it in to csv file
    writer('data.csv', header, info)


if __name__ == "__main__":
    main()
