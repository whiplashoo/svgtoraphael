import xml.etree.ElementTree as ET
tree = ET.parse('world.xml')
root = tree.getroot()
g = root[3]
######################
# XML example tree for this to work:
#   <xml ...>
#   <svg>
#   <defs>
#   <sodipodi:nameview>
#   <metadata>
#   <g>
#       <path/>
#       <path/>
#       <path/>
#       ...
#   </g>
#   </svg>
#
######################
with open("final.txt","w") as f:
    for path in g:
        f.write('var '+ path.attrib['id'].replace(".","").replace("-","").replace("+","").replace(" ","_") + '=rsr.path("'+ path.attrib['d'] + '").attr({id:"'+path.attrib['id'] + '",parent: "layer1",fill:"#d1dbdd","fill-opacity": "1",stroke:"#000000","stroke-width":"1","stroke-miterlimit":"4","stroke-opacity":"1","stroke-dasharray":"none"}).data("id","'+path.attrib['id']+'");')


