---
title: Group testing to save the world
layout: base
tags: ["public", "exploration", "maths", "computer science"]
---

The year is 2021. The world has been transformed into a post-apocalyptic wasteland. 
COVID-19 has been cured,
but one of the vaccines went horribly awry:
some of the people who got the Oxford-Zeneca vaccine started
frothing at the mouth,
indiscriminately biting people, 
and chanting *"Volker Halbach, Volker Halbach"*
before succumbing to their lack of qualia.

Two back-to-back pandemics were too much for the world to handle,
and the remnants of humanity have been reduced to
scavenging for GrabFood discounts,
unable to remember what the sun looks like.

But there is hope. A new screening test has been devised:
a perfect, infinitely sensitive test that
can detect whether someone has the virus in a matter of seconds...

---

You are an overworked civil servant at the Ministry of Health.
Your boss comes in one day 
(all Government offices have been relocated to
fortified underground bunkers to prevent *pzombie* attacks)
brandishing a couple of important-looking documents.

"New directive from the Minister---we need
to test every traveler that comes in.
Can you write me a proposal by today?"

What choice do you have? You get to work.

The proposal goes something like this:
All visitors to the country will have to line up at a testing booth.
When it's their turn they'll have to spit in a cup 
and then their secretions will be tested for the virus.
If they test negative, they're free to go;
otherwise, they'll be whisked away to a quarantine facility.
You bang it all out and send it to your boss.

![How to test travelers](/img/group_testing/queue.png)

You get a call the next day.
Your boss is aghast.

"We haven't got nearly enough tests
to test everyone who comes!" he shouts.

"Can we order more tests?" you ask.

"No, the whole world is out of tests."

You take a deep breath to calm yourself.

"The Minister wants us to test everybody that comes in, right?"

"Yes."

"But we don't have enough tests to test everybody?"

"Yes."

*What the hell do you expect me to do then?*
you think, but (wisely) stay silent.

If your boss had any shame he'd have the courtesy
to at least *look* sheepish, but you've learned not
to expect that from him.
In any case, he wants you to come up with a new proposal.
"Can you find some way to do it with fewer tests? As few as possible?"
You try to say something noncommittal but he's already hung up.

---

Clumps of your hair lie morosely on the table.
Testing everyone without enough tests for everyone?
How is that possible?

You review the evidence.
Preliminary findings suggest that 
out of every 1000 people, 
roughly 3 people will have the virus. 
Also, the test is infinitely-sensitive and perfectly accurate, 
so we can test as many people as we want with one test.

Then you have a flash of insight:

## 1. Can we share tests between two people?

Let's make one small change to the protocol.
Visitors will have to queue-up-and-spit---just as before---but 
now TWO visitors will spit in one cup.
This combined cup will then be sent for testing.
Because the test is infinitely sensitive, it will test
positive if either (or both) of the visitors have the virus.
If the combined test comes back negative, then neither visitor
has the virus, and they are free to go.
If it comes back positive, then at least one of the pair has the virus.
We then test each of them individually.

This two-visitors-one-cup protocol will save almost half
of the tests because most of the tests will come out negative.
Why is this so? 
The key here is that **most travelers don't have the virus.**

Let's use an example to illustrate. 

Suppose we have 1,000 travelers and 3 of them have the virus. [^1]
If you test them individually then you will use up 1,000 tests.
If you pair them up at random, however, one of the following
must be the case:

1. There are three pairs with one positive person,
   and 497 all-negative pairs.
2. There is one pair with two positive people, 
   one pair of one pair with one positive person,
   and 498 all-negative pairs.

In the first case, 
we will use 500 tests for each of the pairs.
Three of those tests will come out positive and we will use
an additional two tests for each of them. 
The total number of tests is
$500 + 3*2 = 506$.

In the second,
we will again use 500 tests for each of the pairs,
and use two additional tests for each of the two positive pairs,
for a total of
$500 + 2*2 = 504$.

In either case, we've cut the number of tests needed by almost half! 
This method only works because most travelers are negative,
and so most pairs will test negative.
If for example 800 people had the virus then
almost all of the pairs would test positive
and you would do better just testing everyone individually.

[^1]: Note that this method doesn't rely on knowing exactly how many people have the virus, only the expected value. If you knew that there were EXACTLY three people you could stop once you found three positives. For ease of exposition we illustrate an example where there are exactly 1,000 travelers and exactly 3 positive cases, but the method and the probabilities are very similar even if we work with expected values instead.

## 2. Can we share tests between even more people?

