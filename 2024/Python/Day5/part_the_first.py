DEBUG = False

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

    return rules_list, updates_list


def CreateCondensedRules(rules_list):
    previous_entries = {} # key = page number, value = list of all page numbers to appear before key
    future_entries = {} # key = page number, value = list of all page numbers to appear after key
    for rule in rules_list:
        if rule[0] not in future_entries:
            future_entries[rule[0]] = [rule[1]]
        else:
            future_entries[rule[0]].append(rule[1])
        if rule[1] not in previous_entries:
            previous_entries[rule[1]] = [rule[0]]
        else:
            previous_entries[rule[1]].append(rule[0])

    return previous_entries, future_entries


def IsValidUpdateOrder(backwards_looking_rules, forward_looking_rules, update_order):
    update_is_valid = True
    for page in update_order:
        page_index = update_order.index(page)
        previous_pages = update_order[:page_index]
        future_pages = update_order[page_index+1:]
        # Check if previous pages need to appear after current page
        if page in forward_looking_rules.keys():
            for p in previous_pages:
                if p in forward_looking_rules[page]:
                    update_is_valid = False
                    break
            if not update_is_valid:
                break
        # Check if future pages need to appear before current page
        if page in backwards_looking_rules.keys():
            for p in future_pages:
                if p in backwards_looking_rules[page]:
                    update_is_valid = False
                    break
            if not update_is_valid:
                break
    return update_is_valid


def ExtractMiddleValue(list):
    middle_index = len(list) // 2
    return list[middle_index]


if __name__ == "__main__":
    if DEBUG:
        rules, updates = ExtractRulesAndUpdates("DebugData")
    else:
        rules, updates = ExtractRulesAndUpdates("TestData")
    print("Read file")

    backward_rules, forward_rules = CreateCondensedRules(rules)
    print("Extracted Rule Ordering")

    total = 0
    for update in updates:
        if IsValidUpdateOrder(backward_rules, forward_rules, update):
            total += ExtractMiddleValue(update)

    print("Total: {0}".format(total))
