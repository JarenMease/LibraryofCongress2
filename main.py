"""
Project Name: Library of Congress
Author: Jaren Mease
Due Date: 10/15/2022
Course: CS1400

This program is designed to sort the data into corresponding texts.
Each text has the min length, max length, and average.
"""


def main():
    open_file = "book_data.txt"

    directory = {}

    with open(open_file, 'r', encoding='utf-8') as fin:

        for line in fin:
            each_line = line.strip().split('|')
            each_line.append(len(each_line[0]))
            each_line[1] = int(each_line[1])

            if each_line[2] in directory:
                directory[each_line[2]].append(each_line)
            else:
                directory[each_line[2]] = [each_line]

        sorted_directory = list(directory.keys())
        sorted_directory.sort()

        for book in sorted_directory:
            directory[book].sort(key=lambda x: x[3])

            longest = directory[book][-1]
            shortest = directory[book][0]
            actual_longest = []
            actual_shortest = []

            average = 0
            directory[book].sort(key=lambda x: x[1])

            with open('novel_text.txt', 'a') as text:
                text.writelines(f'{book}\n')

            for i in directory[book]:
                with open('novel_text.txt', 'a') as text:
                    text.writelines(f'{i[0]}\n')
                average += i[3]
                if i[3] == shortest[3]:
                    actual_shortest.append(i)
                if i[3] == longest[3]:
                    actual_longest.append(i)
            shortest = actual_shortest[0]
            longest = actual_longest[-1]

            with open('novel_text.txt', 'a') as text:
                if book != sorted_directory[2]:
                    text.writelines('-----\n')
            average = round(average / len(directory[book]))

            with open('novel_summary.txt', 'a') as summary:
                summary.writelines(
                    f'{book}\nLongest line ({longest[1]}): {longest[0]}\nShortest line ({shortest[1]}): {shortest[0]}\nAverage length: {average}\n\n')


if __name__ == "__main__":
    main()