If two is good, surely three is better, four even better, 
and ten lagi-plus-chop better?
We'll group travelers into groups---of ten, say---
and get them all to spit into the cup.
Leaving aside how gross that is, doing so could save us even more
tests if most visitors don't have the virus. 
Assuming we only have three visitors with the virus,
there can be at most three positive groups *no matter the group size.*
Doing groups of 10 would mean at most thirty individual tests,
for an upper bound of $100 + (3*10) = 130$ tests.

But of course, there's an upper bound to how many people you can
put in a group.
If you get all 1,000 people to spit into a bucket and test *that*
you'll only have to do one combined test,
but that test is definitely going to come out positive
and you're going to have to test all 1,000 people.
In that case you haven't saved any tests at all. 

Now it turns out that we can calculate an optimal group size.
The fundamental trade-off of having bigger groups
is that you do less combined tests,
but have to do more individual tests when a combined test comes back positive.
Let's introduce some notation:

- Number of total people = $N$
- Number of infected = $K$
- Number of groups = $G$
- Number of people in each partition = $N/G = p$
   
In the worst case one has to do $G + (p * \min(K, G))$ tests.

Why is this so?
In the first step you need to test the $G$ groups.
And in the worst case, all $K$ of the groups will come out positive 
(ergo each positive group has exactly one positive person),
and you'll have to test each of those $K$ groups individually
which takes $p$ tests each.

We can prove by differentiation 
that the optimal number of people in each partition,
$p^{*}$, is given by $p^{*} = \sqrt{\frac{N}{k}}$.

Using the running example of $N=1000$ and $K=3$,
this would mean that the optimal group size is $\sqrt{333}$
which is something like 18.5. [^2] If we use $p = 20$ instead
(just so the numbers are easier to work with)
you would need $50 + (3*20) = 110$ tests at most
in the worst case, where you do 50 combined tests,
then test the 3 positive groups of 20 individually.

That's pretty awesome! By just grouping people together
we can decrease the number of tests needed by almost 90%,
from 1,000 to around 100.

You sketch out a diagram of how this group test approach
would work and email it to your boss with an explanation
He makes a couple of quick scribbles on it
and it's quickly distributed to Border Control:

![Handout to ministry workers](/img/group_testing/group_test_base_2.png)

[^2]: You can achieve an effective group size of 18.5 by having groups of 18 and 19.


For a while, all is well.
You've done the impossible with your great leap of insight
and your boss gives you an A in your performance appraisal.
Your meteoric rise through the ranks of the Civil Service
is all but assured, you think to yourself -- but alas,
Fate is never so kind...

---

You enter the Ministry one day and find it in an
absolute state of upheaval.

It is pandemonium.
People are screaming, jumping on desks, 
and smashing file cabinets:
files and papers litter the floor,
and your Director is bawling his eyes out.

"What happened here?" you ask,
and in between racking sobs he points to a
stack of papers on his desk:

> As part of the Digital Government Blueprint
> and the continuing economic difficulties
> caused by the post-pandemic pandemic,
> we call upon the Whole-of-Government
> to embark upon a Productivity Improvement and Digitisation Journey
> to increase WoG efficiency and reduce government expenditure...

Lesser men would have gotten hopelessly lost
in the thick thicket of Bureaucrat-ease,
but you realise the subtext immediately.
In order for your boss to keep his year-end bonus 
all his charges must demonstrate a 25% efficiency increase
---which means *you* have to reduce the number of tests by 25%.

You steal a furtive glance at your boss.
He seems to have recovered very quickly
and is now eyeing you expectantly.
You try to tell him that you've *already* saved him 90% of tests
but he's having none of it.
He quickly shoos you out of his office,
leaving you once again to do the impossible...

---

## 3. Can we share tests after the combined test comes back positive?

The current proposal is to test groups of 20,
and if any group tests positive,
test every single person in that group.
But must we test everyone individually once a group tests positive?
Can't we group people together again into subgroups of, say, 5?
And if that subgroup tests positive, can't we group people together *again*? 
And so on.

Here's an example. We have a group of 20 that tested positive.
We might then choose subgroups of 5 from that 20,
and start testing the first subgroup of 5.
If *that* subgroup tests positive we then split them
*again* into subsubgroups of 2 and 3, and if those subsubgroups
test positive we test them individually.
As before, if any group/subgroup/subsubgroup... tests negative
then we simply move on to the next one.

![Breadth-first search](/img/group_testing/breadth_first_search_2.png)

Does this actually save us tests?
Let's think about how many tests we would use in the worst case.
The worst case is when the positive tests are as
"spread out" as possible: that is, in different
groups/subgroups/subsubgroups.

So we test 50 groups of 20, using 50 tests.
In the worst case, three of the groups test positive.

