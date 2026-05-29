from collections import Counter

def check_sequence(seq):
    allowed = {"A", "T", "G", "C"}

    for symbol in seq:
        if symbol not in allowed:
            return False

    return True

def reverse_complement(seq):
    pairs = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }

    new_seq = ""

    for nucleotide in seq:
        new_seq = pairs[nucleotide] + new_seq

    return new_seq


def transcribe(seq):
    rna = ""

    for nucleotide in seq:
        if nucleotide == "T":
            rna += "U"
        else:
            rna += nucleotide

    return rna


def nucleotide_percentages(seq):
    data = Counter(seq)

    percentages = {}

    for nucleotide in ["A", "T", "G", "C"]:
        percentages[nucleotide] = round(
            data[nucleotide] / len(seq) * 100,
            2
        )

    return percentages


print("DNA-ANALYSATOR")

sequence = input("DNA-Sequenz eingeben: ").strip().upper()

if sequence == "":
    print("Die Sequenz ist leer.")
    exit()

if not check_sequence(sequence):
    print("Die Sequenz enthält ungültige Zeichen.")
    exit()

print("\nANALYSE")

print(f"Länge der Sequenz: {len(sequence)}")


counts = Counter(sequence)

print("\nAnzahl der Nukleotide:")

for nucleotide in ["A", "T", "G", "C"]:
    print(f"{nucleotide}: {counts[nucleotide]}")

print("\nProzentanteil der Nukleotide:")

percentages = nucleotide_percentages(sequence)

for nucleotide in percentages:
    print(f"{nucleotide}: {percentages[nucleotide]}%")

print("\nReverse Komplementsequenz:")
print(reverse_complement(sequence))

print("\nRNA-Sequenz:")
print(transcribe(sequence))
