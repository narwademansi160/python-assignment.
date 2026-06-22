try:
    file = open("report.txt", "r")

    content = file.read()

    print("File Content:")
    print(content)

    file.close()

except FileNotFoundError:
    print("Error: Report file not found")