When we get a positive group of 20 we
split it up into subgroups of 5.
There will be 12 such subgroups in total ($(20 * 3)/ 5 = 12$).
We test all 12, using 12 tests.
In the worst case, three of those subgroups test positive.

Again, when we get a positive subgroup of 5
we split them up into subsubgroups of 2 and 3.
There will be three subgroups of 2 and three subgroups of 3.

Again we test all six, using 6 tests.
Three of *those* subsubgroups test positive,
and because this is the worst case, all the positive subsubgroups
are of size 3.

Finally, we test each of those subsubgroups individually,
using $3*3 = 9$ tests, for a total of 
$50 + 12 + 6 + 9 = 77$ tests.

---

You've saved the day again!
You send the improved proposal to your boss and
pat yourself on the back for a job well done.

But while things are still fresh in your head 
-- and knowing your boss --
you reckon that you should think whether you can do *even* better
and accumulate a list of improvements
that you can continually dole out.
So you keep cracking...

---

## 4. Can we do better by picking the right sub/subsubgroup size?

You know from part 2 that choosing the right group size
makes a pretty big difference in the number of tests we need.
It stands to reason that the subgroup and subsubgroup sizes
also matter. But how should we pick these sizes?
In part 2 we calculated the optimal group size (20)
but in part 3 we picked the subgroup sizes 
arbitrarily (sizes 5 and 2).
Can we do better?

It turns out that we should halve the size of the (sub)group each time;
this is an idea very similar to *binary search*.
(The proof of why binary search is optimal can be found in the Appendix).

Concretely, we start with a group size of 20 
and first conduct a test on the first 10 of the 20 people
(i.e. the subgroup size is 10), 
allowing us to eliminate either these 10 people 
(if the test came back negative) 
or the other 10 people 
(if the test came back positive) [^3].

After the first test 10 people remain.
We conduct a test on the first 5 of the 10 people 
(subgroup size 5), 
allowing us to eliminate 5 people.
We continue doing so until we are left with a single person --- 
this person must be infected.

[^3]: The astute reader might pick up on the fact that both subgroups of 10 might test positive. But the odds of getting two or more positive elements in a group of 20 are very low, so in the vast majority of cases we will eliminate half of the people. (But see a more rigorous treatment in the Appendix!)

## 5. Can we do better by picking the right group size (again)?

We previously showed in part 2 that the 
ideal number of people in each group is $p = \sqrt{\frac{N}{k}}$.
However, that calculation hinges on the assumption 
that there is only one level of grouping before we test each person individually.
This isn't the case now, since we have many levels 
(specifically it's $\log_2 \frac{N}{p}$ levels, 
since we halve the number of people in a (sub)group after each test).

What is the new ideal group size $p$? 
Because we halve the size of the group each time,
we need (at most) $\log_2 \frac{N}{p} + 1$ tests per infected individual. 
And since there are $k$ infected individuals, 
we need a total of $G + k (\log_2 \frac{N}{p} + 1)$ tests: 
$G$ initial tests, then 
$\log_2 \frac{N}{p} + 1$ 
individual tests.
Using differentiation
we find that the optimal number of people in each partition,
$p^{*}$, is given by 

$$p^{*} = \frac{N}{k}.$$

Note how it is the *square* of the previous value

$$p^{*}_{old} = \sqrt{\frac{N}{k}}.$$

Importantly, this new group size is larger than the previous group size,
which makes a lot of intuitive sense.
Remember that the fundamental group size trade-off is that if you
make your group size too large, you will expend a lot of tests
testing every one individually (subgroups of 1).
But in our refinements of the method we have managed to use fewer tests
by choosing the right subgroup size.
The optimal group size therefore increases.
(And for our case of $N = 1000$ and $k = 3$, 
the optimal group size is $p^{*}=333$).

## 6. Depth-first search: should we "reset" the search after we've found an infected person?

Previously, we were testing all 50 groups of 20 before testing the 12 groups of 5, 
and testing all the 12 groups of 5 before testing the 6 groups of 2 or 3.

There is another way to do it, though.
We could test groups of 20 until we find a group of 20 that tests positive.
Once we find a positive group of 20 we test groups of 5 from that 20 
until we find a group of 5 that tests positive, 
and from that group test the groups of 2 and 3, and so on.
Only when we find an infected individual do we go back up a level.

Here's an illustration of what that looks like:

![Depth-first search](/img/group_testing/depth_first_search.png)

This is called *breadth-* vs *depth-* first search.
In breadth-first search, we explore all groups of the same size before exploring
groups of smaller sizes (i.e. deeper levels). But in depth-first search, we
make our way to the first infected person as quickly as possible, before
backtracking to find the next infected person, and so on.

