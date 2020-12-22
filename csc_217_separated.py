def csc_217_separated():
    with open('csc_attendance.txt', 'r') as input_file, \
            open('csc_computer.txt', 'w') as output_file1, \
            open('csc_IT.txt', 'w') as output_file2:
        elements = [line for line in input_file]
        for line in elements:
            if 'B141' in line:
                output_file2.write(line)
            output_file1.close()
            input_file.close()
        for line in elements:
            if 'B135' in line:
                output_file1.write(line)
        output_file1.close()


csc_217_separated()
