# bib2xml - A tool for getting Word formatted XML from Bibtex files

Processes Bibtex files (.bib), produces Word Bibliography XML (.xml) output

# Why not just use the Word tools?

You may already have the BibTex files and can't use Overleaf or prefer to use Word. This tool may be helpful.

# How can I use it?

Using Python3, you can just run the code giving the input and output paths:

    run bibtex2word.py -i bib-example.bib -o bib-example-xml.xml

After getting the XML file, You can go to: 

    Word > References > Manage Sources 
and then push the XML file to your source document in word.

The original code can be found at: [Paralax's Repo](https://github.com/paralax/bibtex2word)