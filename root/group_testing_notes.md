## Sequence of events

> The year is 2021 and the world has been transformed into a post-apocalyptic wasteland. 
> Due to a global pandemic the remnants of humanity have been reduced to
> scavenging for GrabFood discounts, unable to remember what the sun looks like.
> But there is hope. 

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
