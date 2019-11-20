import sys
import gzip
import argparse
# Import modules.

if __name__ == '__main__':
    """
    Main function.
    """
    parser = argparse.ArgumentParser(description='Gene counts')
    parser.add_argument('in_file', type=str,
                        help='Input gene file')
    parser.add_argument('gene', type=str,
                        help='Gene name')
    parser.add_argument('out_file', type=str,
                        help='Output file')
    args = parser.parse_args()
    # Parse input arguments.

    in_file = args.in_file
    gene = args.gene
    out_file = args.out_file
    # Initialize arguments.

    o = open(out_file, 'w')
    # Create output file for writing.

    version = None
    dim = None
    header = None

    f = gzip.open(in_file, 'rt')
    # Read in the gzipped gene file.

    for l in f:
        # Loop over each line of the input file.
        A = l.rstrip().split('\t')
        if version is None:
            version = A
            continue
        if dim is None:
            dim = A
            continue
        if header is None:
            header = A
            continue
        # Write version, dimension & header information.
        if A[1] == gene:
            # Current gene matches selected gene.
            for i in range(2, len(header)):
                o.write(header[i] + ' ' + A[i] + '\n')
                # Write sample ID & count for selected gene
                # to output file.

    f.close()
    o.close()
    # Close input & output files.
