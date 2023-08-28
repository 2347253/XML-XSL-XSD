from lxml import etree

# Load XML
xml_tree = etree.parse("file:///C:/Users/shawn/OneDrive/Desktop/Skate/Christ%20MCA/First%20Sem/WSD/XML-XSL-XSD/shopsmart.xml")

#load xsd
xsd = etree.parse("file:///C:/Users/shawn/OneDrive/Desktop/Skate/Christ%20MCA/First%20Sem/WSD/XML-XSL-XSD/shopsmart.xsd") 

# Load XSL
xsl_transform = etree.XSLT(etree.parse("file:///C:/Users/shawn/OneDrive/Desktop/Skate/Christ%20MCA/First%20Sem/WSD/XML-XSL-XSD/shopsmart.xsl"))

# Apply XSLT transformation
html_tree = xsl_transform(xml_tree)


# Write transformed HTML to a file
with open("output.html", "wb") as output_file:
    output_file.write(etree.tostring(html_tree, pretty_print=True))


schema = etree.XMLSchema(xsd)


# Validate transformed HTML against XSD schema
validation_result = schema.validate(xml_tree)

if validation_result:
    print("Validation successful!")
else:
    print("Validation errors:")
    print("Validation Result :",validation_result)
    print(schema.error_log)