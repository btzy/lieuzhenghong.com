---
title: Group testing to save the world
layout: base
tags: ["public", "exploration", "maths", "computer science"]
---

> The year is 2021 and the world has been transformed into a post-apocalyptic wasteland. 
> Due to a global pandemic the remnants of humanity have been reduced to
> scavenging for GrabFood discounts, unable to remember what the sun looks like.
> But there is hope. 

The year is 2021. The world has been transformed into a post-apocalyptic wasteland. 
COVID-19 has been cured,
but one of the vaccines went horribly awry:
some of the people who got the Oxford-Zeneca vaccine started
frothing at the mouth,
indiscriminately biting people, 
and chanting *"Volker Halbach, Volker Halbach"*
before succumbing to their lack of qualia.
Two pandemics in a row was too much for the world to handle,
and the remnants of humanity have been reduced to
scavenging for GrabFood discounts, unable to remember what the sun looks like.
But there is hope. A new screening test has been devised:
a perfect, infinitely sensitive test that
can detect whether someone has the virus in a matter of seconds.

You are an overworked civil servant at the Ministry of Health.
Your boss comes in one day 
(all Government offices have been relocated to
fortified underground bunkers to prevent *pzombie* attacks)
brandishing a couple of important-looking documents.

"New directive from the Minister---we need
to test every traveler that comes in.
Can you write me a proposal by today?"

What choice do you have?
The proposal goes something like this:
All visitors to the country will have to line up at a testing booth.
When it's their turn they'll have to spit in a cup 
and then their secretions will be tested for the virus.
If they test negative, they're free to go;
otherwise, they'll be whisked away to a quarantine facility.
You bang it all out and send it to your boss.

`<image here of a testing booth and a long line of people queuing up>`

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

Then---it comes to you. 
Since the test is infinitely-sensitive
and perfectly accurate, we can test as many people
as we want with one test!
And this makes all the difference:

## 1. Can we share tests between two people?

Let's make one small change to the protocol.
Visitors will have to queue-up-and-spit---just as before---but 
now TWO visitors will spit in one cup.
This combined cup will then be sent for testing
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
   and 498 all-negative pairs;

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
and ten double-plus-good better?
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
The fundamental trade-off having bigger groups
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

`<diagram to show upper bound of tests where k = 3?>`

[^2]: You can achieve an effective group size of 18.5 by having groups of 18 and 19.

That's pretty awesome! By just grouping people together
we can decrease the number of tests needed by almost 90%,
from 1,000 to around 100.

## 3. Can we share tests after the combined test comes back positive?

You're feeling pretty pleased with yourself but you wonder if you can do better.
Recall that the current proposal is to test groups of 20,
and if any group tests positive,
test every single person in that group.
But must we test everyone individually?
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

`<diagram here would be very helpful>`

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
using $3*3 = 9$ tests.

How many tests have we used in total?
$50 + 12 + 5 + 9 = 76$.

`<really need a diagram>`

One way you can think about it is that this algorithm 
finds the position of the *first* positive person, and
repeating it on all the elements will eventually give us 
all the positive positions.
Thinking about the algorithm in this way will come in useful later.

Here's a diagram:

`<diagram here>`

## 4. Can we do better by picking the right sub/subsubgroup size?

You know from part 2 that choosing the right group size
makes a pretty big difference in the number of tests we need.
It stands to reason that the subgroup and subsubgroup sizes
also matter. But how should we pick these sizes?

Well, each group that tests positive is quite likely to have only one infected individual, because there are more groups than infected individuals.  Let's assume for now that each group that tests positive has exactly one infected individual.  Our objective, then, is to determine which one of the 20 people in this group is infected.

It turns out that we should halve the size of the (sub)group each time.  (If you have heard of binary search, this is precisely the algorithm being described here.)
That is, we start with a group size is 20 (of which we know exactly one person is infected),
and we first conduct a test on the first 10 of the 20 people (i.e. the subgroup size is 10), allowing us to eliminate either these 10 people (if the test came back negative) or the other 10 people (if the test came back positive).
After that, of the remaining 10 people, we conduct a test on the first 5 of the 10 people (i.e. the subgroup size is 5), allowing us to eliminate 5 people.
We continue doing so until we are left with a single person --- this person must be infected.

`<diagram>`

To see why this is optimal, consider what would happen if we first conducted a test on 5 (instead of 10) of the 20 people in the group.  If the test comes back positive, then we get to eliminate a whopping 15 people!  But if the test comes back negative, then we can only eliminate 5 people.  On average, then, what is the number of people that we will get to eliminate?

