import spacy
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

nlp = spacy.load("en_core_web_sm")

tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")

nlpBert = pipeline("ner", model=model, tokenizer=tokenizer)


def extract_entities(user_input):
    bert_ner = nlpBert(user_input)
    doc = nlp(user_input)
    
    # Filter for B-LOC entities
    filtered_entities = [
    entity for entity in bert_ner
    if entity["entity"] == "B-LOC" and not entity["word"].startswith("##")]

    words = [entity["word"] for entity in filtered_entities]
    print(f"Filtered Entities (words only is): {words}")

    spacy_ner = [(ent.text, ent.label_) for ent in doc.ents]
    print(f"Spacy NER Labels===> {spacy_ner}")

    if len(words) == 1:
        if words[0] == 'is':
            for ent in doc.ents:
                if ent.label_ == "DATE":
                    print(f"From Islamabad seat NO : [from_db] is available on {ent.text}")

        elif words[0] == 'Karachi':
            for ent in doc.ents:
                if ent.label_ == "DATE":
                    print(f"From Karachi seat NO : [from_db] is available on {ent.text}")

        elif words[0] == 'Lahore':
            for ent in doc.ents:
                if ent.label_ == "DATE":
                    print(f"From Lahore seat NO : [from_db] is available on {ent.text}")
                
    elif len(words) == 2:
        if 'Karachi' in words and 'Lahore' in words:
            for ent in doc.ents:
                if ent.label_ == "DATE":
                    print(f"From Karachi to Lahore seat NO : [from_db] is available on {ent.text}")
                    
        elif 'Lahore' in words and 'Karachi' in words:
            for ent in doc.ents:
                if ent.label_ == "DATE":
                    print(f"From Lahore to Karachi seat NO : [from_db] is available on {ent.text}")
    # query = {'arriveLoc': 'Lahore'}
    # result = buses.find(query)
    # print(f"db result is==> {result}")
    return entities
