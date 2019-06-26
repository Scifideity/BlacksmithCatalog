from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, CategoryItem, User

engine = create_engine('sqlite:///blacksmithcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


# Create Dummy User
User1 = User(name="Robo Barista", email="tinnyTim@abc.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Category1 Hammers
category1 = Category(user_id=1, name="Hammers")

session.add(category1)
session.commit()

Item3 = CategoryItem(user_id=1, title="Cross-pein", description="Standard blacksmithing hammer slightly rounded on one face with rounded wedge on the other (wedge is perpendicular to the handle)",
                     category=category1)

session.add(Item3)
session.commit()

Item2 = CategoryItem(user_id=1, title="Rounding", description="Standard blacksmithing hammer slightly rounded on one face and flat on the other",
                     category=category1)

session.add(Item2)
session.commit()


Item1 = CategoryItem(user_id=1, title="Fullering", description="Rounded wedge on one side (wedge is parallel to the handle), flat striking point on the other for adding fullers to blades",
                     category=category1)

session.add(Item1)
session.commit()

print ('Hammers added')

# Category2 Anvils
category2 = Category(user_id=1, name="Anvils")

session.add(category2)
session.commit()

Item3 = CategoryItem(user_id=1, title="Type A1", description="Standard weights are (kg): 32, 41, 52, 91, 129, 161, and 305.  Thin tapered square and upward pointing horn with one hardy hole for tools.",
                     category=category2)

session.add(Item3)
session.commit()

Item2 = CategoryItem(user_id=1, title="Type A4", description="Standard weights are (kg): 32, 41, 56, 92, 126, and 159.  Thick tapered square and rounder upward pointing horn with one hardy hole for tools.",
                     category=category2)

session.add(Item2)
session.commit()


Item1 = CategoryItem(user_id=1, title="Type B25", description="Standard weights are (kg): 38, 48, 69, 102, and 159.  Double horned. One round tapered straight out and the other tapered flat in line with surface",
                     category=category2)

session.add(Item1)
session.commit()

print ('Anvils added')

# Category3 Chisels
category3 = Category(user_id=1, name="Chisels")

session.add(category3)
session.commit()


Item3 = CategoryItem(user_id=1, title="Flat", description="Sharpened Squared tip designed for cutting or marking",
                     category=category3)

session.add(Item3)
session.commit()

Item2 = CategoryItem(user_id=1, title="Chasing", description="Sharpened tip in an arc (fishtail) designed for making longer marks along a pattern or curve",
                     category=category3)

session.add(Item2)
session.commit()


Item1 = CategoryItem(user_id=1, title="Rounded", description="Squared tip but rounded for making decorative marks or light fullering",
                     category=category3)

session.add(Item1)
session.commit()
print ('Chisels added')

# Category4 Punches
category4 = Category(user_id=1, name="Punches")

session.add(category4)
session.commit()

Item3 = CategoryItem(user_id=1, title="Center(Round)", description="Round Sharpened tip designed for putting round point marks",
                     category=category4)

session.add(Item3)
session.commit()

Item2 = CategoryItem(user_id=1, title="Center(Square)", description="Round tip but sharpened in square fashion to allow center marks to be more of a X pattern for better visibility",
                     category=category4)

session.add(Item2)
session.commit()


Item1 = CategoryItem(user_id=1, title="Rounded", description="Round tip rounded to make half sphere indentions for decoration",
                     category=category4)

session.add(Item1)
session.commit()
print ('Punches added')

# Category5 Marking
category5 = Category(user_id=1, name="Marking")

session.add(category5)
session.commit()

Item3 = CategoryItem(user_id=1, title="Awl", description="Any large 'needle' like object for etching a mark or line into steel",
                     category=category5)

session.add(Item3)
session.commit()

Item2 = CategoryItem(user_id=1, title="Silver Pencil", description="Gravity fed mechanical pencil with replaceable 'silver' lead for marking on steel. Often used on top of awl scratch marks to highlight them for better visibility",
                     category=category5)

session.add(Item2)
session.commit()


Item1 = CategoryItem(user_id=1, title="High Temp Marker", description="Liquid filled pens with wick tip that allow for marking on steel in various temperature tolerant pigments.  Very useful when needing to know a specific temperature range of the steel.  The Paints are rated temperature and stick around until that temperature is surpassed",
                     category=category5)

session.add(Item1)
session.commit()
print ('Marking added')


# Category6 Tongs
category6 = Category(user_id=1, name="Tongs")

session.add(category6)
session.commit()

Item5 = CategoryItem(user_id=1, title="Knife/Blade Tongs", description="Tongs with jaws offset from the handles to allow for griping of bars and blades that would extend past the hinge point of the tongs. ",
                     category=category6)

session.add(Item5)
session.commit()

Item4 = CategoryItem(user_id=1, title="RRS Tongs", description="'Rail Road Spike' Tongs.  Tongs specifically designed to grasp and hold the head of a Rail Road Spike while forging the shaft.",
                     category=category6)

session.add(Item4)
session.commit()

Item3 = CategoryItem(user_id=1, title="Open-Mouthed Tongs", description="Used for holding medium-sized pieces of round or square iron.  Sometimes called Flat Bills",
                     category=category6)

session.add(Item3)
session.commit()

Item2 = CategoryItem(user_id=1, title="Bolt Tongs", description="For holding bolts or similar work.  The hollow a the back jaws allow the head to clear the tongs.  Also used for holding flat iron to bend it edgewise",
                     category=category6)

session.add(Item2)
session.commit()


Item1 = CategoryItem(user_id=1, title="Bent-Bit Tongs", description="For holding iron parallel to tongs.  Sometimes called side tongs. ",
                     category=category6)

session.add(Item1)
session.commit()
print ('Tongs Added')

# Category7 Forges
category7 = Category(user_id=1, name="Forges")

session.add(category7)
session.commit()


Item3 = CategoryItem(user_id=1, title="Induction Forge", description="An induction heater operates by surrounding the object to be heated with a coil carrying high frequency AC current. Basically, the entire setup acts like a huge transformer with a shorted secondary. At 30 kVA, an induction forge heater gets hot enough to melt and forge steel, iron, and aluminum. Instructables user 'bwang' published his build at https://www.instructables.com/id/30-kVA-Induction-Heater/ if you'd like to tackle building one. WARNING!! HIGH VOLTAGE!! WITHOUT PROPER TRAINING OR SKILLS THIS PROJECT CAN KILL YOU!!!!",
                     category=category7)

session.add(Item3)
session.commit()

Item2 = CategoryItem(user_id=1, title="Propane Forge", description="Typical Propane Forges are metal containers lined with Fire Brick and Ceramic Refactory Blankey liner to retain as much heat as possible. This helps conserver fuel as you don't need to run the forge as hot all the time.  Propane Forges can have 1-5 burners depending on the size of the forge.  Interrior cubic inch space is important.  Typical ratio is one well tuned 3/4in burner per 300-350 cu/in.",
                     category=category7)

session.add(Item2)
session.commit()


Item1 = CategoryItem(user_id=1, title="Coal Forge", description="Every Blacksmith's Starter Forge.  It's any type of forge that uses coal as fuel. Works best with a forced air flow up from the bottom center of the forge to control temperature.  Can be made from a simple stack of Fire Brick on any fire retardant surface or any metal container with access points that will retain heat. Coal can be Hardwood Lump Coal from a local store but Bituminous Coal is the coal-of-choice for the blacksmith. It is a soft, mid-grade, black coal. Mined from deeper mines than other coals. It burns much more cleanly. Your neighbors will thank you for using it over the heavy smoking stuff",
                     category=category7)

session.add(Item1)
session.commit()
print ('Forges added')

# Category Template - Replace 'TEMPLATE with Category Name'
# Category TEMPLATE
# category# = Category(user_id=1, name="TEMPLATE")

# session.add(category#)
# session.commit()

# Item Template - Replace # with appropriate Item and Category #
# Item# = CategoryItem(user_id=1, title="PUT-ITEM-NAME-HERE", description="PUT-ITEM-DESCRIPTION-HERE",
#                     category=category#)

# session.add(Item#)
# session.commit()
# print ('TEMPLATE added')

print ('Starter Database populated...')
