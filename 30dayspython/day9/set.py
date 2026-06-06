"""
Module 3: Sets Practice

Concepts covered:
- Unique values
- Add and remove
- Union
- Intersection
- Difference

Exercises implemented as functions and demonstrated below.
"""

def remove_duplicates_using_set(lst):
    return list(set(lst))

def remove_duplicates_preserve_order(lst):
    return list(dict.fromkeys(lst))

#  Find common values between two sets
def common_values(a, b):
    return a & b

#  Find values present in one set but not another
def difference(a, b):
    return a - b

# Demonstrate add and remove
def demo_add_remove():
    s = set()
    s.add('apple')
    s.add('banana')
    s.discard('cherry')  # safe if not present
    try:
        s.remove('banana')  # will raise KeyError if missing
    except KeyError:
        pass
    return s

if __name__ == '__main__':
    # Exercise 1
    lst = [1, 2, 2, 3, 4, 4]
    print('Original list:', lst)
    print('Unique (set):', remove_duplicates_using_set(lst))
    print('Unique (preserve order):', remove_duplicates_preserve_order(lst))

    # Exercises 2 & 3
    a = {1, 2, 3}
    b = {2, 3, 4}
    print('\nSet A:', a)
    print('Set B:', b)
    print('Common (A & B):', common_values(a, b))
    print('In A not B (A - B):', difference(a, b))

    # Demo add/remove
    print('\nAdd/remove demo result:', demo_add_remove())

    # Mini Project: Course Enrollment System
    python_students = {"Ram", "Hari", "Sita"}
    ai_students = {"Hari", "Sita", "Gita"}

    common_students = common_values(python_students, ai_students)
    total_unique_students = python_students | ai_students

    print('\nPython students:', python_students)
    print('AI students:', ai_students)
    print('Common students:', common_students)
    print('Total unique students:', total_unique_students)
    print('Number of unique students:', len(total_unique_students))
