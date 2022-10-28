
# coding: utf-8

# # Publications markdown generator for academicpages
# 
# Takes a TSV of publications with metadata and converts them for use with [academicpages.github.io](academicpages.github.io). This is an interactive Jupyter notebook, with the core python code in publications.py. Run either from the `markdown_generator` folder after replacing `publications.tsv` with one that fits your format.
# 
# TODO: Make this work with BibTex and other databases of citations, rather than Stuart's non-standard TSV format and citation style.
# 

# ## Data format
# 
# The TSV needs to have the following columns: pub_date, title, venue, excerpt, citation, site_url, and paper_url, with a header at the top. 
# 
# - `excerpt` and `paper_url` can be blank, but the others must have values. 
# - `date` must be formatted as YYYY-MM-DD.
# - `permalink` will be the descriptive part of the .md file and the permalink URL for the page about the paper. The .md file will be `YYYY-MM-DD-[url_slug].md` and the permalink will be `https://[yourdomain]/publications/YYYY-MM-DD-[url_slug]`


# ## Import pandas
# 
# We are using the very handy pandas library for dataframes.

# In[2]:

import pandas as pd
import json


# ## Import TSV
# 
# Pandas makes this easy with the read_csv function. We are using a TSV, so we specify the separator as a tab, or `\t`.
# 
# I found it important to put this data in a tab-separated values format, because there are a lot of commas in this kind of data and comma-separated values can get messed up. However, you can modify the import statement, as pandas also has read_excel(), read_json(), and others.

# In[3]:

# publications = pd.read_csv("publications.tsv", sep="\t", header=0)
with open('publications.json') as f:
    publications_json = json.load(f)
    assert publications_json["collection"] == "publications"

    venues = dict(publications_json["venues"])

    d = {
        "title": [],
        "venue": [],
        "date": [],
        "award": [],
        "excerpt": [],
        "citation": [],
        "permalink": [],
        "link": [],
        "bibtex": [],
        "authors": []
    }
    for pub in publications_json["data"]:
        d["title"].append(pub["title"])

        if pub["venue"][0] == "@":
            d["venue"].append(venues[pub["venue"][1:]])
        else:
            d["venue"].append(pub["venue"])

        d["date"].append(pub["date"])
        d["excerpt"].append(pub["abstract"])
        d["permalink"].append(pub["permalink"])
        d["link"].append(pub["link"])
        d["citation"].append(pub["citation"])
        d["bibtex"].append(pub["bibtex"])
        d["authors"].append(pub["authors"])
        if "award" in pub:
            d["award"].append(pub["award"])
        else:
            d["award"].append("")
    publications = pd.DataFrame(d)

# ## Escape special characters
# 
# YAML is very picky about how it takes a valid string, so we are replacing single and double quotes (and ampersands) with their HTML encoded equivilents. This makes them look not so readable in raw format, but they are parsed and rendered nicely.

# In[4]:

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)


# ## Creating the markdown files
# 
# This is where the heavy lifting is done. This loops through all the rows in the TSV dataframe, then starts to concatentate a big string (```md```) that contains the markdown for each type. It does the YAML metadata first, then does the description for the individual page. If you don't want something to appear (like the "Recommended citation")

# In[5]:

import os
for row, item in publications.iterrows():
    
    md_filename = item.permalink + ".md"
    html_filename = item.permalink
    year = item.date[:4]
    
    ## YAML variables
    
    md = "---\ntitle: \""   + item.title + '"\n'
    
    md += """collection: publications"""
    
    md += """\npermalink: /publication/""" + html_filename
    
    if len(str(item.excerpt)) > 0:
        md += "\nexcerpt: '" + html_escape(item.excerpt) + "'"
    
    md += "\ndate: " + str(item.date) 

    if len(str(item.award)) > 0:
        md += "\naward: '" + html_escape(item.award) + "'"
    
    md += "\nvenue: '" + html_escape(item.venue) + "'"

    md += "\nauthors: '" + html_escape(item.authors) + "'"
    
    if len(str(item.link)) > 0:
        md += "\npaperurl: '" + item.link + "'"
    
    md += "\ncitation: '" + html_escape(item.citation) + "'"
    
    md += "\n---"
    
    ## Markdown description for individual page
    
    if len(str(item.link)) > 5:
        md += "\n\n<a href='" + item.link + "'>Download paper here</a>\n" 
        
    if len(str(item.excerpt)) > 5:
        md += "\n" + html_escape(item.excerpt) + "\n"
        
    md += "\nRecommended citation: " + item.citation
    md += "\n\n"

    md += "{% raw %}\n"
    md += "```\n"
    md += item.bibtex
    md += "\n```\n{% endraw %}\n"

    md_filename = os.path.basename(md_filename)
       
    with open("../_publications/" + md_filename, 'w') as f:
        f.write(md)
