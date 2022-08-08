from datetime import date
import argparse

parser = argparse.ArgumentParser()

# Add argument for name
parser.add_argument('-n',
                    '--name',
                    required=True,
                    help='input your name'
)

# Add argument for date of birth
parser.add_argument('-d',
                    '--dob',
                    required=True,
                    help='input your date of birth (DD-MM-YYYY)'
)

# Parse the argument
args = parser.parse_args()

# Get each date, month, and year from the argument
d = int(args.dob[:2])
m = int(args.dob[3:5])
y = int(args.dob[-4:])

# Get today date, month, and year
today = date.today()

# Calculate the age with today date - date of birth
age = today.year - y - ((today.month, today.day) < (m, d))

# If the age is less than 30, print with "kakak", else print with "bapak"
if (age < 30):
    print(f"Terima kasih telah menggunakan argParser.py pada tahun {str(today.year)}, kakak {args.name}")
else:
    print(f"Terima kasih telah menggunakan argParser.py pada tahun {str(today.year)}, bapak {args.name}")
