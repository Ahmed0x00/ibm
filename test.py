import re

def extract_domains(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            match = re.match(r'([^\s]+)\s+\[\d+\]\s+\[\d+\]', line)
            if match:
                outfile.write(match.group(1) + '\n')
    print(f"Extracted domains saved as {output_file}")

# Example usage
extract_domains('ibm_cloud-live.txt', 'ibm_cloud.txt')
extract_domains('ibm_com-live.txt', 'ibm_com.txt')