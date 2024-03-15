'''
Notice: I'm dog shit at Python. No seriously.
This script compiles every single CSS File in the input_files array to produce a singular file to be uploaded at
https://sirio-network.com/flashcord/sid.css (or lpm.css or stb.css)
I honestly have no idea how this script works and it's half assed (?).
Ever since Flashcord versions "compiled" past or during January 2024, every single file except lpm.css (due to Replugged restrictions)
are minimized manually and are inserted manually at the beginning the following string:

/* WARNING: The file you have opened is not meant to be edited and isn't user friendly.
Please open https://github.com/SiriusBYT/Flashcord/tree/main/src/ and clone the folder that concerns your installed Flashcord Branch.

Please remind yourself also to read https://github.com/SiriusBYT/Flashcord/blob/main/LICENSE.md before modifying Flashcord.
If you can't be bothered doing that, just know that:
This license requires that re-users give credit to the creator. It allows re-users to copy and distribute the material in any medium or format in unadapted form and for noncommercial purposes only. 
[Flashcord] © 2023-2024 by [SiriusBYT] is licensed under [CC BY-NC-ND 4.0]. (Exceptions to the license's restrictions may and will apply.) */
'''

def merge_files():
    input_files = [
    "0-BIOS.css",
    "0-Kernel_Ring0.css",
    "0-Kernel_Ring1.css",
    "0-Kernel_Ring2.css",
    "0-Kernel_Ring3.css",
    "0-Kernel_Serial.css",
    "1-Anarchy_SID.css",
    "2-ThemeHooker.css",
    "2-Theme_00-Iridescent.css",
    "2-Theme_01-CustomIMG.css",
    "2-Theme_03-Transparent.css",
    "2-Theme_04-Terminal.css",
    "3-MGM_00-Control.css",
    "3-MGM_00-Control-MAT.css",
    "3-MGM_00-Control-AT.css",
    "3-MGM_01-ChatEX.css",
    "3-MGM_01-ChatIn.css",
    "3-MGM_02-OTUI_Base.css",
    "3-MGM_02-OTUI_Pop.css",
    "4-SM_Base.css",
    "4-SM_Pop.css",
    "4-SM_UnNitrofy.css",
    "5-ChatEffects_CD.css",
    "5-ChatEffects_KF.css",
    "6-CFIX_RPLUGIN.css",
    "6-CFIX_RTHEME.css",
    "6-CLIST_RPLUGIN.css",
    "6-CLIST_RTHEME.css",
    "7-Lang.css"
    ]
    output_file = "sid.css"
    try:
        with open(output_file, 'w', encoding='utf-8') as out_file:
            for input_file in input_files:
                try:
                    with open(input_file, 'r', encoding='utf-8') as in_file:
                        out_file.write((in_file.read()))
                except FileNotFoundError:
                    print(f"Warning: File '{input_file}' not found. Skipping...")
        print("Files merged successfully!")
    except Exception as e:
        print(f"Error merging files: {e}")

if __name__ == "__main__":
    merge_files()
