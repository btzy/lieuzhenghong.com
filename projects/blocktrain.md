---
title: Blocktrain
date: 2018-08-01
tags: project
layout: base
img: "/img/blockchain_project/final_product.jpg"
blurb: "A blockchain-connected train diorama"
---

## Blockchain train diorama (Blocktrain)

June 2018 -- Aug 2018

Tech stack: Hyperledger Fabric/Composer, Node.js, JavaScript

After obtaining buy-in from senior management,
I conceptualised and led a project that persuades industry leaders
to adopt blockchain in their companies.

The project is a fully-automated blockchain demonstrator for supply chain management.
It showcases how blockchain technology can be adopted in the supply chain.

![](/img/blockchain_project/final_product.jpg)
![](/img/blockchain_project/detail_2.jpg)
![](/img/blockchain_project/detail_3.jpg)
![](/img/blockchain_project/detail_4.jpg)
![](/img/blockchain_project/detail_5.jpg)

To this end, I've built an automated train diorama, and three other components:

1. Model train diorama with IoT sensors (to showcase the system in action)
2. Blockchain (powered by Hyperledger)
3. Real-time blockchain visualisation
4. Asset tracker (good viewer) that works on any mobile device

Here's how it works. On the train are shipping containers with QR codes pasted
on them. Scanning each QR code will pull up the asset tracker, a webpage that
gives the real-time location and previous provenance of the good --- all stored
immutably on the blockchain. As the train pulls up to a station, the goods are
unloaded and sent to a different location (absent a robotic arm, I'm afraid one
has to use his imagination for this).

When this happens, each shipping container will update its location automatically.
This is stored on the blockchain. I also built a blockchain visualisation
so we can see new blocks being added in real-time.

![screenshot of blockchain slides](/img/blockchain_project/blockchain_3.png)
![screenshot of blockchain slides](/img/blockchain_project/blockchain_1.png)
![screenshot of blockchain slides](/img/blockchain_project/blockchain_2.png)

I've written a more extensive writeup about the project
[here](../2019/01/31/building-a-blocktrain.html),
where I go into further detail.

Built with Hyperledger, Node.js, and HTML Canvas.