If you've answered "10 people", that's unfortunately wrong.  Since the infected individual has an equal chance of being each of the 20 people in the group, it is more likely that the the infected individual is in the untested 15 remaining people rather than the 5 people we conducted a test on.  This means that it's more likely that we will only get to eliminate 5 people, rather than 15.  As such, the average number of people that we get to eliminate is more than 10.

We may make a similar argument if 15 people are chosen for the first test, instead of 5 or 10.  The average number of people that we get to eliminate will also be more than 10.

Hence, testing exactly half of the group is the most efficient way to narrow down the group size.

All the things we have said will work fine when there's just one infected individual in the group, but we can't guarantee it even though it would be the case most of the time.  How do we modify this procedure to work even when there are more than one infected people?

Let's first consider what the above procedure does when there are multiple infected individuals in the group.  Which person would the above procedure identify?  Since we conduct testing on the _first_ half of the (sub)group each time, and make decisions based on whether this half tests positive, the above procedure will identify the _first_ infected individual.

`<diagram showing that the procedure identifies the first one>`

Notice that the procedure gives us totally no information about the people behind the first infected individual.  In other words, suppose the procedure tells us that the M^th person is the first infected individual.  Then we know that persons 1 to (M-1) are not infected, and (of course) that person M is infected, but whether each of persons (M+1) to G is infected never affects any of the test results obtained by the procedure.  This means that persons (M+1) to G are equally likely to be infected, and it is as if we never did any tests on them at all.

It is then intuitive to treat the people (M+1) to G as a new group, check (with a single test) if there is at least one infected individual, and if so, repeat the binary search procedure on them.

`<diagram>`

It turns out that this intuition is correct.  There are $K$ infected individuals, and we need $\log \frac{N}{G} + 1$ tests per infected individual, so we need a total of $G + K (\log \frac{N}{G} + 1)$ tests, or alternatively in terms of $p$ we need $\frac{N}{p} + K (\log p + 1)$ tests.  

Again using differentiation, we can show that the optimal number of people in each partition,
$p^{*}$, is given by $p^{*} = \frac{N}{k}$.

TODO


we want to do something akin to a binary search, to identify that positive person.  In other words, we want to half the size of the (sub)group each time.
That is, if our group size is 20,
then the subgroup size should be 10,
subsubgroup size 5,
sub^3group size 2.5, and so on (rounding fractional values to the nearest integer).





Why? Recall from the diagram in part 3 that our algorithm finds 
where the first positive person is. 
You can think of all of the people in a line and us trying to find
where the first positive person is on that line.
Once we find the first positive person the algorithm can be run again
to find the 2nd, 3rd, ... kth positive person.

Now suppose we have a group size of 20 and we have a positive group of 20.
Initially there are 20 possibilities where the first positive person might be.
By splitting into subgroups we are essentially trying to find
the first positive as quickly as we can.
For instance, if we test the first subgroup of 5 and it comes back negative,
we know that the first positive person must lie from the 6th person onwards.
And if we test the first subgroup of 5 and it comes back negative we
know that the first positive person must be one of the first 5.

It turns out that the best way to eliminate all the possibilities
is to split the group size into half each time.

Why is this so?

Think about having a group of 20 and a subgroup of 5.
Now it's possible that the first subgroup tests positive,
in which case we know that the first positive person
lies in the front 5. This means we can eliminate 15 possibilities.
But of course it's more likely that the subgroup tests *negative*
(since the first positive person has an equal chance of being in
any of the 20 positions)
and we can only eliminate 5 positions 
(ergo there are still 15 possibilities for the first positive).

On the other hand, if we used a subgroup of 10, 
then we can eliminate 10 possibilities 
for the first positive person
no matter whether the subgroup tests positive or negative.

Implementing the new algorithm gives the following
number of tests in the worst case scenario:

- 50 tests (of size 20), 3 positive
- 6 tests (of size 10), 3 positive
- 6 tests (of size 5), 3 positive
- 3 tests of size 2 and 3 of size 3, 3 positive
- 9 tests of size 1

$50 + 6 + 6 + 6 + 9 = 77$

Hmm, that's strange, how come the number of tests needed
went up?
It turns out that the optimal group size
that we calculated in the previous part is no longer optimal.
Recall that the fundamental trade-off in having bigger groups
is that you do less combined tests,
but have to do more individual tests when a combined test comes back positive.
Previously our optimal group size for $N = 1000$ and 
$k = 3$ was 20. If a group of 20 tested positive
we then needed 20 subsequent tests to identify the positives.
But with our new repeated-halving testing protocol
we will use a fraction of that on average.

Since we now have a more efficient way to 
do the subsequent tests, our optimal group size is now larger.

How much larger?
It turns out that when $k$ is relatively small compared to
$N$ the ideal group size $G$ is $N/k$.
That means that our new optimal group size is
$N/k = 333$.
How many tests would we need in the worst case?
Enumerating:

