def merge_files():
    input_files = ["0-BIOS.css", "0-Kernel_Ring0.css", "0-Kernel_Ring1.css", "0-Kernel_Ring2.css", "0-Kernel_Ring3.css", "0-Kernel_Serial.css", "1-Anarchy_SID.css", "2-Theme_00-Iridescent.css", "2-Theme_01-CustomIMG.css", "2-Theme_03-Transparent.css", "3-MGM_00-Control.css", "3-MGM_00-Control-MAT.css", "3-MGM_00-Control-AT.css", "3-MGM_01-ChatEx.css", "3-MGM_01-ChatIn.css", "3-MGM_02-OTUI_Base.css", "3-MGM_02-OTUI_Pop.css", "4-SM_Base.css", "4-SM_Pop.css", "4-SM_UnNitrofy.css", "5-ChatEffects_CD.css", "6-CFIX_RPLUGIN.css", "6-CFIX_RTHEME.css", "6-CLIST_RPLUGIN.css", "6-CLIST_RTHEME.css", "7-Lang.css"]
    output_file = "sid.css"  # Specify the output file path here

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