Does it matter whether we use depth- or breadth-first search? 
It turns out that depth-first search opens up some further
optimisations.
The idea is that once we find the first infected individual 
we can stop and "reset" the search, using fewer tests overall.

Suppose we conduct our tests, using the depth-first search procedure, 
pausing just after we have identified the first infected individual
(in our example, it is the 13th person).
But note here that we have no information whatsoever
about the people behind the 13th person.
More specifically, we know that persons 1 to 12 are not infected, 
and (of course) that person 13 is infected, 
but we don't know anything about whether any of the subsequent people are infected.
This is because subsequent infected people don't 
affect any of the test results obtained so far by the procedure.
This means that persons 14 to N are equally likely to be infected; 
it is as if we never did any tests on them at all.

In our current procedure, after finding that the 13th person is infected, 
we backtrack and test the 14th and 15th persons together (size 2)
then back out further and test the 15th to 20th person (size 5).
But if you think about it, 
we have no information about the 14th to 20th people,
and as such have no reason to test them in small groups.
These two tests will very likely be negative!
It would be similar to doing individual testing 
when we know that most people will test negative.

The key insight here is to "reset" the search.
Since persons 14 to N are equally likely to be infected, 
we arrive at a smaller instance of the same original problem --- 
there are $1000-13=987$ people that we want to test, 
of which $3-1 = 2$ of them are infected!
It then follows that we should perform an identical procedure 
on these remaining people --- 
we recalculate the new value of $G$ (and hence $p^{*}$), 
and proceed with the procedure with those new values.

---

All the optimisations lead you to the final, optimal algorithm:

1. Set the optimal group size as $p = N/k$. 
   Pick the first $p$ people, group them together and test them.
2. If that group tests negative, remove all of these people, and repeat the
   algorithm with $N$ now set to $N-p$.
3. If that group tests positive, take a subgroup of the first half of those people and
   test them: 
    - If that subgroup tests negative, clear them and test the first half of the other subgroup.
    - If that subgroup tests positive, test the first half of the subgroup.
    - In either case, repeat this process until we get to a single person.
4. Remove all the people before and including the first positive person, 
   repeating the algorithm and setting $N$ and $k$ appropriately. Repeat this
   process until everyone has been cleared or quarantined.

---

You smugly file the optimal algorithm away,
content in the knowledge that you'll be able
to appease your boss and exceed your KPIs
for many months to come. You're feeling very clever with yourself,
but unbeknownst to you
Hwang (1972) beat you to it almost fifty years ago with his paper
_A Method for Detecting All Defective Members in a Population by Group Testing_.
Maybe you should have studied something useful instead of PPE...

---

The next few months pass uneventfully.
You spend your working hours writing florid poetry on the human condition,
until one day your boss barges into your office.

"Your testing method is taking too long!
People are dying before they even get to the front of the line.
Can you come up with a way to do the tests in parallel?"

(TO BE CONTINUED..?)

---

## Acknowledgements

This piece was a collaboration between me and Bernard.

## Appendix

### Why halving the group size each time is optimal

Each group that tests positive is quite likely to have only one infected individual, 
because there are more groups than infected individuals.
Suppose you rolled twenty 100-sided dice (d100): 
the odds of getting one 
100 is quite rate, but the odds of getting two or more 100s
is vanishingly unlikely.
In the same way,
since an individual is very unlikely to have the virus,
it is quite rare for a group to have an infected person,
and extremely rare for a group to have two (or more) infected people.

Let's assume for now that each group that tests positive 
has exactly one infected individual.
Our objective, then, is to determine which one of the 20 people 
in this group is infected with the minimum number of tests,
and this is optimally done by halving the group size each time.

To see why halving the group size each time 
consider what would happen if we first 
conducted a test on 5 (instead of 10) of the 20 people in the group.
If the test comes back positive, then we get to eliminate a whopping 15 people!
But if the test comes back negative, then we can only eliminate 5 people.
On average, then, what is the number of people that we will get to eliminate?

If you've answered "10 people", that's unfortunately wrong.
Since the infected individual has an equal chance 
of being each of the 20 people in the group, 
it is more likely that the the infected individual 
is in the untested 15 remaining people 
rather than the 5 people we conducted a test on.
This means that it's more likely that 
we will only get to eliminate 5 people, rather than 15.
As such, the average number of people 
that we get to eliminate is less than 10.

We may make a similar argument if 
15 people are chosen for the first test, instead of 5 or 10.
The average number of people that we get to eliminate 
will also be less than 10.

Hence, testing exactly half of the group 
is the most efficient way to narrow down the group size.
