
class Challange():

    def __init__(self, name:str, tooltip:str):
        self.name:str = name
        self.tooltip: str = tooltip

    def give_tooltip(self):
        return self.tooltip

    def give_name(self):
        return  self.name


normal_challange = Challange('The Salty Scrub', 'No Spirit Ashes, NPC Summons, or Multiplayer/Cooperative Summons can ever be used')

general_challanges = [
    Challange('Lactose Intolerance', "You cannot use Rivers of Blood, Moonveil, Eleonora's Poleblade, Mohgwyn's Sacred Spear, Blasphemous Blade, Fingerprint Stone Shield, Seppuku, Flame of the Redmanes, Rock Sling, or Comet Azur"),
    Challange('The Lay of The Land', 'You cannot pick up/acquire any Map Fragments'),
    Challange('Great Rune Restriction', "You cannot activate, equip, or use any Great Runes (Rennala's Great Rune, as a passive, is allowed)"),
    Challange('Intrepid Infantry', "You cannot ever mount or ride Torrent in combat (you can still mount and ride him to traverse the overworld, explore, jump, etc., but you cannot use him in any fights)"),
    Challange('Daring Disrobement', 'You cannot wear/equip any type of armor'),
    Challange('Talisman Teetotaler', 'No Talismans can ever be equipped'),
    Challange('Off The Sauce', 'You cannot ever drink from/use the Flask of Wondrous Physick'),
]

String = """Pride of Legolas
You can only equip and deal damage with Light Bows, Bows, and Greatbows.
Dag Swag
You can only equip and deal damage with Daggers.
Indiana Jones
You can only equip and deal damage with Whips.
Strength Through Length
You can only equip and deal damage with Spears, Great Spears, and Halberds.
The Grim Gauntlet
You can only equip and deal damage with Reapers.
Wolverine
You can only equip and deal damage with Claws.
The Lumberjack
You can only equip and deal damage with Axes and Greataxes.
Better Call Maul
You can only equip and deal damage with Twinblades.
Peyronie Power
You can only equip and deal damage with Curved Swords and Curved Greatswords.
Witch-king of Angmar
You can only equip and deal damage with Flails.
The Otaku
You can only equip and deal damage with Katanas.
Inigo Montoya
You can only equip and deal damage with Thrusting Swords and Heavy Thrusting Swords.
Whac-A-Mole
You can only equip and deal damage with Hammers and Great Hammers.
King Arthur
You can only equip and deal damage with Straight Swords and Greatswords.
Big Boy Bonanza
You can only equip and deal damage with Colossal Weapons and Colossal Swords.
The Balboa
Fists only, you cannot equip or deal damage with anything else.
Flame Freak
Torches only, you cannot equip or deal damage with anything else.
The Wall
Shields only, you cannot equip or deal damage with anything else.
Spellin' Like a Felon
You can only equip Staffs or Seals and can only deal damage using Sorceries and Incantations.
Living Off The Land
The only damage-inflicting things you can use are craftable items (pots, perfumes, craftable arrows, darts, etc.) If it's not craftable/in a cookbook, it CANNOT be used to deal damage. Thus, Greases cannot be used, as any weapon they are applied to deals damage by itself.
Apeshit Assault
The only damage-inflicting things you can use are throwables: pots, throwing daggers, fan daggers, kukri, poisoned stones and stone clumps, explosive stones and stone clumps, gravity stone chunks and fans, and darts of all types.
"""


def conv(text:str):
    Return_list = []
    skip = False
    text = text.splitlines()
    for x in range(len(text)):
        if skip == False:
            Return_list.append(Challange(text[x], text[x+1]))
            skip = True
        else:
            skip = False
    return Return_list

basic_weapons = conv(String)

