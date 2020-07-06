## Homework3 review

### Homework3 evaluation
- Maximum score is +10 minimum is 0.
- Completed tasks 1-3 are scored as +5.
- Completed tasks 4-6 are scored as +1 each.
- +0,5 for Task 5 O(n) solution. 
- +1 for good namings, code structure, overall impression.
- PR that doesn't pass any of PR checklist checks takes -0,5.
- PR that doesn't pass any 2 of PR checklist checks takes -3.
- All review comments should be addressed (either fixes or 
substantiation of your position) . Missed comments causes score 
penalties.

### PR checklist
Please make sure you've passed PR checklist
- [ ] my PR passes CI checks (flake8 and pycodestyle)
- [ ] my PR named according guidelines: `Homework3: Name Surname`
- [ ] my PR contains complete tasks descriptions for all tasks
- [ ] my PR made from fork feature brunch to Maxim master branch.
- [ ] my PR don't contain only code that solves Homework3 tasks.
Redundant files (configs, etc. ) are put to .gitignore


### Review notes:
1. Please don't move \_\_init__.py file, make new one if you need.
2. Please don't delete \_\_init__.py file
3. Please remove redundant comments from code.
4. Failed PR checks - tasks description
5. Please divide tasks with two blank lines if you're doing them in one file
6. Redundant comments in code.
7. FAILED CI CHECKS

8. Task 1. Looks too bulky for such easy task. 
9. Task 1. if you want to check `value == ''` it can be written like `if not value` here.
10. Task 1. `i % 15`?
11. Task 1. if you want to check `value == 0` it can be written like `if not value` here.
12. Task 1. It doesn't solve task in homework (both versions)

13. Task 2.1. Redundant parentheses.
14. Task 2.1. It doesn't solve task in homework. 
15. Task 2.1. It can be one-line solution. 
16. Task 2.1. `'abcd'` would be enough.
17. Task 2.2. It doesn't solve task in homework. 
18. Task 2.3 '1234' - one more option. No need in str
19. Task 2.3. It can be one-line solution.
20. Task 2.3. `for a in 'a'` looks redundant here
21. Task 2.4. It should be deleted and printed simultaneously. Your code doesn't solve task.
22. Task 2.4. According to task description, element should be deleted, not just get it.
23. Task 2.5. It doesn't solve task in homework.

24. Task 3.2 it would be more explicit with parentheses
25. Task 3.3. Too many redundant code.
26. Task 3.3. Your code doesn't make assignments.
27. Task 3.3. Your code doesn't solve task in homework.
28. Task 3.4. You code doesn't solve task in homework.
29. Task 3.4. This tuple has length 3 and it contradicts task description
30. Task 3.4. It doesn't contain elements `1, 2, 3`. Code doesn't solve task.  

31. Task 4. Looks like O(n**2) solution. It can be solved for O(n)
32. Task 4. `dct[el] = dct.get(el, 0)+1`

33. Task 5. For immutable types can be solved with set - it would be more clear
34. Task 5. O(n**2) solution. It can be solved as O(n) for immutable types. 

35. Task 6. if you want to check `value == 0` it can be written like `if not value` here.
36. Task 6. Contradicts with task description in homework.






