DEBUG = False

from part_the_first import ExtractRulesAndUpdates, IsValidUpdateOrder, CreateCondensedRules, ExtractMiddleValue

# def CountDictionaryKeysWithEmptyListValues(my_dict):
#     my_list = []
#     for key in my_dict:
#         my_list.append(len(my_dict[key]))
#         #print("List size: {0}\nList: {1}".format(len(my_dict[key]), my_dict[key]))
#     my_list.sort()
#     for item in my_list:
#         print("List size: {0}".format(item))


# def CountUniquePages(rules):
#     unique_pages = []
#     for rule in rules:
#         if rule[0] not in unique_pages:
#             unique_pages.append(rule[0])
#         if rule[1] not in unique_pages:
#             unique_pages.append(rule[1])
#     print("Number of unique pages: {0}".format(len(unique_pages)))


# def PrintRules(rules, idx):
#     key_rule = rules[idx][0]
#     forward_rules_list = []
#     backward_rules_list = []
#     for rule in rules:
#         if rule[0] == key_rule:
#             forward_rules_list.append(rule)
#         if rule[1] == key_rule:
#             backward_rules_list.append(rule)
#     print(forward_rules_list)
#     print(len(forward_rules_list))
#     print("")
#     print(backward_rules_list)
#     print(len(backward_rules_list))


def FilterRules(rules, pages):
    filteredRules = []
    for rule in rules:
        if rule[0] in pages and rule[1] in pages:
            filteredRules.append(rule)
    return filteredRules


def GetRelevantPages(update):
    relevantPages = [x for x in update]
    return relevantPages


def CreateCorrectUpdate(relevant_rules):
    # relevant_rules is a list of tuples, where each tuple is a rule order

    prior_pages, future_pages = CreateCondensedRules(relevant_rules)
    # prior/future_pages = dictionary. key = page#. values = pages to appear before/after key

    correctUpdate = []
    correctUpdate.append(relevant_rules[0][0])
    correctUpdate.append(relevant_rules[0][1])
    last_page = correctUpdate[-1]
    while future_pages[last_page].keys():
        correctUpdate.append(future_pages[last_page][0])
        last_page = future_pages[last_page][0]

    first_page = correctUpdate[0]
    while prior_pages[first_page].keys():
        correctUpdate.insert(0, prior_pages[first_page][0])
        first_page = prior_pages[first_page][0]

    for key,values in prior_pages:
        for value in values:
            key_index = correctUpdate.index(key)

    pass


if __name__ == "__main__":
    if DEBUG:
        rules, updates = ExtractRulesAndUpdates("DebugData")
    else:
        rules, updates = ExtractRulesAndUpdates("TestData")

    backward_rules, forward_rules = CreateCondensedRules(rules)

    total = 0
    for update in updates:
        if not IsValidUpdateOrder(backward_rules, forward_rules, update):
            relevant_pages = GetRelevantPages(update)
            relevant_rules = FilterRules(rules, relevant_pages) # list of tuples
            corrected_update = CreateCorrectUpdate(relevant_rules)
            total += ExtractMiddleValue(corrected_update)
