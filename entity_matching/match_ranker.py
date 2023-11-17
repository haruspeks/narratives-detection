class MatchRanker:
    def rank_matches(self, original_post, matches):
        match_ranking = []
        for intersection_size, matching_posts in matches.items():
            for post in matching_posts:
                rank = self._rank_match(original_post, post, intersection_size)
                match_ranking.append((rank, post))
        match_ranking.sort(reverse=True, key=lambda pair: pair[0])
        return match_ranking

    def _rank_match(self, original_post, match, intersection_size):
        original_entity_count = len(original_post['numbered_entities'])
        match_post_entity_count = len(match['numbered_entities'])
        rank = (intersection_size / original_entity_count) * (intersection_size / match_post_entity_count)
        return rank
