import sys
import markdown

def convert_markdown_to_html(input_file, output_file):
    with open(input_file, 'r') as infile:
        markdown_content = infile.read()
        html_content = markdown.markdown(markdown_content)
        with open(output_file, 'w') as outfile:
            outfile.write(html_content)

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 file-converter.py markdown inputfile outputfile")
        return

    command = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    if command != "markdown":
        print("Invalid command. Use 'markdown' as the first argument.")
        return

    if not input_file.endswith('.md'):
        print("Input file must have a .md extension.")
        return

    if not output_file.endswith('.html'):
        print("Output file must have a .html extension.")
        return

    convert_markdown_to_html(input_file, output_file)
    print(f"Conversion complete. HTML file saved as {output_file}.")

if __name__ == "__main__":
    main()
