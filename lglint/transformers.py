from typing import Dict
import spacy

nlp = spacy.load("en_blackstone_proto")


def convert_to_cheyyali_format(text: str) -> Dict:
    """
    convert texts to jsonl format for cheyyali annotator
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
