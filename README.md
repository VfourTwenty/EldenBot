GAME COMPLETION, WEAPONS OR OTHER ITEMS ARE NOT REQUIRED (ONLY HAVING OPENED ACCESS TO THE DLC)

Bot demo:

https://github.com/Vfor20/EldenBot/assets/132915930/31fce448-e4b3-4aae-9223-36b2c930b819


If you've already played the Elden Ring DLC you should know about the "Rauh Ancient Ruins, East" lost grace spot, where you can gain endless runes with no combat.
This is truly an amazing place for the late game and even more so for the beginning. If you are just starting the game, all you need is to defeat Radan and Mog at the Mogwin palace 
to open access to the DLC, and then watch a guide on youtube on how to get to this grace, which will really be a fun journey :) 

in order for the bot to work, you'll need to have downloaded the main.py at least, and the win32_helpers.py located in the helpers folder. all other dependencies can be seen 
at the very top of the main file

![Снимок экрана 2024-07-08 193617](https://github.com/Vfor20/EldenBot/assets/132915930/25c70ec2-643e-4f45-98ae-8a7df48b91fc)
they all can be pip3 installed

![Снимок экрана 2024-07-08 201454](https://github.com/Vfor20/EldenBot/assets/132915930/fb808a11-55ab-40d1-94a6-f870e2f1723a)
the proper way to place the helpers file



one more thing you'll need is to have Tesseract installed on you computer (you can look it up, it's pretty easy), by default it should install on your C drive, but if you choose another
location for it, you'll have to change the executable path here in main:
![Снимок экрана 2024-07-08 194033](https://github.com/Vfor20/EldenBot/assets/132915930/e2414804-74f9-417f-be14-ebc5d62970d0)

it is needed for keeping track of the amount of runes you've farmed is case your computer freezes and the bot falls out of its routine. if that happens, the bot will be stopped so 
you can safely pick up all the runes.

It's STRONGLY RECOMMENDED to use the Golden Scarab talisman at least to increace the amouns of the runes gained. also, you can use Gold-pickled Fowl Feet and Golden Horn (?) which looks 
like this:

![photo_2024-07-08_19-51-05](https://github.com/Vfor20/EldenBot/assets/132915930/456ddffb-7411-40f8-b1fd-f6dc61d3dbbe)
these will greatly boost your rune income!

Once you've set up the bot, installed all the packeges and got to the grace spot, put the game into windowed mode and place it into the top left corner of you screen, that's
needed so the mouse clicks the proper things. Then, launch the main script, the bot will start after 5 seconds once you've dome that so you have time to open the game. Enjoy! ;)
stop the script manually with ctrl+c

--------------------------------------------
! IMPORTANT NOTES IF THE BOT ISN'T WORKING !
--------------------------------------------
It may be due to the speed of your machine, and the timings of the bot might need to be twicked slightly. 
Here are the key moments where the performance may be influencing the timings:
1)![Снимок экрана 2024-07-08 200208](https://github.com/Vfor20/EldenBot/assets/132915930/da6051b4-8699-46c0-ba3b-862db4601514)
2)![Снимок экрана 2024-07-08 200248](https://github.com/Vfor20/EldenBot/assets/132915930/ebb6dd3f-a467-4cab-abed-0f1c82b438eb)
3)![Снимок экрана 2024-07-08 200131](https://github.com/Vfor20/EldenBot/assets/132915930/9398e438-28df-43f4-b63c-8b9ca4c796d6)
so feel free to add or take away a few miliseconds there

this project was inspired by
https://github.com/AdamBissonnette/elden-ring-bot
and 
https://www.youtube.com/watch?v=ViFgSxzHhRU&list=PL91jA61XuCIC3JH0ey5cnCxpQ46IuvzwE&ab_channel=OwenLockwood
the informationn these people have gathered was very useful! :)



