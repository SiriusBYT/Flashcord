def merge_files():
    input_files = [
        "0-BIOS.css", 
        "0-Kernel_Ring1.css",
        "0-Kernel_Ring3.css",
        "0-Kernel_Serial.css",
        "2-Theme_01-CustomIMG.css",
        "3-MGM_00-Control.css",
        "3-MGM_01-ChatEx.css",
        "3-MGM_01-ChatIn.css",
        "4-SM_Pop.css",
        ]
    output_file = "lpm.css"  # Specify the output file path here

    try:
        with open(output_file, 'w', encoding='utf-8') as out_file:
            for input_file in input_files:
                try:
                    with open(input_file, 'r', encoding='utf-8') as in_file:
                        out_file.write(in_file.read())
                        out_file.write('\n')  # Add a newline between the content of each file
                except FileNotFoundError:
                    print(f"Warning: File '{input_file}' not found. Skipping...")
        print("Files merged successfully!")
    except Exception as e:
        print(f"Error merging files: {e}")

if __name__ == "__main__":
    merge_files()