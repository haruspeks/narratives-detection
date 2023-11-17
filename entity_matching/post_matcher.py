from . import matchmaker
from . import match_ranker


class PostMatcher:
    def __init__(self, base_file) -> None:
        self._matchmaker = matchmaker.Matchmaker(base_file)
        self._match_ranker = match_ranker.MatchRanker()
    
    def match_post(self, post):
        print(f"Original post:\n\n{post['content']}\n")
        intersecting = self._matchmaker.find_intersecting_posts(post, minimum_intersection=3)
        ranking = self._match_ranker.rank_matches(post, intersecting)
        self._present_results(intersecting, ranking)

    def _present_results(self, intersecting, ranking):
        biggest_intersection = max(intersecting.keys())
        print(f"Found total {len(intersecting)} intersecting posts.\n"
              f"Biggest intersection: {biggest_intersection} entities.\n"
              f"Highest intersection ranking: {ranking[0][0]}/1.\n"
              f"Highest ranked intersecting post:\n\n{ranking[0][1]['content']}.")
