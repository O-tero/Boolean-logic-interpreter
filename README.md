# Boolean Logic Interpreter

This implementation uses a class BooleanExpression to evaluate boolean expressions.
The class has a method evaluate which returns the result of the expression. The expression can contain the variables, which are stored in the variables dictionary.
The method set_variable can be used to set the value of the variables.

## Syntax

The syntax for expressions is as follows:

The expression can contain variables, which are case-sensitive strings that start with a letter and can contain letters, digits, and underscores.
The expression can contain the following operators:

- `!` (NOT) operator, which negates a boolean value. The operator has higher precedence than the ∧ (AND) and ∨ (OR) operators.
- `∧` (AND) operator, which returns True if both operands are True, and False otherwise.
- `∨` (OR) operator, which returns True if at least one of the operands is True, and False otherwise.
- Parentheses can be used to change the precedence of operations.

Here are some examples of valid expressions:

'T ∨ F'

`(T ∧ F) = F'

`let X = F'

`let Y = ¬X`

`¬X ∧ Y`

## Operator Precedence

The interpreter follows the following operator precedence rules:

1. Parentheses take precedence over all other operators.
2. NOT (¬) takes precedence over AND (∧) and OR (∨).
3. AND (∧) takes precedence over OR (∨).
