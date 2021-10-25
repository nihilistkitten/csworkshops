---
title: "00-Principles of Good Code"
geometry: margin=1in
...

We're going to start by looking at an example of very bad code:

```{.python include=000-fib-bad.py}
```

Question: what does this code actually do?

Brainstorm: what are some issues with this code?

We're going to step through a series of so-called "refactorings" (meaning, basically, changes to the code that don't effect its behavior) to improve this code.

_(Note: feel free during the discussion to go in a different order based on the issues pointed out by people in the workshop. The idea is to use this document as a guide, but make all the edits live in one file.)_

## Loops

This code does the same thing a bunch of times. We can easily rewrite this in a loop:

```{.python include=010-fib-loop.py}
```

This is an example of a basic principle of coding, called "Don't Repeat Yourself," or _DRY_.

Brainstorm: Why is DRY a good idea?

- Later refactors
- Error proneness
- Readability (the same thing is in the same place)

Brainstorm: When might DRY be a bad idea?

- Potential for future divergence

WET, or "write everything twice", is an alternative to DRY. It holds that the first two duplications might be a coincidence, but the third probably indicates there's some fundamental commonality between the problems you're trying to solve.


## Naming

This code is still not particularly readable. One problem is the variable names: `i`, `j`, and `k` are not particularly easy to keep track of. Imagine if this code was hundreds of lines long: you'd want to know which is which.

Question: suggestions for better names?

```{.python include=020-fib-rename.py}
```

This is an example of a _readability_ refactor.

Brainstorm: why do we care about readability?

- code review
- other maintainers
- future you

Two things to keep in mind with variable names:

- _Convention_. The names `prev` and `curr` are conventionally used for this kind of iterative procedure when you need to keep track of the two previous values. Many programmers will automatically know the meanings of variables like `prev` and `curr` just from their names because they've read other code that used those same conventions. Other examples of this: `n` for some kind of bound, `ret` or `out` for the value that's going to be returned at the end, `self` for an instance of a class in a method. In 121 we've used `xs` for a list of numbers.
- _Length_. Avoid one-letter names except in rare cases (a very short loop index, or `n` for a bound). Also avoid unnecessarily long names like `the_fibonacci_number_that_i_calculated_previously`.


## Spacing

Another readability issue: this code doesn't use any spacing between operators. Here's a better version:

```{.python include=030-fib-spacing.py}
```

This is just visually easier to read, with clearer separation between variables. A second change I made is moving `count = 0` a line down, to emphasize its relationship to the `while` loop.

In fact, there's a whole encyclopedia of python formatting conventions, called "PEP 8" (PEP means "Python Enhancement Proposal"), and different universities and companies each have their own modifications and additions to these. You don't need to be so stringent in your own code, but it can be good to know.

There are also tools that can automatically handle things like this kind of formatting for you. We'll talk about these more in another workshop, but I recommend the command-line tool `black` for python.

## Commenting

Comments make our code infinitely more readable by explaining in spoken language exactly what the code is doing.

```{.python include=040-fib-comment.py}
```

A few things to note:
- On top is a _docstring_, or "documentation string". This is a special type of comment, written as a triple-quoted string, and placed on top of a file, function, or class. Its purpose is to explain what the thing it documents does, without getting in to any of the details, so that anyone interested in using that object doesn't need to understand the implementation in order to understand how to use it.
- Comments can explain what the code does or how it does it, i.e. the comment which talks about simultaneous assignment.
- There is such a thing as overcommenting (to be honest, this example is probably overcommented), but it's way harder to overcomment than undercomment.

Brainstorm: why might overcommenting sometimes be bad?

## For Loop

To do the same thing some number of times, the convention is to use a `for` loop, instead of a `while` loop, like so:

```{.python include=050-fib-for.py}
```

Note the special variable `_`. This is a conventional variable name for when your variable isn't actually used, but is just there to count something else. If we relied on the value of the counting variable to perform our computation, we could call it something like `count` or `index`.

## Function Abstraction

Right now, all our code is just sitting at the top level of our file. We should separate each piece of logic into its own function, like so:

```{.python include=060-fib-fn.py}
```

Note that I named the functions and their arguments descriptively, just like the variable names from before. Also note that I wrote a short docstring describing what each function does.

How does python read this code? First, it sees that you've defined these two functions, so it stores their code in its memory. Then, it sees that you call `print_first_n_fib(8)`. So then it runs the code it had previously stored for `print_first_n_fib`, except it substitutes `n` (the function's argument) with `8`). It does something similar each time it sees `fib_step`: it knows the code that `fib_step` corresponds to, so it runs that code with the arguments it's called with. 

