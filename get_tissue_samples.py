import argparse
import sys
# Import modules.


def main(in_file, tissue, out_file):
    """
    Function to extract samples of a chosen tissue group.

    Inputs
    ------
    in_file: string
    File with genes (?).

    tissue: string
    Tissue group to query.

    out_file: string
    Output file of tissue samples.
    """

    out = open(out_file, 'w')
    # Open output file for writing.

    header = None
    sampid_col = -1
    smts_col = -1

    file = open(in_file, 'rt')
    # Open the input file.

    for line in file:
        # Loop over all lines of the file.

        line = line.rstrip().split('\t')
        if header is None:
            header = line
            sampid_col = line.index('SAMPID')
            smts_col = line.index('SMTS')
            continue
            # Write header information.

        if line[smts_col] == tissue:
            # Current tissue matches selected tissue.
            out.write(line[sampid_col] + '\n')
            # Write tissue sample to output file.

    file.close()
    out.close()
    # Close output & input files.


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Get tissue samples")
    parser.add_argument('in_file', type=str,
                        help="File of sample")
    parser.add_argument('tissue', type=str,
                        help="Tissue group (SMTS)")
    parser.add_argument("out_file", type=str,
                        help="File of tissue group samples")
    args = parser.parse_args()
    # Read in arguments.

main(args.in_file, args.tissue, args.out_file)
# Run the main function.
