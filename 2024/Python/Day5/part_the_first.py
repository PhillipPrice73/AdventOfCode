DEBUG = True

def ExtractRulesAndUpdates(input_file):
    rules_list = []
    updates_list = []
    with open(input_file) as f:
        gathering_rules = True
        for line in f:
            line = line.rstrip()
            if line == "":
                gathering_rules = False
                continue # blank line separating rules and updates, doesn't belong in either camp

            if gathering_rules:
                line = line.split("|")
                rules_list.append([int(item) for item in line])
            else:
                line = line.split(",")
                updates_list.append([int(item) for item in line])

    #print("{0}".format(rules_list))
    #print("{0}".format(updates_list))
    return rules_list, updates_list


def ExtractRuleOrder(rules_list):
    rule_order = []
    rule_order.append(rules_list[0][0])
    rule_order.append(rules_list[0][1])
    rules_list.pop(0)

    #generate endpoint of rules list
    target_to_find = rule_order[-1]
    target_found = False
    target_exists = True
    while target_exists:
        for item in rules_list:
            if item[0] == target_to_find:
                rule_order.append(item[1])
                target_to_find = item[1]
                #rules_list.remove(item)
                target_found = True
                break
        if target_found:
            target_found = False
            continue
        else:
            target_exists = False

    #generate starting point of rules list
    target_to_find = rule_order[0]
    target_found = False
    target_exists = True
    while target_exists:
        for item in rules_list:
            if item[1] == target_to_find:
                rule_order.insert(0, item[0])
                target_to_find = item[0]
                #rules_list.remove(item)
                target_found = True
                break
        if target_found:
            target_found = False
            continue
        else:
            target_exists = False

    # putting remaining rules in order
    rules_to_add = []
    for item in rules_list:
        if item[0] not in rule_order and item[0] not in rules_to_add:
            rules_to_add.append(item[0])
        if item[1] not in rule_order and item[1] not in rules_to_add:
            rules_to_add.append(item[1])

    for rule in rules_to_add:
        for item in rules_list:
            if rule == item[0]:
                if rule in rule_order and item[1] in rule_order:
                    rule_pt1_idx = rule_order.index(rule)
                    rule_pt2_idx = rule_order.index(item[1])
                    if rule_pt1_idx < rule_pt2_idx:
                        continue
                    else:
                        rule_order.remove(rule)
                        rule_order.insert(rule_pt2_idx-1, rule)
                elif item[1] in rule_order:
                    rule_idx = rule_order.index(item[1])
                    rule_order.insert(rule_idx, rule)
            elif rule == item[1]:
                if rule in rule_order and item[0] in rule_order:
                    rule_pt1_idx = rule_order.index(item[0])
                    rule_pt2_idx = rule_order.index(rule)
                    if rule_pt1_idx < rule_pt2_idx:
                        continue
                    else:
                        rule_order.remove(rule)
                        rule_order.insert(rule_pt1_idx, rule)
                elif item[0] in rule_order:
                    rule_idx = rule_order.index(item[0])
                    rule_order.insert(rule_idx+1, rule)

    #print("Rule to add: {0}".format(rules_to_add))
    #print("Rules list: {0}".format(rules_list))
    #print("Rule ordering: {0}".format(rule_order))
    return rule_order


def isValidUpdateOrder(rule_order, update_list):
    lower_bound = rule_order.index(update_list[0])
    for i in range(1,len(update_list)):
        if update_list[i] in rule_order[lower_bound+1:]:
            lower_bound = rule_order.index(update_list[i])
        else:
            return False
    return True


if __name__ == "__main__":
    if DEBUG:
        rules, updates = ExtractRulesAndUpdates("DebugData")
    else:
        rules, updates = ExtractRulesAndUpdates("TestData")

    rule_ordering = ExtractRuleOrder(rules)
    for update in updates:
        print("{0}".format(isValidUpdateOrder(rule_ordering, update)))