Brainstorm: why are functions helpful here?

- abstraction
- code reuse (helps with DRY)
- testing!

## Single Responsibility

Right now, our `print_first_n_fib` function has two jobs: it's both responsible for _computing_ the first n Fibonacci numbers, and for _printing_ them to the terminal. Let's say that tomorrow, the powers that be decided that our code needs to compute the sum of the first 8 Fibonacci numbers, instead of just printing them out. Or, say we needed to write them to a file, instead of printing them. We would need to look through our code for actually computing the Fibonacci numbers (the process for which hasn't changed) in order to make either of these changes.

Instead, we can refactor our code like so:

```{.python include=070-fib-list.py}
```

Now each of our functions has a single responsibility: `first_n_fib` is responsible for _computing_ the Fibonacci numbers, and `print_list` prints each item in an _arbitrary_ list, which, in this case, is our list of Fibonacci numbers. If we need to print another list, we can reuse the code we wrote for `print_list`, and if we need to do some other computation on the Fibonacci numbers, we can reuse the code to compute the first `n` numbers.

This is an example of the "Single Responsibility Principle", or _SRP_. The SRP says that each function or class should be responsible for a single thing. What a "thing" means here is often left kind of vague and left to your best judgement. Another way to think of this principle is that each piece of code should have only a single reason to change: `first_n_fib` only changes if the definition of the Fibonacci numbers changes, `print_list` only changes if we decide there's a better way to print out lists (say, separated by commas, instead of newlines), and the code at the bottom changes in response to changes in the high-level requirements of our code; e.g., it could call a function `save_list_to_file` instead of `print_list`.

As an aside, by some measures, this code is actually worse than what we had before. It'll be slightly slower (though not asymptotically so), and it requires (even asymptotically) more storage space on the disk than the previous version did. There are some fancy techniques, for instance something called "dependency injection", or a python feature called "generators", that you can use to get around this without violating the SRP, but I generally prefer readable/maintainable code even at slight performance costs. If it turns out that this code is extremely performance-sensitive, and that this is the major bottleneck in your program, you can always refactor it later.

## Testing

A major, major advantage of the SRP is _automated testing_. Here, we're going to use a tool called `pytest`, a very standard tool for automatic testing of python code. You can probably install it with `pip3 install -U pytest`. We'll talk more about testing in a future workshop, but the basic idea is that `pytest` looks for functions whose names start with `test_`. We can use the special `assert` keyword inside these functions to cause a test to fail if any arbitrary condition is false. Note that we couldn't have written code like this before we did the SRP refactor: `print_first_n_fib` didn't return anything, and testing printed output is much, much harder than testing return values.

```{.python include=080-fib-tests.py}
```

Because our tests are in the same file as our code, we run pytest like `pytest fib.py` from the command line. You could also put your tests in their own file, called something like `test_fib.py`; as long as it starts with `test_` pytest will find it automatically. Again, we'll talk more about testing later, but it's super helpful for refactoring so we wanted to mention how it works: now we can run our tests after each refactor to make sure the refactor didn't break the part of our code that's tested.


## More modularity

We sort of have some code duplication here: `prev` is responsible for storing the previous value of `curr`, but that's _already_ stored, in `ret`. We can actually eliminate our use of `curr` and `prev` altogether: 

```{.python include=090-fib-more-modularity.py}
```

And... our tests fail! Good thing we had them. We might've been able to spot this issue here, but maybe not for more complicated cases.

Pytest tells us exactly what went wrong: for all three of our tests, we output two more Fibonacci numbers than we asked for. So the problem must be with the bounds of our `for` loop, since that's what determines how many numbers we compute. Notice that we now start with two items in our list `ret`, but we still compute an additional `n`, one for each iteration of the loop. So we need to adjust the loop accordingly:

```{.python include=100-fib-fix-one.py}
```

Two of the tests pass, but one still fails. We can see the issue: there's nothing preventing it from returning the two seed values with `n=0`.

First, thinking about this issue, we notice it's still a problem for `n=1`, so we'll add another test for that case:

```python
def test_first_n_fib_1():
    """Test that `first_n_fib` is correct for n=1."""
    assert first_n_fib(1) == [1]
```

So here's a solution that works:

```{.python include=110-fib-fix.py}
```

But this is unnecessarily complex; special cases tend to be hard to read. So maybe our instinct to refactor out `curr` and `prev` was wrong, and that's ok! Our tests and our knowledge of code design principles helped us reject this refactor.
