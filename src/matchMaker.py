class MatchMaker:
    def match(self, entities: set[str]):
        print(entities)
        # in entityA, entityB, entityG 
        database_result = {'entityA', 'entityG', 'entityB'}

        if len(database_result.difference(entities)) == 0:
            return "true"
    
        return "false"
