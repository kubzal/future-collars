import sys

# print(sys.argv)

input_file = sys.argv[1]
output_file = sys.argv[2]
changes = sys.argv[3:]

print(f"Input file: {input_file}")
print(f"Output file: {output_file}")

print("\nChanges:")
for change in changes:
    row, col, new_value = change.split(",")
    print(f"Row: {row}, Column: {col}, New value: {new_value}")