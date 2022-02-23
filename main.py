# Roger Le
# C950 Performance Assessment
# Student ID: 1060770

import typer
import csv


def main():
    # import data from CSV into HashTable
    with open('csv/packages.csv') as packages_file:
        csv_reader = csv.reader(packages_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count +=1
            else:
                print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
            print(f'Processed {line_count} lines.')


    typer.echo(f"Hello User")

if __name__ == "__main__":
    typer.run(main)