String = '''Master of Magic
You can only use weapons and Spells that deal Magic damage.
Lighting Lord
You can only use weapons and Spells that deal Lightning damage.
Habitué of Heat
You can only use weapons and Spells that deal Fire damage.
Sacred Soldier
You can only use weapons and Spells that deal Holy damage.
Madness Mukbang
You can only use weapons and Spells that inflict Madness.
Ashen Aggression
You can only deal damage by using Weapon Skills/Ashes of War.
Original Flavor
You cannot modify any weapon with Ashes of War or change any weapon's Affinity (any weapon's normal/base Weapon Skill can still be used)
Substance Over Style
No Weapon Skills/Ashes of War can ever be used
'''

adv_weapons = conv(String)

String = '''Mage of Convenience
The only spells you can cast are Glintstone Sorceries.
Black Arts of the Blade
The only spells you can cast are Carian Sorceries.
Crepuscular Casting
The only spells you can cast are Night Sorceries.
Fancy the Necromancy
The only spells you can cast are Death Sorceries.
Gravitation Invocation
The only spells you can cast are Gravity Sorceries.
Charms of the Cold Coven
The only spells you can cast are Snow Witch Sorceries and Full Moon Sorceries.
Spells of the Stonemen
The only spells you can cast are Claymen Sorceries and Crystalian Sorceries.
Conflagration Conjuring
The only spells you can cast are Magma Sorceries, Fire Monk Incantations, and Fire Giant Incantations.
Hemo-Hocus-Pocus
The only spells you can cast are Aberrant Sorceries and Blood Incantations.
Draconic Domination
The only spells you can cast are Dragon Communion Incantations.
Thaumaturge of Thunder
The only spells you can cast are Dragon Cult Incantations.
Wild Wizardry
The only spells you can cast are Bestial Incantations.
Teachings of the Tree
The only spells you can cast are Erdtree Incantations.
Follower of the Fingers
The only spells you can cast are Two Fingers Incantations.
Golden Boy
The only spells you can cast are Golden Order Incantations.
Incantations of Insanity
The only spells you can cast are Frenzied Flame Incantations.
By the Skin of the Gods
The only spells you can cast are Godskin Apostle Incantations.'''

adv_spells = conv(String)

String = """Arsenal Aesthete
Each time you acquire a new weapon, you must immediately equip it and only use that weapon (until you find/acquire another new weapon, and so on). You cannot use any of the weapons you previously used again; once it is replaced by a new weapon, it is gone.
Magic Maven
Each time you acquire a new Sorcery or Incantation, you must permanently retire 1 Sorcery or Incantation that is already in your inventory (it can never be used again in that playthrough). This challenge begins once you have 3 Spells/Incantations in your inventory.
Night Gaol Spelunking
Each and every time you defeat a Legend or Shardbearer, before proceeding to the next Legend or Shardbearer, you must first defeat 2 of the following 3 (your choice each time):A Night Boss, An Evergaol Boss, A Cave, Catacombs, or Hero's Grave Boss.
The Wheel
If you die three times in a row while using the same weapon, you must immediately Discard that weapon, thereby losing it forever. (Thus, either change up your weapons consistently, or risk losing them)
The Magic Wheel
If you die three times in a row while using the same Sorceries/Incantations, you must immediately Discard the Sorcery or Incantation that you last used, thereby losing it forever. (Thus, either change up your magic consistently, or risk losing your go-to, favorite spells)
Boss and Toss
Each and every time you defeat a Great Enemy, Legend, or Shardbearer, you must Discard ALL of the weapons/shields you used to beat them. If you used magic, you must also Discard ALL of the Sorceries/Incantations you used to beat them (you can keep all Staffs/Seals)."""

ex_challange = conv(String)

String = '''QuikClot
You cannot inflict Hemorrhage/Blood Loss on any enemy
Warm Heart
You cannot inflict Frostbite on any enemy
Antidote Inherent
You cannot inflict Poison on any enemy
Putrefaction Preventative
You cannot inflict Scarlet Rot on any enemy
Emissary of Insomnia
You cannot inflict Sleep on any enemy
Panacea Playthrough
No status effects of any kind can be inflicted on any enemy
100% Organic
No Spells or Incantations can be used to remove/cure status ailments (consumables only!)
Bugchaser
You cannot ever remove/cure any status ailment (You must heal through it and let it run out!)'''