- 3 tests of size 333, 3 positive
- 6 tests of size 162, 3 positive
- 6 tests of size 81, 3 positive
- 6 tests of size 41, 3 positive
- 6 tests of size 21, 3 positive
- 6 tests of size 11, 3 positive
- 6 tests of size 5, 3 positive
- 6 tests of size 3, 3 positive
- 9 tests of size 1, 3 postiive

$3 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 9 = 51$

## 5. Can we do better by dynamically choosing sub^Ngroup sizes? 

## 6. The final algorithm

1. Set your group size to be $G = N/k$. Pick the first $G$ people, group them
   together and test them.
2. If that group tests negative, remove all of these people, and repeat the
   algorithm with $N$ now set to $N-G$.
3. If that group tests positive, take a subgroup of half of those people and
   test them: 
    - If that subgroup tests negative, clear them and test the next subgroup.
    - If that subgroup tests positive, take a sub-subgroup of half of the subgroup
        and test them, repeating this process.
4. Remove all the people before and including the first positive person, 
   repeating the algorithm and setting $N$ and $k$ appropriately. Repeat this
   process until all people have been cleared.

You're feeling very clever with yourself until it turns out that 
Hwang (1972) beat you to it almost fifty years ago with
_A Method for Detecting All Defective Members in a Population by Group Testing_.
Oh well. Maybe you should have studied something useful instead of PPE.


## Sequence of events

1. Frame story: you're the Minister for Health of a small island nation and you
   need to test everyone who comes into the airport. 
   Your boss wants you to come up with a proposal.
2. Your first proposal is to just test everyone.
3. Your boss is aghast. "We can't test everybody, we don't have enough tests!"
4. So you think, Oh, can we mix everyone's saliva together and test?
    Turns out that you can because the test is very sensitive.
5. So in your second proposal you suggest that we group 2 people together, get
   them to spit in the same cup (or whatever), and do a test on that combined
   sample. 
   (INCLUSIVE OR IDEA HERE)
   And the idea is, that if the test comes out negative, both those people are 
   negative,
   and if the tests comes out positive, *at least one* of those people is positive.
   And assuming that most epople don't have the virus, this allows us to
   halve the number of tests! (Short proof here.) 
   - With some loss of generality let's assume that there's only three people
     who's positive in 1000. (We'll see how to extend this to other numbers later.)
6. Ok, but can we do better? If two is good, surely three is better, four even
   better, etc. What about 10? And the intuition here is that most of the
   partitions are still going to come out negative.
   And at the most, with a partition of 10, we'll have to test 30 people maximum.
   But of course there's an upper bound. If you get all 1000 people to spit into
   the same cup then that test is definitely going to be positive, BUT you're
   going to have to test all 1,000 people. So you haven't saved any tests at
   all.
   In some sense the formula is as follows:
   - Number of partitions = p
   - Number of people N
   - number of people in each partition = N/p
   - Number of infected = k
   
   So the formula is that you'll have to , in the worst case,
   do
   p + N/p * k
   In the first step you need to test all the partitions
   And in the worst case, *k* of the partitions come out positive and you'll
   have to test all of them.
   And minimising this (by differentiation or AM/GM)
   gives us .... $p = \sqrt{Nk}$.
6. (Extra intermediate step). 
    So one very obvious improvement is that we don't test every single person individually when the group tests positive.
    We can split that positive group into subgroups and test *those*. 
    I.e. for instance if we chose groups of 20 at the start,
    and a group of 20 tested positive,
    We might then choose subgroups of 5,
    and if *that* subgroup tested positive we might then split them 
    *again* into subsubgroups of 2 and 3,
    and if *that* subsubgroup tests positive we'll then test them individually.
    And by the same logic as previously this will allow us to reduce the number of tests.
    (Here we should make it clear that this algo finds the position of
    the first positive, and running it recursively on the remaining
    elements will eventually give all the positives.)
7. How do we choose the size of the subgroup/subgroupgroups/etc... to test? 
    What's the ideal? 
    So we're trying to find where the first positive is and there are 20
    possibilities where the first positive might be.
    Now in order to find the first positive as efficiently/quickly as possible,
    we want to eliminate the most number of possibilities at every step.
    And it turns out that the best way to do it is to split the group into half each
    time.
    Why is this so?
    Imagine for now we had a group of 20 and we query a subgroup of 5.
    Now it's possible that that subgroup of 5 tests positive
    (in which case we can be sure the first positive lies in the front 5)
    but it's more likely that the subgroup tests negative
    and we can only eliminate 5 elements 
    (ergo there are still 15 possibilities for the first positive)
    Now if we used a subgroup of 10, then we can eliminate 10 possibilities 
    for the first positive
    no matter whether the subgroup tests positive or negative.
