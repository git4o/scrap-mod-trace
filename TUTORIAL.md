# **This tutorial is how to delete broken shape ids, but you can use it to find the name of the missing mod, so you can install it**

**I have no idea what the linux equivalent of the paths are, but google is your friend**

**I backed it up, because I find that Reddit posts sometimes disappear, but here is [the original post by u/Tomas0514_cz](https://www.reddit.com/r/ScrapMechanic/comments/1epfyls/comment/lhlp0ud/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) all credit goes to them, I just turned his tutorial into a tool that just detects mods**

Find your blueprint in the file explorer.

Usualy in `C:\Users\<user>\AppData\Roaming\Axolot Games\Scrap Mechanic\User\User_<your player id>\Blueprints`.

And in there you need to find your blueprint. You have open each blueprint and check the description for the name of the blueprint. I don't know a easier way, sorry.

2. Copy the blueprint folder and paste is somewhere else for safety.

3. Go to the original folder and openblueprint.json, you'll find the the code is in a single line. So i would recommend to format the code with this or some other website. And you will replace the code with the formatted one. Be carefull to replace it and not just paste it in.

4. Scroll all the way down and find "dependencies": and find the name of the mod you don't want (or the name of the mod you want to install). Next to that you'll find "shapeIds":. Select the first one and copy it.

My test blueprint:

(Your dependencies will look differently, you'll probably have more mods and shape ids)

The mod I don't want is "The Modpack Continuation". So I'll copy the first shape id. (eg. d8296109-2ffb-4efb-819a-54bd8cadf549)
`
"dependencies": [
    {
      "contentId": "b7443f95-67b7-4f1e-82f4-9bef0c62c4b3",
      "name": "The Modpack Continuation",
      "shapeIds": [
        "d8296109-2ffb-4efb-819a-54bd8cadf549"
      ],
      "steamFileId": 2448492759
    }
  ]`
  **You can install the mod using its name or continue below to delete the broken shape**
5. Press Ctrl+f and paste the shape id in to the search bar to search the file for the shape id. Go to the first match and you should see something similar.
`
,
{
  "color": "DF7F00",
  "controller": {
    "containers": null,
     "controllers": null,
     "data": "0ExVQQAAAAEEAAAAATA",
     "id": 41133,
     "joints": null
   },
   "pos": {
     "x": 11,
     "y": -2,
     "z": 3
  },
  "shapeId": "d8296109-2ffb-4efb-819a-54bd8cadf549",
   "xaxis": 1,
   "zaxis": -2
}`
6. And delete ALL of this, the comma on top, the bracket on the bottom and everything in between.

Then go to the next match of the shape id (still the same as before) and repeat this. And repeat it until the only match of the shape id is under the dependencies.

Then go back to the dependencies and move onto the next shape id in the "shapeIds":, if there is another one and REPEAT - again search for the new shape id, delete...

You'll repeat that until you went thru all the shape ids. If you have multiple mods you don't want you'll have go thru all of those ids as well.
7. And we are technically done, the blueprint should be spawnable, but you shoud also remove the mod from the dependecies.

So delete this (you'll have it diffirent):
`
,
{
      "contentId": "b7443f95-67b7-4f1e-82f4-9bef0c62c4b3",
      "name": "The Modpack Continuation",
      "shapeIds": [
        "d8296109-2ffb-4efb-819a-54bd8cadf549"
      ],
      "steamFileId": 2448492759
    }`
Be aware the comma on top might not be there if the mod the first one in the dependencies.

And we are DONE.
