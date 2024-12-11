def get_link_options(field):
    link_options = frappe.get_all(
        'Some Doctype',  # Replace with the actual Doctype name
        filters={"some_field": field},  # Replace with actual filters
        fields=["value"]  # Adjust based on what you need
    )

    if not link_options:
        return ""

    return "\n".join([str(doc['value']) for doc in link_options])
