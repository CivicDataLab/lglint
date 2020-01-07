from typing import List, Dict, Mapping
import spacy

nlp = spacy.load("en_blackstone_proto")


def convert_to_cheyyali_format(text: str) -> Dict[str, Mapping[str, List[List[str]]]]:
    """
    Convert texts to jsonl format for cheyyali annotator

    Parameters:
            text: the input text that you want to convert to cheyyali's format
    """
    doc = nlp(text)
    ent_dict = {}
    all_labels = []
    for ent in doc.ents:
        label = [ent.start_char, ent.end_char, ent.label_]
        all_labels.append(label)
    ent_dict["text"] = text
    ent_dict["labels"] = all_labels

    return ent_dict
