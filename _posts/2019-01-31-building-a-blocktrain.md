---
layout: base
date: 2019-01-31
title: "Building an automated, blockchain-connected model train diorama"
tags:
  - programming
  - build
  - making
  - hardware
  - internship
  - imda
  - public
---

**WIP**

# Introduction
![](/img/blockchain_project/final_product.jpg)

Over the summer of 2018 (June-Aug 2018), I built an automated, blockchain-connected model train diorama and an accompanying visualisation. The diorama shows how changes in the locations of goods can be added in real-time to the blockchain, ensuring an immutable and unforgeable chain of provenance. This exhibit is also *interactive*: members of the public can scan QR codes pasted on several shipping containers, and they'll see that good's location and history on their phones update in real time.

# Why a blocktrain?

My boss was part of the group promoting industry adoption of blockchain. He wanted me to find some way to i) explain how the blockchain works, and ii) show how blockchain can be used in industry.

I chose to showcase the supply chain, because this application is already being promoted by [IBM](https://www.ibm.com/blockchain/industries/supply-chain) and it would have more relevance to the industry experts my boss talks to.

My boss was enamoured with the idea of a moving train, having seen a model train set at the Accenture HQ. So I had the task of finding out how to use a model train set to showcase the supply chain. After several iterations, I decided on the current diorama + blockchain visualisation.

# Architecture

![](/img/blockchain_project/blockchain_1.png)
![](/img/blockchain_project/blockchain_2.png)
![](/img/blockchain_project/blockchain_3.png)
![](/img/blockchain_project/final_product_annotated.jpg)

There are four main components of this diorama:

1. Hyperledger Blockchain and REST API (running on a DigitalOcean instance)
2. Train diorama (controlled by a Raspberry Pi)
3. Blockchain visualisation (running on the Raspberry Pi)
4. Asset tracker (served by a DigitalOcean instance)


<video width = "100%" controls>
<source src ="/img/blockchain_project/in_action.MOV">
</video>



# Blockchain on the cloud

I spun up a DigitalOcean instance to run the blockchain. 

Hyperledger Composer comes with its own REST API.

## Blockchain visualisation

The blockchain visualisation is written from scratch in HTML5 Canvas, and runs on the Raspberry Pi. It polls the Hyperledger REST API to check for updates.

I made a nice animation whereupon new blocks slide in, giving the diorama a sense of dynamism.

## Asset tracker

I wanted to make the diorama interactive so I created a 

People viewing the diorama can use their phones to scan the QR codes attached to several goods containers. 



# Building the diorama

## Ideation

I bought a $20 *Thomas the Train* model train set just to figure out how the diorama would work. You can see the video of it here:

<video width = "100%" controls>
<source src = "/img/blockchain_project/thomas_the_train.mp4">
</video>

## Starting and stopping the train


This was the hardest part of the project. 

I first tried to use a weird German device called an *Aufenthaltsschalter* to stop and start the train automatically. 

![](/img/blockchain_project/german_device.jpg)
The Aufenthaltsschalter*

![](/img/blockchain_project/jain_puzzled.jpg)
*Jain trying to figure out the device*

![](/img/blockchain_project/crazy_german_manual.jpg)
*Complicated schematic*

Finally, **Eureka moment**

The program running on the Raspberry Pi is very simple. It constantly listens for a voltage change on any of the reed switches, and if there is, it toggles the reed switch, which stops the train (to simulate goods unloading/loading).

It then makes a HTTP request to the Hyperledger blockchain REST API to update the locations of the goods on the train.

![Schematic of how the Raspberry Pi controls the train](/img/blockchain_project/how_it_works.png)

There were many possible approaches I considered: ultrasonic sensor, light sensor, etc

Here's a video of the train starting and stopping when toggling the reed switch. 

<video width = "100%" controls>
<source src = "/img/blockchain_project/reed_switch.mp4">
</video>

## Construction

I knew I wanted water in my diorama, as i) water looks very aesthetic, ii) I wanted to put a shipping container on the ship which people could scan, iii) Singapore is an island.

To get a nice water effect, I used this thing called "Realistic Water". We painted the styrofoam base a deep blue to get a "deep sea" effect, taped the sides to prevent water egress, then slowly poured the "Realistic Water" in, pressed in some rocks and finally left it to set overnight.

It worked quite well, I think: see for yourself.

![Closeup of realistic water, before ship was added](/img/blockchain_project/water_closeup.jpg)



# Glamour shots
![](/img/blockchain_project/final_product.jpg)
![](/img/blockchain_project/detail_2.jpg)
![](/img/blockchain_project/detail_3.jpg)
![](/img/blockchain_project/detail_6.jpg)

![](/img/blockchain_project/detail_4.jpg)
![](/img/blockchain_project/detail_5.jpg)


# Conclusion

I greatly enjoyed this project.

It was super fun to play with model trains and fix up the diorama.

Learned a lot of new things:

- Hyperledger
- Reed switch, relay switch
- 
