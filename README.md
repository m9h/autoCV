# autoCV

[![PyPI version](https://badge.fury.io/py/autocv.svg)](https://badge.fury.io/py/autocv)

A tool for automatic generation of a LaTeX-based curriculum vitae (CV)

### Motivation

I recently wanted to update my CV to include all of my open science activities, such as links to open access papers, code/data, and include DOIs.  Rather than doing this by hand for each publication, I decided to build an automated tool to generate a CV using PubMed and ORCID to download the publication information, and a set of text files containing other info.  It's still a work in progress but it might be helpful for you; so far I have only tested it on my own CV, and it will almost certainly need work for others (especially if you have a common name that is not uniquely identified with a simple Pubmed query). It will be most useful for more advanced researchers whose CV may be many pages long.  

The project takes advantage of the [very nice LaTeX CV template](http://nitens.org/taraborelli/cvtex) from Dario Taraborelli.

### Structure

The idea behind this package is to use PubMed and ORCID to obtain an up-to-date CV in a relatively automated way.
Using it requires that the user first enter some relevant information into their ORCID account:

* Education
* Employment
* Invited Positions and Distinctions
* Membership and Service

In addition, it requires generating several CSV files containing other information that is not well organized or available within ORCID:

* **[conference.csv](tests/conference.csv)**: Conference presentations
* **[talks.csv](tests/talks.csv)**: Colloquium and other talks
* **[funding.csv](tests/funding.csv)**: Grants and other funding
* **[editorial.csv](tests/editorial.csv)**: Editorial duties and reviewing
* **[additional_pubs.csv](tests/additional_pubs.csv)**: Publications that are not found in PubMed/ORCID (including books, book chapters, and conference proceedings - note that ORCID allows addition of books but the metadata are a bit screwy, so I prefer entering them manually in this file)
* **[teaching.csv](tests/teaching.csv)**: Courses taught

It also allows addition of links to any reference using a csv file called **[links.csv](tests/links.csv)**.

Finally, you will need to generate a json file called params.json that contains some metadata about you - see example [here](tests/params.json).

You will need to take a look at the examples of these files in the repository to see their structure.

## Running the code

The easiest way to run the code is using Docker, which removes the need to install a full LaTeX installation.  After [installing the Docker client](https://docs.docker.com/get-docker/), you can simply install the package:

```pip install autocv```

and then use this command from a directory containing the necessary files:

```autoCV```

This will download the data and generate the CV files, and then render them to PDF.

To test it out, you can run it from within the *tests* directory, which contains example files for my CV.  You can see an example of the output [here](tests/autocv_template.pdf).