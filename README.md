# AVHackbrightProject
<h1> Bit-z-Bots </h1><h4> customizable robot figurines </h4>

<h5>Bit-z-Bots, a web application for girls to customize and create their own miniature 3D-printed robot figurine, 
is a tribute to the developer's childhood spent borrowing her brother’s Legos and science kits. Cute and unassuming, a 
Bit-z-Bot’s noble purpose in its 3D-fabricated life is to foster interest in science and technology while combating 
the lack of creative, intelligent, tech-related toys available for girls. 

Why give a girl a doll if she can make her own?</h5>

<h2>Technology Stack</h2>

Written primarily in Python and Javascript, Bit-z-Bots utilizes a Flask framework and its gallery uses a 
SQLite3 database engine. 

All 3D models were hardcoded using OpenSCAD 3D-modeling software (exported as .stl).

The ability to change a Bit-z-Bot's color and size, and to purchase it for 3D fabrication is made feasible via
the i.materialise 3D Print Lab Connection API (specifically, a POST request using the appropriate .stl file and 
redirection of the user to the i.materialise site).

Frontend tech stack also includes use of HTML5, Jinja, CSS3, and JQuery.

<h2>Basic Principles</h2>

Customization: Enter the makestation and select components from three choices each for face, body and legs of your Bit-z-Bot. In the background,
each component is tethered to a variable that, when stitched together with others, forms the appropriate, corresponding 3D-model file.
There are currently 27 unique Bit-z-Bots that can be generated.

Creation: Name your Bit-z-Bot, enter your information, and upload it to the Gallery so everyone can see (and 3D print!) your design.
3D print your design via the i.materialise 3D Print Lab. 


<h2>Troubleshooting</h2>

With only 4 weeks to complete the project, time was scarce and optimizing the time for a Bit-z-Bot to be generated
was a feat. After making 3-minute-long API calls and enduring the inner firey circles of OAuth with other less 
dev-friendly 3D printing APIs, the developer discovered i.materialise, whose simple, straightfoward 3D Print Lab
Connection API made the 3D fabrication aspect of the project feasible. 

Stitching together the components to make a unique .stl file for each Bit-z-Bot was difficult, but to optimize 
loading time of the app during creation of the figurine, the app was simplified to include three choices for each
component, and the .stl files were quickly hardcoded (i.e. with the "face" component positioned at fixed positive y-axis, 
"body" centered at origin, and "legs" at fixed negative y-axis).

Bit-z-Bots is considered a WIP as the developer's first independent programming project, and more features will be
implemented in the near future (e.g. social aspect to the gallery for sharing and trading designs, more customization,
seamless .stl stitching without hardcoding, and ability to download the .stl file directly for local 3D fabrication).


<h3>Origin and Evolution of the Bit-z-Bot</h3>

Originally named BotGals (Gal meaning "gal" and a pedantic nod at Galatea, Pygmalion's statue), Bit-z-Bots was the
final form of an amateur developer's attempt at battling the gender normative toy aisles. She realized she had independently
reached the conclusion many other larger companies already had addressed-- that children are impressionable and
that playing with toys, an activity they spend much of their time doing, is influential in the 
career that they ultimately pursue as adults. Toys marketed toward boys often involve spatial reasoning and problem-solving; 
toys marketed toward girls often have a more superficial aspect. When boys are given building blocks and girls are
given dolls, the trend of a minority of female engineers becomes partly elucidated.

To allow a girl the creative agency to create her own figurine-- make her own role model, rather than be given
a superficial, vapid one-- seemed a powerful and important endeavor. An important point of Bit-z-Bots was to not 
enforce the idea that femininity and power or intelligence are mutually exclusive. Born during Hackbright Academy's
Software Engineering Fellowship, Bit-z-Bots had to be a unique, compelling project, but also fit in the constraints 
of a 4-week project deadline, and be feasible with the skillset the developer had garnered after only five weeks of 
intensive programming.

The solution to making Bit-z-Bots unique, science- and tech-oriented, and feasible for an amateur developer was to make
the 3D model design as simple as possible-- using basic shapes like rectangles, spheres and cylinders in OpenSCAD
3D-modeling software. The result: adorable miniature robot figurines that were customizable based on which components
were chosen (originally from three different choices for face, body and legs). Bit by bit, a bot could be made on a 
computer screen, and their tiny stature afforded them their name "Bitsy" Bots. 

Though the initial problem space Bit-z-Bots entered was focused on fostering girls' interest in science and tech (thus
the app catered toward girls' general preferences), the creator quickly realized that everyone wanted their own Bit-z-Bot.
Bit-z-Bots is of course open to creation by all genders and ages, with an emphasis on tech being inclusive to young girls.
