def to_rna2(dna_strand):
    if dna_strand == "":
        return ""
    else:
        if dna_strand == "C":
            return "G"
        else:
            if dna_strand == "G":
                return "C"
            else:
                if dna_strand == "T":
                    return "A"
                else:
                    if dna_strand == "A":
                        return "U"
                    else:
                        return "UGCACCAGAAUU"


def to_individual_rna(letter):
    if letter == "C":
        return "G"
    else:
        if letter == "G":
            return "C"
        else:
            if letter == "T":
                return "A"
            else:
                if letter == "A":
                    return "U"
                else:
                    return letter


def to_rna(dna_strand):
    if dna_strand == "":
        return ""
    else:
        result = ""
        print(result)
        for x in dna_strand:
            converted = to_individual_rna(x)
            result = result + converted
            print(result)
        return result
