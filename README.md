# My First Poker Game v1.0
<h3> Author: Pablo Loren-Aguilar </h3>
<h3> Email: p.loren-aguilar@outlook.com </h3>

My kids asked me to download a poker game for their phones, but I didn't like the idea of exposing them to online gambling yet, so I decided to create my own one. The game uses the open source treys poker library (https://github.com/ihendley/treys) in order to calculate all the poker maths associated with the game, and uses the cards and chips images found in the open source blackjack game by Torbjörn Hedqvist (https://github.com/torbjornhedqvist/blackjack)

The game plays poker using a simple "positive expected value" approach. The game calculates the probabilities of obtaining long term benefits when playing a specific hand. If the value is positive, the hand will be played, otherwise it will not. To make it more human, a random variable is added to the calculation in order to make the game play weak hands or to emulate bluffs.

Happy to receive any criticism and suggestions so the program can be improved. Please note that this software is free and comes without any guarantee. SEE LICENSE FOR DETAILS.
