import csv


with open("covid_confirmed_usafacts.csv") as csv_file:

    file = open("outfile.csv","w")


    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count = 0

    for row in csv_reader:

        if line_count == 0:
            out_string = ""
            n = 0
            for i in row:
                if n == len(row) - 1:
                    out_string = out_string + str(i)
                else:
                    out_string = out_string + str(i) + ","
                n += 1
                    
            file.write(out_string + "\n")
            line_count += 1
        else:

            num = row[0]


            if (len(str(num)) == 4):
                out_string="0"
                
            else:
                out_string = ""
                
            n = 0
            for i in row:
                if n == len(row) - 1:
                    out_string = out_string + str(i)
                else:
                    out_string = out_string + str(i) + ","


                n += 1
                    
            file.write(out_string + "\n")
                    
    file.close

print("Complete")
