import re


def get_target_case(filename, metadata, use_cnr, pattern):
    if not re.search(pattern, filename):
        print({f"error": "File {filename} doesnt match the pattern {self.pattern} "})
        return None

    case_identifier = re.findall(pattern, filename)[0]
    if not use_cnr:
        column = "case_no"
        case_identifier = int(case_identifier)
    else:
        column = "cino"
    # case_identifier = filename.split('_')[0]
    return metadata[metadata[column] == case_identifier]
