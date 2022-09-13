import re


def test_field_on_home_page(app):
    field_from_home_page = app.contact.get_contact_list()[0]
    field_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert field_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(field_from_edit_page)
    assert clear(field_from_home_page.firstname) == clear(field_from_home_page.firstname)
    assert clear(field_from_edit_page.lastname) == clear(field_from_edit_page.lastname)
    assert clear(field_from_home_page.address) == clear(field_from_edit_page.address)
    assert clear_email(field_from_home_page.all_emails_from_home_page) == merge_emails_like_on_home_page(field_from_edit_page)


"""def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2"""



def clear(s):
    return re.sub("[\s ()-]", "", s)

def clear_email(s):
    return re.sub("\s", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != '',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != '',
                            map(lambda x: clear_email(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))