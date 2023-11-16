import spacy
from dataclasses import dataclass
import wikipedia

# nlp = spacy.load("en_core_web_sm")
nlp = spacy.load('en_core_web_sm')
_BLACKLIST = {'ORDINAL','CARDINAL','PERCENT','QUANTITY','PERCENT'}

@dataclass
class Entity:
  # Raw text.
  text: str
  # Type of entity.
  type: str
  # ID provided by Wikipedia if available.
  wiki_id: str = None
  # ID from Wikipedia if available, else text itself.
  id: str = None

class EntityExtractor:

    def _extract_raw_entities(self, text: str):
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(text)
        # return [{'text':ent.text,'type':ent.label_, 'kb_id':ent.kb_id} for ent in doc.ents]
        return [Entity(ent.text,ent.label_) for ent in doc.ents]

    def _filter_entities(self, entities):
        return [e for e in entities if e.type not in _BLACKLIST]

    def _get_wiki_id(self, text, language="en", auto_suggest=False, debug=False):
        assert language == "en", "Only English is supported for now!"
        wikipedia.set_lang(language)

        if debug: print(text)

        try:
            page = wikipedia.page(text, auto_suggest=False)
        except wikipedia.DisambiguationError or wikipedia.PageError:
            return None
        except BaseException:
            if debug: print('Other exception')
            return None
        return page.pageid


    def _disambiguate_entities(self, entities, auto_suggest=False, debug=False):
        wiki_ids = (self._get_wiki_id(entity.text, auto_suggest=auto_suggest, debug=debug) for entity in entities)
        entities = [Entity(text=e.text,type=e.type, wiki_id=wiki_id, id=(wiki_id or e.text)) for e, wiki_id in zip(entities, wiki_ids)]

        found_ids = set()
        normalized_entities = []
        for entity in entities:
            if entity.id not in found_ids:
                normalized_entities.append(entity)
                found_ids.add(entity.id)
            else:
                continue
        
        return normalized_entities

    #### MAIN METHOD #####
    def extract_entity_ids(self, text: str):
        print('xxxxx')
        entities = self._extract_raw_entities(text)
        entities = self._filter_entities(entities)
        entities = self._disambiguate_entities(entities)
        return [e.id for e in entities]