8. So here's how it works: 
    For each positive partition we test
    the front half of that partition. 
    If it's negative we know that everyone in the
    front partition is negative and we can send them home---any positive
    cases must be in the back half. 
    Then we test the front half of that back half..
    (TODO: diagram)
    If it's positive then we halve that again, test the front half etc.
    Eventually we'll reach a subgroup of size 1 or 2 and then we'll just test individually.
    This eventually finds the first positive patient. (why? diagram)
9. We should then ask if our initial partitioning of $p = \sqrt{nk}$ was ideal.
    (No.) Why not? 
    So in our initial solution, whenever we found a positive
    partition, we had to individually test every single person in that partition.
    But now in step 7 we've been able to get the right answer with much fewer tests.
    And therefore our partitions can be larger.
    But how much larger?

    So recall in step 7 that we chose the size of the subgroup in order to halve
    the number of possibilities at each step.
    So no matter whether the subgroup returned positive or negative, half of
    the possibilities would be eliminated.
    Now that's equivalent to saying that we chose the size of the subgroup
    *such that there would be a 50% probability that it would be positive* [^0]
    And this same logic applies to the initial partitioning as well.
    We want to choose a size of the initial group such that there's a 50%
    chance of the initial group returning positive.

    [^0]: not quite true --- assuming a uniform distribution

    And it turns out (maybe we want to derive this) that the optimal group size
    to choose in order to return a 50% chance is roughly $n/k$ (proof).
11. So with all that said, the final algorithm you come up with is as follows:
    1. Set your group size to be $g = n/k$. Pick the first $g$ people, group them together and
    test them.
    2. If that group tests negative, remove all of these people, and repeat the algorithm with n now set to $n-g$.
    3. If that group tests positive, take a subgroup of half of those people and test
    them: 
    - If that subgroup tests negative, clear them and test the next subgroup.
    - If that subgroup tests positive, take a sub-subgroup of half of the subgroup
        and test them, repeating this process.
    4. Remove all the people before and including the first positive person, repeating the algorithm and setting k to $k-1$ and n appropriately. Repeat this process until all people have been cleared.

12. You're feeling very clever with yourself until it turns out that Hwang
    (1972) beat you to it almost fifty years ago with 
    _A Method for Detecting All Defective Members in a Population by Group Testing_ .

13. All is well and good until you get a call from your boss a few days later.
"The queue at the testing station is getting way too long; 
we've had several passengers die of Covid while waiting to be tested.
We're going to greatly increase the number of testing stations.
Can you make your algorithm run in parallel?"


=== 


Now a question might come up at this point. Why half?
Suppose we drew like 30 partitions of 1,000
The probability of a partition having exactly ONE positive is low
and the probability a partition having TWO positives is even lower,
sort of like when you're rolling like a d20 getting a 20 vs rolling 2 d20s and
getting both 20s. So we can kind-of-safely say that the parttion is MOST likely
going to have ONLY one positive if the partition tests positive.

9. So what? So if we assume that the partition only has one positive patieent,
then if we divide the partition into half, ONLY one half will be positive.
While this assumption doesn't always hold, because almost always we have
only 1 positive patient,
P(front half is positive) ~= 0.5.
In other words, consider a positive partition. If we test the front half (or the
back half for that matter), there is an approximately 50% chance that the test will return a positive result.

So here let's look at a partition of 8. And recall in 7 that this algorithm
finds the first positive patient. Before making any queries there are 8
possibilities where the positive patient is.
And when you split that into half, you find out if the patient is from 1--4 or
5--8. In either case the number of possibilities is halved. 
And everytime you do it it halves again.

Recall that previously we had 8 possibilities and we chose to halve it (4/4),
(2/2) and so on. We do this by choosing a set that has a 50% chance of being
positive, and we want to do the same for the first step as well.

Because each partition is so much more likely to return negative
than positive (just look at the diagram). We can see that out of X partitions of
size 8, only Y of them were positive (max 3 out of however many).

===

7. OK, but can we do better again?  So the idea of splitting up the groups into
subgroups in Stage One was that we wanted to strike a balance between
testing everybody (i.e. subgroups of 1), while not getting a "guaranteed"
positive test (i.e. subgroups of 1000.)
And so it would make very little sense if we abandoned this idea in the second
stage, and just tested eveyrone in the group.
In some sense the first stage removes people from consideration and we can
consider the second stage a same reduced group, and the same logic applies.
So e.g. instead of 1,000 people now there are 50 people to test.
And with 50 people to test we don't have to test individually, we can split
*that* into groups as well. 
8. This leads us to a *multi-stage testing approach...* at every juncture we
   split each into a subgroup.

