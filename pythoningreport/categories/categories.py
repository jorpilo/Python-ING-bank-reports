import re

'''Define your list of categories, the REGEX lookup that will match
and the Function to allign with your criteira of category.'''
config = {
    "Income": {
        "match": ["Salary", "Dividend" "ATO"]
    },
    "Groceries": {
        "match": [ "WOOLWORTHS", "COLES", "ALDI", "Cosmos", "7-ELEVEN", "FISHME"]
    },  
    "Transport": {
        "match": ["OPAL", "UBER", "CARSHAREAUS", "TRANSPORT"],
    },
    "Shopping": {
        "match": ["Daiso", "store", "AMAZON", "BIG W", "MARKETPLACE", "KMART", "JB HI-FI", "EB GAMES", "TARGET", "OFFICEWORKS", "TYPO"]
    },
    "House":{
        "match":["VODAFONE", "AGL", "CIRCLES"]
    },
    "Rent": {
        "match": ["DEFT RENT", "RENT"]
    },
    "Investment": {
        "match": [ "Spaceship", "binance", "stake", "Stake"]
    },
    "Subs": {
        "match": ["LINODE", "Patreon", "AMZNPRIMEAU", "NETFLIX"]
    },
    "Internal": {
        "match": ["Internal", "round up"]
    },
    "Fitness": {
        "match": ["Clublinks", "Fitness"]
    }
}



class Category:
    name=""
    description=""
    match_terms=[]
    
    def __init__(self, name, description="", match_terms=[]):
        self.name = name
        self.description = description
        self.match_terms = match_terms
        self.regex = re.compile("|".join(map(re.escape, match_terms)), re.IGNORECASE)
        
    def match(self, item):
        return re.search(self.regex, item)


# Initialize categories classess
all_categories = [Category(name, config[name].get("description", None) , config[name].get("match", None)) for name in config]

def match_categories(item, categories=all_categories):
    category_list = list(categories)
    valid_categories = [x for x in category_list if x.match(item)]
    #valid_categories = [x for x in categories.values() if item == x]
    #TODO: return all the matching categories instead of only the first one
    # return valid_categories
    return valid_categories[0].name if valid_categories else "Uncategorized"
