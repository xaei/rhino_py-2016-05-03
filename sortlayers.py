import rhinoscriptsyntax as rs
from scriptcontext import doc
from System import Guid

sorted_layer_names = sorted([layer.FullPath for layer in doc.Layers
if layer.ParentLayerId == Guid.Empty],
key=lambda s: s.lower(), reverse=True)

tmp_layer_name = rs.AddLayer(Guid.NewGuid().ToString())
tmp = doc.Layers[doc.Layers.FindByFullPath(tmp_layer_name, False)]

for fp in sorted_layer_names:
    l = doc.Layers[doc.Layers.FindByFullPath(fp, False)]
    l.ParentLayerId = tmp.Id
    l.CommitChanges()
    l.ParentLayerId = Guid.Empty
    l.CommitChanges()

doc.Layers.Delete(tmp.LayerIndex, True)
