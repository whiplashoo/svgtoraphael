# svgtoraphael
Parses an XML file, originated from SVG, and outputs a Raphael object. Used for creating the maps on http://mapchart.net .

## Example
Open world.html file in a browser. You can see that it contains a SVG world map. 

## Usage

If you want to **convert a large SVG file to a Raphael object**, follow these steps:

1. First, **edit the SVG file until it has the following structure**:
	```
	<xml ...>
   	<svg>
   	<defs .../>
   	<sodipodi:nameview .../>
   	<metadata>
   	...
   	</metadata>
   	<g>
       <path .../>
       <path .../>
       <path .../>
       ...
    </g>
    </svg>
    ```
	You can make use of Inkscape edit features. You need to remove all groups from the SVG image, except for the general group containing all the paths, and convert the previously grouped paths to one path. You can do this by selecting a path group, Object--> Ungroup, and then merge the selected paths by selecting Path--> Union. You can check the structure of the SVG in Inkscape's XML Editor (Ctrl-X).

2. Once your SVG is ready, open it in a text editor and **save it as XML file (.xml)**.

3. In the SVGtoRaphael.py script, **change the argument to tree = ET.parse()** to whichever file you want to convert. By default, it is 'world.xml', which is uploaded here for example purposes. 

4. After running the script, a text file 'final.txt' is created. You can paste its content between this snippet in a .js file:

	$( document ).ready(function() {
		var rsr = Raphael('rsr', '2600', '1300'); var layer1 = rsr.set();
		// 'final'.txt output goes here
	});

	All this snippet does is load all the paths that consist the SVG to the <div id="rsr"> that exists in the HTML page, and create a Raphael object out of it, enabling you to use all of Raphael.js functions and features.

