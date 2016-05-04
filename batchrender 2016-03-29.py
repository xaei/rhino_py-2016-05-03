import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino

"""from discourse
def Render_iso():
    vports = rs.ViewNames(True, 0)
    cv = rs.CurrentView()
    ortho = ["Top","Bottom","Front","Back","Right","Left",]
    if cv not in ortho: rs.Command("!_Render", echo=True)
    else:
        rend = rs.GetString (message="View is orthogonal, render? Y/N", defaultString="N", strings=["Y", "N"])
        if (rend == "Y"): rs.Command("!_Render", echo=True)

#Render_iso()
"""


def renderEachView():
    #print rs.ViewNames() #all viewports
    for a in rs.NamedViews():
        if a.startswith("0"):
        #if a[:2] in ["20","21","22"]:
            #print "rendering: " + a
            rs.RestoreNamedView(a)
            print "rendering: " + rs.CurrentView()
            rs.Command("!_Render", echo=True)#render each named view
            print "completed" + a
        #rs.RestoreNamedView("03 entrance interior view")
        #rs.Command("!_Render", echo=True)
        #rs.RestoreNamedView("04 interior view from service wall 1")
        #rs.Command("!_Render", echo=True)

renderEachView()
