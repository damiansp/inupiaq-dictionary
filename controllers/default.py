# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    add_data = A('Add Data', _class = 'btn btn-primary',
                 _href = URL('default', 'add_data'))
    return dict(add_data = add_data)

# For dictionary input, specify allowed values for fields, where necessary
allowed_pos = ['n', 'v', 'adj', 'adv', 'prep', 'expr', 'art', 'conj']
allowed_pos_detail = ['coll', 'np']
allowed_gender = ['f', 'm']

def check_pos(form):
    if form.vars.pos not in allowed_pos:
        form.errors.pos = T('Accepted parts of speech are: "adj", "adv", ' +
                            '"art", "conj", "expr", "n", "prep", and "v".')
def check_gender(form):
    if form.vars.gender not in allowed_gender:
        form.errors.gender = T('Accepted genders are "f" and "m".')

def check_entry(form):
    check_pos(form)
    check_gender(form)
    
def add_data():
    '''Allow a user to input a new dictionary entry'''
    form = SQLFORM(db.gaighlig)

    if form.process(onvalidation = check_entry).accepted:
        session.flash = T('Entry added.')
        redirect(URL('add_data'))

    view_button = A('View Database', _class = 'btn btn-primary',
                    _href = URL('default', 'dictionary_display'))

    return dict(form = form, view_button = view_button)


def dictionary_display():
    '''Show contents of the dictiorary database (gaighlig.db)'''
    q = db.gaighlig
    grid = SQLFORM.grid(
        q,
        editable = True, # must be logged in to work
    )

    return dict(grid = grid)

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