status = conv(String)

String = '''Scavenger
You cannot buy anything from anyone (or trade a Remembrance for anything)
Rune Ruin
You cannot gain Runes by using any consumable Runes (this includes Remembrances)
Fastest Draw in The Lands Between
You can only use a Grease if it's a Drawstring Grease (list of Consumables, scroll to Greases)
Hygienic Hero
You cannot use any Greases of any type'''

crafting = conv(String)

String = '''Magic Mending
You can only heal using Incantations
Rejuvenating Rocks
You can only heal using Warming Stones and/or Frenzyflame Stones
Raw Remedy
You can only heal using Raw Meat Dumplings
Physick Fixer-Upper
You can only heal using the Flask of Wondrous Physick
Critical Convalescence
You can only heal through Critical Hits (with Assassin's Crimson Dagger equipped)
The Isai
You cannot ever heal in any way (except as noted below)
No Need for Golden Seed
You cannot ever upgrade your Crimson and Cerulean Flasks using Golden Seeds
No Tears, No Fears
You cannot ever upgrade your Crimson and Cerulean Flasks using Sacred Tears
Mana From The Heavens
You can only recover FP by using Starlight Shards
Focus Fighter
You can only recover FP by using the Assassin's Cerulean Dagger, the Ancestral Spirit's Horn, the Sacrificial Axe, and the Sword of Milos'''

healing = conv(String)

String = '''Vigor Vexation
You cannot increase your Vigor level higher than 30
Fettered Focus
You cannot increase your Mind higher than 25
Stymied Stamina
You cannot increase your Endurance higher than 20
The Hellish Hundred
You cannot increase your total level above 99 (you cannot get to level 100)
Thin Crust
You must always maintain a Light Equip Load
Deep Dish
As soon as possible, you must achieve and always maintain a Heavy Equip Load
'''

stats = conv(String)

String = '''Soul Simplicity
You cannot increase your stats/level, ever.
Tactical Trek
You cannot ever mount or ride Torrent.
Blunt Instrument
You cannot ever upgrade any weapons/shields using Smithing Stones/Somber Smithing Stones.
The Waver
You can only ever have 1 hand equipped with/holding a weapon/shield/etc. (One hand must ALWAYS be empty, free to "wave" at enemies. You cannot two-hand a weapon, either!)
How Can She Slap?
You cannot deal damage with anything other than your empty hands: no weapons, spells, throwables, or anything other than empty hands can be used to deal damage
Globetrotter
You cannot ever warp using Sites of Grace (unless absolutely necessary, i.e. to get to Farum Azula or the Roundtable Hold and back)
Amnesiac
You cannot acquire any Memory Stones or equip the Moon of Nokstella
Three Strikes
If you die 3 times to the same Boss, regardless of its status/class, it's game over. You must delete that character and restart the challenge. (3 lives/attempts per Boss. Thus, dying twice to an optional boss is acceptable, but you might want to walk away or consider if the reward is worth it to risk a third, run-ending death!)
1UP
You start with 1 Extra Life, and each time you defeat a Great Enemy, Legend, or Shardbearer you get another Extra Life. Each time you die, you lose a life. If you run out of lives, it's game over. You must delete that character and restart the challenge. (Thus, if you die twice before ever defeating a Great Enemy, Legend, or Shardbearer, you ran out of lives, and it's GG. You do NOT get an Extra Life for defeating an Enemy class boss. The mandatory death that occurs at the very beginning of the game against/after the Grafted Scion does not count as a death)
Git Gud
If you die even once, you're done. You must delete that character and start over. (The mandatory death that occurs at the very beginning of the game against/after the Grafted Scion does not count)'''

EX_EX_EX = conv(String)

print(EX_EX_EX)