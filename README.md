# mi-osiris.github.io
This is the source for our website at http://www.osris.org

The website is based on Jekyll templates.  
Commits to this repository master branch will automatically be compiled into the website.

For more information on Jekyll templates: https://help.github.com/articles/about-github-pages-and-jekyll/

## Quick tutorial 

Clone this repository locally.  Start a new branch - only designated people can push directly to master.

To make a new news post create a new file in _posts.  You can also create a post in _drafts and it will only show up if a 
flag is passed to jekyll (more later).  The posts already there should provide good examples.

To make a new static page (such as the About, Publications, etc) begin a new document in the root of the repo or create 
a subdirectory.  If you create a subdirectory with several pages create a sidebar menu in _includes and reference it in the 
'sidebar' tag at the top of the page.  Examples of this are in the 'performance' or 'components' directories.  If you want your page
to be in the menu at the top of the page include 'group: navigation' and 'order: xxxx' in the top material.  You'll see that
existing pages have a certain order already so be sure to renumber their order tags appropriately.  

New pages can be created as .md (markdown) or .html. I recommend doing .md since you can mix html freely in those and still 
use markdown. 

If you prefer to use markdown here are the formatting and syntax rules:  https://help.github.com/articles/basic-writing-and-formatting-syntax

For many things, regular html will be easier and more logical to write - for example hrefs around images and inline css or using a css class. 
You can find many examples throughout this code.    

Images are in assets/images.  Refer to them with the ASSET_PATH template var:  {{IMAGE_PATH}}/sc16/total-showfloor-Thursday.jpg

Specify a percentage width with all images so they resize as the site scales.  Prefer to use a larger image and scale down so it works well even on
high-dpi displays.  Link all your images to the image file so users can click/tap on them to get the full-size view.  In certain 
cases this may not be logical, such as for company logos or images that you need to link elsewhere.  

CSS is in assets/css/style.css.  You shouldn't generally need to modify it but it may be useful to know certain pre-existing classes.

 - 'lf' and 'rf' to float left and right
 - 'imgwrap' is useful to wrap a div around an image that will format any text as a caption
 
 ```
 <div class="imgwrap">
<a href="{{IMAGE_PATH}}/ATLAS-Object-Gateway.png">
	<img src="{{IMAGE_PATH}}/ATLAS-Object-Gateway.png" style="width: 100%">
</a>
	ATLAS and OSiRIS S3 Gateways
</div>
```

## Preview your work

You will need to install the Jekyll bundle to preview your work.  

```
gem install jekyll bundler
```

To preview your work on http://localhost:4000 run: 
```
bundle exec jekyll serve
```

To view draft posts add '--drafts' to the above command line.

## Configuration

Certain configuration options are set in _config.yml: 
 - google analytics ID 
 - site title
 - tag used to denote where front-page news posts should break (&lt;!--excerpt--&gt;)

The basic layout used for every page is in _layouts/default.html.  The content you put into .md files is inserted into this 
layout at the {{ content }} template variable.  Tags in the top material of the page effect navigation, title, etc.  

Bootstrap and jQuery libraries are in assets/resources.  In theory it would be possible to put updated versions of these resources if 
so inclined.  

This code started out as the Jekyll-Bootstrap-3 theme though it is now heavily modified.
http://jekyll-bootstrap-3.github.io/
