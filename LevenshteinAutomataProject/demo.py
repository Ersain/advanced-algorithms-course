from levenshtein import LevenshteinAutomata

children = LevenshteinAutomata("children")

assert children.is_similar('children') is True
assert children.is_similar('childrens', max_errors=1) is True
assert children.is_similar('zhildren', max_errors=1) is True
assert children.is_similar('chipbzen', max_errors=3) is True

assert children.is_similar('zhildren', max_errors=0) is False
assert children.is_similar('chipbzen', max_errors=2) is False

print('OK!')
