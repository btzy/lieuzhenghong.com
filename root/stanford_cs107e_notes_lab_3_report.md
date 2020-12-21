---
title: Report on CS107E Lab and Assignment 3
layout: base
tags: ["public", "computer science", "programming"]
---

## Writing a `strcpy` function

This was a pretty easy task

## Debugging with GDB

## More assembly

```c
void stack_array(void)
{
    char array[32];         // not initialized before read
    
    // printf("array[] = {");
    for (int i = 0; i < 5; i++) {
        printf(" 0x%x ", array[i]);
        array[i]++;     // increment starting from garbage
    }
    // printf("}\n");
}
```

This compiles into the following assembly code:

```arm64
stack_array:
    stmfd sp!, {r4, r5, r6, lr}
    sub sp, sp, #32
    mov r5, #0
    b .L2
.L3:
    add r3, sp, #32
    add r6, r3, r5
    ldrb r4, [r6, #-32] @ zero_extendqisi2
    mov r1, r4
    ldr r0, .L5
    bl printf
    add r4, r4, #1
    strb r4, [r6, #-32]
    add r5, r5, #1
.L2:
    cmp r5, #4
    ble .L3
    add sp, sp, #32
    ldmfd sp!, {r4, r5, r6, lr}
    bx lr
.L5:
    .word .LC0
.LC0:
    .ascii " 0x%x \000"
```

What is happening in `.L3:`

`r5` is `i` and `r4` is the current value of `array[i]`
So what we do is we load the value in the address pointed to at `r6` minus 32
into `r4`, we increment it, then we store it back into that address.
Note that at every loop `r6` is being added to 
Note also that the array is being added from the back.


`stmfd`

`ldmfd sp!, {r4, r5, r6, lr}`
stores the first four words
of the stack pointer into those four registers

If the stack is descending you use
`fd` to do full descending
otherwise you use `fa` instead

> So, the instruction

```ldm r4!, {r0, r1, r2, r3}```

can be represented by the following pseudocode:

```c
r0 = *(int)(r4) 
r1 = *(int)(r4+4) 
r2 = *(int)(r4+8) 
r3 = *(int)(r4+12) 
r4 = r4 + 16 // writeback (16 bytes transferred)
```

> In the variant without ! the writeback doesn't happen so R4 retains the original value.


## Serial communication

## Lab 3: Check-in

### Explain how the lr register is used as part of making a function call. Which instruction writes to the lr register? Which instruction reads from it? What commands could you use in gdb to observe the changes to the lr register during execution of a function call?

The `lr` register is the link register.
You store the 

```arm
bl loop
add r1, #1
mov lr #500 @ this stores 500 into LR

loop:
@ do some stuff
@ ...
bx lr @ jump back to `add r1, #1`
```

One thing the prolog here `stmfd sp! {r4, r5, r6, lr}` does
is to support nested functions.
Since we only have one `lr` register,
if we had a function calling another function
the previous `lr` would get overwritten
and we wouldn't be able to jump back to the grandparent function.
That's why you store the `lr` at the start of the stack
when a function is called
and load it back into `lr` after the function has returned
and that allows you to go back to your grandparent.

The `bl` instruction writes to the lr register
but you can also use instructions like `mov` to write to the lr register
since it's just another register (register 14).
The `bx lr` instruction reads from the lr register.
(it actually reads from any register).

We could use `disassemble` to look at 
the source code of the function currently in scope
and also points to the current line.
We can use `info reg` to look at the registers
and `step` to go stepwise and keep using `info reg`
to observe the changes in the `lr` register.
    
### Why is it necessary to plug in both TX and RX for loopback mode to work?

If you don't plug in TX to RX you either don't receive the transmitted messages
or you don't transmit any messages at all (if you plug in RX but not TX).
        
### On a hosted system, executing an incorrect call to strlen (e.g. argument is an invalid address or unterminated string) can result in a runtime error (crash/halt). But when running bare metal on the Pi, every call to strlen (whether well-formed or not) will complete “successfully” and return a value. Explain the difference in behavior. What is the return value for an erroneous call?
 
Let's answer the second part first.
Recall that the implementation of `strlen` iterates through incrementing
memory addresses until we hit a `\0`.
Now if we don't hit a zero `strlen` will keep increasing and
the return value is undefined 
(it can be arbitarily high depending on the state of the Raspi).

Here's our best guess:
when we run it on a hosted system the stack size is limited by the OS
(see 
[this SO answer](https://stackoverflow.com/questions/2780100/is-there-any-limit-on-stack-memory))

> But programs compiled with for instance C or C++ allocate a fixed size stack at program startup. The size of the stack can usually be specified at compile time (on my particular compiler it default to 1 MB).

and we're guessing that once you try to read values outside of that stack
the OS will throw an error.
