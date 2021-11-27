import pathlib

class _Rule:
    def __init__(self, rule):
        rule_parts = rule.split(" bags contain ")
        self.primary_color = rule_parts[0]
        containing_bags = rule_parts[1].replace(" bags", "").replace(" bag", "").replace(".", "").replace("no other", "")
        containing_bags_parts = containing_bags.split(", ")
        if any(containing_bags_parts):
            self.containing_bags = [(int(x.split(" ")[0]), " ".join(x.split(" ")[1::])) for x in containing_bags_parts]
            self.containing_bags_set = set([x[1] for x in self.containing_bags])
        else:
            self.containing_bags = []
            self.containing_bags_set = set()
        self.parents = set()
        self.children = set()

    def contains_bag_color(self, bag_color):
        return bag_color in self.containing_bags_set

def load_rules(rules_location):
    return [_Rule(x) for x in pathlib.Path(rules_location).read_text().strip("\n").splitlines()]

def get_parents_recursively(current_parent_set, rule):
    for parent in rule.parents:
        if (parent not in current_parent_set):
            current_parent_set.add(parent)
            get_parents_recursively(current_parent_set, parent)
    
    return current_parent_set


def get_contained_bag_count_recursively(rules_dict, current_child_set, rule):
    current_bag_count = 0
    for contained_bag in rule.containing_bags:
        if (contained_bag[1] not in current_child_set):
            current_bag_count = current_bag_count + contained_bag[0] * (get_contained_bag_count_recursively(rules_dict, current_child_set, rules_dict[contained_bag[1]]) + 1)
    
    return current_bag_count

if __name__ == "__main__":
    rules = load_rules("./input/rules.txt")

    rules_dict = { x.primary_color : x for x in rules }
    for rule in rules:
        rule.children = set([rules_dict[x] for x in rule.containing_bags_set])
        for child in rule.children:
            child.parents.add(rule)

    # Part 1
    parent_bags = get_parents_recursively(set(), rules_dict["shiny gold"])
    print(len(parent_bags))

    # Part 2
    contained_bag_count = get_contained_bag_count_recursively(rules_dict, set(), rules_dict["shiny gold"])
    print(contained_bag_count)

    
