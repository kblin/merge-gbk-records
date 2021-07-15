from argparse import ArgumentParser
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio.SeqRecord import SeqRecord
import sys

from merge_gbk_records import __version__

ALL_FRAME_STOP_MOTIF = 'TAGCTAACTGACCGTCAGTTAGCTA'


def main():
    """Run merge-gbk-records"""

    parser = ArgumentParser(description="Merge GenBank records with a defined spacer sequence")
    parser.add_argument('records', nargs='+',
                        help='A GenBank file to merge')
    parser.add_argument('-l', '--length',
                        type=int, default=20,
                        help='Length of the spacer in kbp (default: %(default)s).')
    parser.add_argument('-s', '--spacer',
                        choices=('n', 'stop'), default='n',
                        help="Spacer sequence to use, can be Ns or all-frame stop codons (default: %(default)s).")
    parser.add_argument('-o', '--outfile',
                        default='stdout',
                        help="Output file to write to, or 'stdout' to write to terminal (default: %(default)s).")
    parser.add_argument('-V', '--version', version=__version__, action='version')

    args = parser.parse_args()

    records = []
    for seqfile in args.records:
        records.extend(SeqIO.parse(seqfile, 'genbank'))

    merged_record = merge(records, args.length, args.spacer)

    if args.outfile == 'stdout':
        outfile = sys.stdout
    else:
        outfile = open(args.outfile, 'w')

    SeqIO.write([merged_record], outfile, 'genbank')

    if args.outfile != 'stdout':
        outfile.close()

    sys.exit(0)


def merge(records, length=20, spacer='n'):
    """Merge multiple SeqRecords into one, using a defined spacer

    :param records: Iterable containing SeqRecords to be merged
    :param length: Length of the spacer in kbp
    :param spacer: Kind of spacer to use ('n' for UnknownSeq spacer, 'stop' for all-frame stop codon spacer)

    :return: A single SeqRecord that is the product of the merge.
    """

    if spacer not in ('n', 'stop'):
        raise ValueError("Invalid spacer: %r, use either 'n' or 'stop'" % spacer)

    if not len(records):
        raise ValueError("No records given")

    if spacer == 'stop':
        spacer_seq = Seq(ALL_FRAME_STOP_MOTIF * 40 * length)
    else:
        spacer_seq = Seq('N' * 1000)

    new_rec = records[0]

    if len(records) == 1:
        return new_rec

    rec_id = new_rec.id
    rec_name = new_rec.name
    rec_desc = new_rec.description
    date = new_rec.annotations.get('date', '')
    source = new_rec.annotations.get("source", '')
    organism = new_rec.annotations.get('organism', '')
    taxonomy = new_rec.annotations.get('taxonomy', [])
    data_file_division = new_rec.annotations.get('data_file_division', 'UNK')
    topology = new_rec.annotations.get('topology', 'linear')

    for i, rec in enumerate(records[1:]):
        spacer_id = 'spacer_{}'.format(i + 1)

        spacer_feature = SeqFeature(FeatureLocation(0, length * 1000, 0),
                                    type='misc_feature', id=spacer_id,
                                    qualifiers={'note': [spacer_id]})

        spacer_rec = SeqRecord(spacer_seq, id=spacer_id, name=spacer_id,
                               description=spacer_id, features=[spacer_feature])

        new_rec = new_rec + spacer_rec + rec

    new_rec.id = rec_id
    new_rec.name = rec_name
    new_rec.description = rec_desc
    new_rec.annotations['molecule_type'] = "DNA"
    new_rec.annotations["date"] = date
    new_rec.annotations["source"] = source
    new_rec.annotations["organism"] = organism
    new_rec.annotations["taxonomy"] = taxonomy
    new_rec.annotations["data_file_division"] = data_file_division
    new_rec.annotations["topology"] = topology

    return new_rec


if __name__ == '__main__':
    main()
