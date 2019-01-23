# OTL_licenses

Script to retrieve license information for Open Textbook Library e-books and format 540 field to be inserted in MARC records

## Usage
The input file must be a .csv with the e-book URL in the final (rightmost) column. It should be located in the same directory as OTL_licenses.py. The output file is also a .csv file containing all the data from the input file with two additional columns, LICENSE and 540FIELD. The script checks each e-book page for text indicating the license, which is added to the LICENSE column of the output file. The 540FIELD column contains the license information formatted for insertion into MARC records.

To run the script from the command line, first move to the directory where OTL_licenses.py is located. Then type the following and hit Enter:

`python OTL_licenses.py input.csv output.csv`

where 

- `input.csv` is the name of your input file, and
- `output.csv` is the name of the output file that will be created.


## Author
Rebecca B. French
