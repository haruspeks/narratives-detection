import csv
import ast
import collections

BLACKLIST = {'ORDINAL','CARDINAL','PERCENT','QUANTITY','PERCENT'}


# Assuming Bellingcat QAnon DB csv dump
class EntityMatchmaker:
    def __init__(self, file_path):
        with open(file_path) as file:
            reader = csv.DictReader(file)
            self._posts = [line for line in reader]
            self._convert_named_entities_to_objects()
            self._collect_unique_entities()
            self._add_numbered_entities_set_to_posts()

    def _convert_named_entities_to_objects(self):
        failed = 0
        new_posts = []
        for post in self._posts:
            try:
                parsed = ast.literal_eval(post['named_entities'])
                if type(parsed) != list:
                    raise Exception
                post['named_entities'] = parsed
                new_posts.append(post)
            except:
                failed += 1
        print(f"Failed to parse {failed} posts")
        self._posts = new_posts

    def _collect_unique_entities(self):
        count = 0
        self._unique_entities = {}
        for post in self._posts:
            for entity in post['named_entities']:
                if entity['text'] in self._unique_entities.keys():
                    continue
                if entity['type'] in BLACKLIST:
                    continue
                self._unique_entities[entity['text']] = count
                count += 1
        self._id_to_entity = {value: entity for entity, value in self._unique_entities.items()}

    def _add_numbered_entities_set_to_posts(self):
        for post in self._posts:
            post_entities = [entity['text'] for entity in post['named_entities']]
            post['numbered_entities'] = set([self._unique_entities[entity] for entity in post_entities])

    def find_intersecting_posts(self, post):
        intersecting = collections.defaultdict(list)
        for other_post in self._posts:
            intersection = post['numbered_entities'].intersection(other_post['numbered_entities'])
            if len(intersection) <= 0:
                continue
            other_post['intersecting'] = [self._id_to_entity[id] for id in intersection]
            intersecting[len(intersection)].append(other_post)
        return intersecting
