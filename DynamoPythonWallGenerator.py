#Description: Basic Wall Generator and placement in Revit though Dynamo Script
#Author: Steven Blevins from Danny Bently exaample https://www.youtube.com/watch?v=6YpEU91YYbM&list=PLlyMZ5IcKccjERFZwQgagGYFvitBKxVnu&index=2
#Date: 4-30-2020


import clr
clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import XYZ, Line, Wall

length = IN[0]
level = UnwrapElement(IN[1])

pt1 = XYZ(0,0,0)
pt2 = XYZ(length,0,0)


TransactionManager.Instance.EnsureInTransaction(doc)
line = Line.CreateBound(pt1, pt2)
wall = Wall.Create(doc, line, level.Id, False)
TransactionManager.Instance.TransactionTaskDone()


# Assign your output to the OUT variable.
OUT = wall